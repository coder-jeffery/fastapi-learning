# pip install langchain_openai
# top_p值相同，多次运行，比较结果
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
load_dotenv()
# top_p 影响明显：
# top_p = 0.1：输出更保守、集中，可能生成较常规的标题。
# top_p = 0.9：输出更发散、多样，可能出现更奇特、意想不到的创意。
# top_p=0.1, top_p=0.5, top_p=0.9 多次运行，观察输出的多样性和创造性变化。
# 初始化Qwen模型
chat_qwen = ChatOpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    model_name="qwen-plus",  # 可以根据需要更换为其他Qwen模型，如qwen-max等
    temperature=0.5,  # 控制输出的随机性
    top_p=0.2 #控制结果的多样性和创造性

)
response = chat_qwen.invoke("请发挥想象力，创作 5 个关于‘时间旅行者’的短篇小说标题")
print(response.content)

#  测试问题：
# "请发挥想象力，创作 5 个关于‘时间旅行者’的短篇小说标题。",
# "请列举 5 种未来可能存在的智能交通工具。",
# "请描述 5 个外星文明可能与人类不同的交流方式。",
# "请写出 5 句以‘如果世界突然失去重力’开头的科幻场景。",
