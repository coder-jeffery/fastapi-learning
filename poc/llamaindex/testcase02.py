from sympy.printing.pytorch import torch
from transformers import AutoTokenizer, AutoModel

# 注意：这是 Qwen2.5 或 Qwen3 的 base 模型（非 chat 版）
tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen3-4B", trust_remote_code=True)
model = AutoModel.from_pretrained("Qwen/Qwen3-4B", trust_remote_code=True)

text = "自然语言处理很强大"
inputs = tokenizer(text, return_tensors="pt")
with torch.no_grad():
    outputs = model(**inputs)
    embedding = outputs.last_hidden_state[:, -1, :]  # 取最后一个 token（类似 GPT 风格）

    print(embedding)
