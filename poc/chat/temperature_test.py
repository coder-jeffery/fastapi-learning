#pip install langchain_openai
#在相同temperature相同的前提下，一个问题多次运行，看运行结果的差异
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
load_dotenv()
chat_qwen = ChatOpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    model_name="qwen-max",
    temperature=0.95,  # 控制输出的随机性
    max_tokens=1024  # 最大生成 tokens 数量
)
response = chat_qwen.invoke("为一款会飞的运动鞋设计3句广告语")
print(response.content)