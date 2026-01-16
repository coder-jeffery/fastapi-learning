# # 安装依赖
# pip install llama-index-core llama-index-llms-openai llama-index-embeddings-openai llama-index-tools-calculator python-dotenv requests

import os
import requests
from dotenv import load_dotenv
from llama_index.core.memory import ChatMemoryBuffer
from llama_index.core.vector_stores.simple import SimpleVectorStore

 # 旧版
# LlamaIndex 核心导入
from llama_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
)
from llama_index.core.agent import ReActAgent
from llama_index.core.tools import FunctionTool, ToolMetadata

from llama_index.llms.openai import OpenAI
# 从独立的 embeddings-openai 子包导入 OpenAIEmbedding
from llama_index.embeddings.openai import OpenAIEmbedding

# 加载环境变量（需配置 OPENAI_API_KEY）
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")


# ===================== 步骤1：定义工具（Agent 的「手脚」） =====================
# 工具1：计算器（本地工具）
def calculate(expression: str) -> str:
    """
    数学计算工具，支持加减乘除、平方、开方等简单运算
    :param expression: 数学表达式，如 "1+2*3"、"sqrt(16)"
    :return: 计算结果
    """
    try:
        # 安全执行计算（避免恶意代码）
        allowed_ops = {"+", "-", "*", "/", "sqrt", "pow", "abs"}
        # 过滤非法字符
        clean_expr = "".join([c for c in expression if c.isdigit() or c in allowed_ops or c in "()."])
        result = eval(clean_expr, {k: getattr(__builtins__, k) for k in allowed_ops})
        return f"计算结果：{expression} = {result}"
    except Exception as e:
        return f"计算失败：{str(e)}，请检查表达式格式（如 '1+2*3'）"


# 工具2：天气查询（外部 API 工具，需替换为免费天气 API）
def get_weather(city: str) -> str:
    """
    查询城市天气
    :param city: 城市名，如 "北京"、"上海"
    :return: 天气信息
    """
    try:
        # 示例：使用免费天气 API（可替换为其他接口）
        url = f"http://wthrcdn.etouch.cn/weather_mini?city={city}"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()

        if data.get("desc") != "success":
            return f"查询失败：未找到 {city} 的天气数据"

        weather_info = data["data"]["forecast"][0]
        return (
            f"{city} 今日天气：{weather_info['type']}，"
            f"温度 {weather_info['low']}~{weather_info['high']}，"
            f"风向 {weather_info['fengxiang']}，风力 {weather_info['fengli']}"
        )
    except Exception as e:
        return f"天气查询失败：{str(e)}，请检查城市名或网络"


# 工具3：知识库检索（RAG 工具，读取本地文档）
def load_knowledge_base() -> VectorStoreIndex:
    """加载本地知识库（docs 目录下的文本/Markdown/PDF 文件）"""
    # 读取文档（需在当前目录创建 docs 文件夹，放入测试文档）
    try:
        documents = SimpleDirectoryReader("./docs").load_data()
        # 构建向量索引（使用 OpenAI 嵌入模型）
        embedding = OpenAIEmbedding(model="text-embedding-3-small")
        index = VectorStoreIndex.from_documents(
            documents,
            embed_model=embedding
        )
        return index
    except FileNotFoundError:
        # 无文档时返回空索引
        return VectorStoreIndex.from_documents([], embed_model=OpenAIEmbedding())


def search_knowledge_base(query: str) -> str:
    """
    检索知识库回答问题
    :param query: 检索问题
    :return: 知识库中的相关答案
    """
    index = load_knowledge_base()
    if not index.docstore.docs:
        return "知识库为空，请先在 ./docs 目录下放入文档"

    # 检索 Top-3 相关内容
    query_engine = index.as_query_engine(similarity_top_k=3)
    response = query_engine.query(query)
    return f"知识库检索结果：\n{response}"


# 封装工具为 LlamaIndex Tool
calculator_tool = FunctionTool.from_defaults(
    fn=calculate,
    metadata=ToolMetadata(
        name="calculator",
        description="数学计算工具，用于解决加减乘除等数学运算问题，输入为数学表达式"
    )
)

weather_tool = FunctionTool.from_defaults(
    fn=get_weather,
    metadata=ToolMetadata(
        name="weather",
        description="天气查询工具，输入为城市名，返回该城市的当日天气信息"
    )
)

knowledge_tool = FunctionTool.from_defaults(
    fn=search_knowledge_base,
    metadata=ToolMetadata(
        name="knowledge_base",
        description="知识库检索工具，用于回答与本地文档相关的问题，输入为检索关键词/问题"
    )
)

# ===================== 步骤2：初始化记忆（Agent 的「记忆」） =====================
# 短期记忆：会话窗口（保留最近 10 轮对话）
chat_memory = ChatMemoryBuffer.from_defaults(token_limit=2000)

# 长期记忆：向量存储（可选，用于跨会话记忆）
long_term_memory = MemoryVectorStore(embed_model=OpenAIEmbedding())

# ===================== 步骤3：初始化 LLM（Agent 的「大脑」） =====================
llm = OpenAI(model="gpt-3.5-turbo", temperature=0.1)

# ===================== 步骤4：创建 ReAct Agent（核心） =====================
# 整合工具列表
tools = [calculator_tool, weather_tool, knowledge_tool]

# 创建 ReAct Agent（基于 ReAct 框架，支持「推理+行动」）
agent = ReActAgent.from_tools(
    tools,
    llm=llm,
    memory=chat_memory,
    verbose=True,  # 打印思考/执行过程
    max_iterations=10,  # 最大迭代次数（避免无限循环）
    context="你是一个智能助手，能够使用计算器、天气查询、知识库检索工具回答问题。优先使用工具解决问题，工具无法解决时再直接回答。"
)


# ===================== 步骤5：运行 Agent =====================
def run_agent():
    print("=== LlamaIndex AI Agent 启动（输入 'exit' 退出）===")
    while True:
        user_input = input("\n你：")
        if user_input.lower() == "exit":
            print("Agent 已退出")
            break

        # 执行 Agent 推理
        response = agent.chat(user_input)
        print(f"\nAgent：{response.response}")


if __name__ == "__main__":
    # 首次运行前，可创建 docs 目录并放入测试文档（如 knowledge.txt）
    if not os.path.exists("./docs"):
        os.makedirs("./docs")
        # 写入测试文档
        with open("./docs/knowledge.txt", "w", encoding="utf-8") as f:
            f.write("LlamaIndex 是一款开源的 RAG 框架，专为大模型应用设计。\n")
            f.write("AI Agent 具备感知、决策、执行、反馈、记忆五大核心能力。\n")
            f.write("向量数据库的核心作用是存储高维向量，支持相似性检索。")

    run_agent()