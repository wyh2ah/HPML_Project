import matplotlib.pyplot as plt
import numpy as np
from datasets import load_dataset
from transformers import AutoTokenizer

dataset_id = "dair-ai/emotion"
raw_dataset = load_dataset(dataset_id)
print(f"Dataset loaded. Train size: {len(raw_dataset['train'])}")

model_ckpt = "bert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_ckpt)

print("Tokenizing data to calculate lengths...")

def get_token_len(example):
    return len(tokenizer.encode(example["text"], add_special_tokens=True))

lengths = [get_token_len(ex) for ex in raw_dataset["train"]]

min_len = np.min(lengths)
max_len = np.max(lengths)
mean_len = np.mean(lengths)
median_len = np.median(lengths)
p90 = np.percentile(lengths, 90)
p95 = np.percentile(lengths, 95)
p99 = np.percentile(lengths, 99)

print("-" * 30)
print(f"Statistics for {model_ckpt} on {dataset_id}")
print("-" * 30)
print(f"Min Length: {min_len}")
print(f"Max Length: {max_len}")
print(f"Mean Length: {mean_len:.2f}")
print(f"Median Length: {median_len}")
print("-" * 30)
print(f"90% coverage length: {p90:.0f}")
print(f"95% coverage length: {p95:.0f}")
print(f"99% coverage length: {p99:.0f}")
print("-" * 30)

plt.figure(figsize=(10, 6))

plt.hist(lengths, bins=range(min_len, max_len + 2), alpha=0.7, color='skyblue', edgecolor='black')

plt.axvline(p95, color='red', linestyle='dashed', linewidth=2, label=f'95% ({int(p95)} tokens)')
plt.axvline(max_len, color='green', linestyle='dashed', linewidth=2, label=f'Max ({max_len} tokens)')

plt.axvline(64, color='orange', linestyle='dotted', linewidth=2, label='Length 64')
plt.axvline(128, color='purple', linestyle='dotted', linewidth=2, label='Length 128')

plt.title(f'Token Length Distribution: {dataset_id}', fontsize=14)
plt.xlabel('Number of Tokens (BERT Tokenizer)', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.legend()
plt.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig('token_length_distribution.png')
print("Chart saved to token_length_distribution.png")