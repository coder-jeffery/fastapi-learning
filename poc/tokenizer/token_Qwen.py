# Qwen
from transformers import Qwen2Tokenizer
tokenizer = Qwen2Tokenizer.from_pretrained("Qwen/Qwen1.5-72B")

# 使用示例
text = "hello,how are you?"
tokens = tokenizer.tokenize(text)
input_ids = tokenizer.encode(text)

print("Tokens:", tokens)
print("Input IDs:", input_ids)
print("Decoded:", tokenizer.decode(input_ids))