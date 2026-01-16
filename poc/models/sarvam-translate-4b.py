from transformers import AutoTokenizer, AutoModelForCausalLM

# 指向你的本地模型路径
model_path = "./qwen-1_8b"  # ← 改成你的路径

# 加载 tokenizer 和模型
tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    model_path,
    trust_remote_code=True,
    device_map="auto",        # 自动使用 GPU（如果有）
    torch_dtype="auto"        # 自动选择 float16 / bfloat16 节省显存
)

# 输入文本
prompt = "解释量子计算的基本原理。"

# 编码 + 生成
inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
outputs = model.generate(
    **inputs,
    max_new_tokens=200,
    do_sample=True,
    temperature=0.7,
    top_p=0.9
)

# 解码输出
response = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(response)