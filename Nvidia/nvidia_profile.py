import os, time, math, json, random
from dataclasses import dataclass
from typing import Optional, Dict, Any
import torch
from torch import nn
from torch.utils.data import DataLoader
from torch.cuda.amp import autocast, GradScaler

from datasets import load_dataset
import evaluate
from transformers import (
    AutoTokenizer, AutoModelForSequenceClassification,
    DataCollatorWithPadding, default_data_collator,
    get_linear_schedule_with_warmup, Trainer, TrainingArguments, set_seed
)

import os, time, math, json, random
from dataclasses import dataclass

import torch
from datasets import load_dataset
import evaluate
from transformers import (
    AutoTokenizer, AutoModelForSequenceClassification,
    DataCollatorWithPadding,
    Trainer, TrainingArguments, set_seed,
)

device = "cuda" if torch.cuda.is_available() else "cpu"
if device == "cuda":
    gpu_name = torch.cuda.get_device_name(0)
    cc_major, cc_minor = torch.cuda.get_device_capability(0)
else:
    gpu_name = "CPU"
    cc_major, cc_minor = (0, 0)
print(device)
bf16_supported = torch.cuda.is_available() and torch.cuda.is_bf16_supported()
dtype_for_amp = torch.bfloat16 if bf16_supported else torch.float16

print(f"Device: {gpu_name}, CC: {cc_major}.{cc_minor}, bf16_supported={bf16_supported}")

@dataclass
class Config:
    dataset_id: str = "dair-ai/emotion"
    model_name: str = "bert-base-uncased"
    lr: float = 5e-5
    per_device_batch_size: int = 8
    num_epochs: int = 3
    use_bf16: bool = bf16_supported
    use_fp16: bool = (not bf16_supported) and torch.cuda.is_available()
    weight_decay: float = 0.0
    warmup_ratio: float = 0.0
    grad_accum_steps: int = 1
    seed: int = 42
    output_dir: str = "/content/bert_emotion_gpu"

cfg = Config()
os.makedirs(cfg.output_dir, exist_ok=True)
set_seed(cfg.seed)


raw_ds = load_dataset(cfg.dataset_id)

print(raw_ds)
print("Train size:", len(raw_ds["train"]))
print("Test size: ", len(raw_ds["test"]))

tokenizer = AutoTokenizer.from_pretrained(cfg.model_name, use_fast=True)

def tokenize(batch):
    return tokenizer(
        batch["text"],
        padding="max_length",
        truncation=True,
    )

tokenized = raw_ds.map(tokenize, batched=True, remove_columns=["text"])

train_ds = tokenized["train"]
eval_ds  = tokenized["test"]

num_labels = len(raw_ds["train"].features["label"].names)
print("num_labels:", num_labels)

data_collator = DataCollatorWithPadding(
    tokenizer=tokenizer,
    pad_to_multiple_of=None
)


metric_acc = evaluate.load("accuracy")

def compute_metrics(eval_pred):
    logits, labels = eval_pred
    preds = logits.argmax(-1)
    return metric_acc.compute(predictions=preds, references=labels)


model = AutoModelForSequenceClassification.from_pretrained(
    cfg.model_name, num_labels=num_labels
).to(device)

bf16 = cfg.use_bf16
fp16 = cfg.use_fp16 and (not bf16)

print(f"Using bf16={bf16}, fp16={fp16}")

training_args = TrainingArguments(
    output_dir=os.path.join(cfg.output_dir, "trainer_baseline"),
    per_device_train_batch_size=cfg.per_device_batch_size,
    per_device_eval_batch_size=cfg.per_device_batch_size,
    gradient_accumulation_steps=cfg.grad_accum_steps,
    num_train_epochs=cfg.num_epochs,
    learning_rate=cfg.lr,
    weight_decay=cfg.weight_decay,
    warmup_ratio=cfg.warmup_ratio,
    logging_steps=50,
    eval_strategy="epoch",
    save_strategy="no",
    report_to="none",
    fp16=fp16,
    bf16=bf16,
    max_steps=10,
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_ds,
    eval_dataset=eval_ds,
    tokenizer=tokenizer,
    data_collator=data_collator,
    compute_metrics=compute_metrics,
)

t0 = time.perf_counter()
train_result = trainer.train()

trainer.save_model()
train_metrics = train_result.metrics
trainer.log_metrics("train", train_metrics)
trainer.save_metrics("train", train_metrics)
trainer.save_state()

eval_metrics = trainer.evaluate()
trainer.log_metrics("eval", eval_metrics)
trainer.save_metrics("eval", eval_metrics)



