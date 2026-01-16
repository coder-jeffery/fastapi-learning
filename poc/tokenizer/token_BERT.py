# pip install transformers
#BERT base
from transformers import BertTokenizer
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
text = "hello,how are you?"
tokens = tokenizer.tokenize(text)  # ['hello', ',', 'how', 'are', 'you', '?']
print(tokens)
# 转ID
input_ids = tokenizer.encode(text)
print("Input IDs:", input_ids)

# 解码
decoded_text = tokenizer.decode(input_ids)
print("Decoded:", decoded_text)