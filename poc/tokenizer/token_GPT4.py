import tiktoken

enc = tiktoken.get_encoding("cl100k_base")  # GPT-4 使用的编码
enc.encode("Hello, 世界!")  # → [15496, 11, 87508, 0, 100257]

print(enc.decode("utf-8"))