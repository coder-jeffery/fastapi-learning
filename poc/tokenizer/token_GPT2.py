#GPT-2
from transformers import GPT2Tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
text = "hello,how are you?"
tokens = tokenizer.tokenize(text)  # ['Hello', ',', 'Ġhow', 'Ġare', 'Ġyou', '?']
print(tokens)
# 转ID
input_ids = tokenizer.encode(text)
print("Input IDs:", input_ids)

# 解码
decoded_text = tokenizer.decode(input_ids)
print("Decoded:", decoded_text)