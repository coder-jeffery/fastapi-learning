from transformers import AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained("gpt-3.5-turbo")
input_text = "Hello World! how are you?"
token_count = len(tokenizer(input_text)["input_ids"])
print(f"token count:",{token_count})