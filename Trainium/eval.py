import argparse
import torch
import numpy as np
from transformers import AutoModelForSequenceClassification, AutoTokenizer, DataCollatorWithPadding
from datasets import load_dataset
from torch.utils.data import DataLoader
from tqdm import tqdm

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model_path", type=str, required=True, help="Path to the saved model directory")
    parser.add_argument("--dataset_name", type=str, default="dair-ai/emotion", help="Dataset name")
    return parser.parse_args()

def main():
    args = parse_args()
    
    print(f"Loading model from: {args.model_path}")
    
    device = torch.device("cpu")
    
    try:
        model = AutoModelForSequenceClassification.from_pretrained(args.model_path)
        tokenizer = AutoTokenizer.from_pretrained(args.model_path)
    except OSError:
        print("error")
        return

    model.to(device)
    model.eval()

    print(f"Loading dataset: {args.dataset_name}")
    dataset = load_dataset(args.dataset_name)
    
    def tokenize_function(example):
        return tokenizer(example["text"], truncation=True, padding="max_length", max_length=128)

    eval_dataset = dataset["validation"].map(tokenize_function, batched=True)
    eval_dataset = eval_dataset.remove_columns(["text", "label_text"] if "label_text" in eval_dataset.column_names else ["text"])
    eval_dataset.set_format("torch")

    data_collator = DataCollatorWithPadding(tokenizer=tokenizer)
    eval_dataloader = DataLoader(eval_dataset, batch_size=32, collate_fn=data_collator)

    print("Starting evaluation...")
    all_preds = []
    all_labels = []

    with torch.no_grad():
        for batch in tqdm(eval_dataloader):
            batch = {k: v.to(device) for k, v in batch.items()}
            outputs = model(**batch)
            logits = outputs.logits
            preds = torch.argmax(logits, dim=-1)
            
            all_preds.extend(preds.numpy())
            all_labels.extend(batch["labels"].numpy())

    correct = np.sum(np.array(all_preds) == np.array(all_labels))
    total = len(all_labels)
    accuracy = correct / total

    print("\n" + "="*30)
    print(f"Model: {args.model_path}")
    print(f"Accuracy: {accuracy:.4f} ({accuracy*100:.2f}%)")
    print("="*30 + "\n")

if __name__ == "__main__":
    main()