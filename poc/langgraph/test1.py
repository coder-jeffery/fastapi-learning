from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from langgraph_supervisor import create_supervisor
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
import os

load_dotenv()
DASHSCOPE_API_KEY = os.getenv("DASHSCOPE_API_KEY")
model_name = os.getenv("MODEL_NAME")
base_url = os.getenv("BASE_URL")

model = ChatOpenAI(
    model=model_name,
    api_key=DASHSCOPE_API_KEY,
    temperature=0.0,
    base_url=base_url
)


def book_hotel(hotel_name: str):
    """订酒店"""
    return f"酒店预定成功： {hotel_name}."


def book_flight(from_airport: str, to_airport: str):
    """订飞机票"""
    return f"飞机票预定成功： {from_airport} to {to_airport}."


flight_assistant = create_react_agent(
    model=model,
    tools=[book_flight],
    prompt="""
你是一名航班预订助手。
- 仅处理航班预订相关请求（例如：“预订从A地到B地的航班”）。
- 若请求中包含非航班类任务（例如：酒店预订），请勿对这些部分进行回应。
- 处理完航班相关事务后，立即将控制权交回主管，并告知主管需处理其他剩余任务。""",
    name="flight_assistant"
)

hotel_assistant = create_react_agent(
    model=model,
    tools=[book_hotel],
    prompt="""
你是一名酒店预订助手。
- 仅处理酒店预订相关请求（例如：“预订X酒店的住宿”）。
- 若请求中包含非酒店类任务（例如：航班预订），请勿对这些部分进行回应。
- 处理完酒店相关事务后，立即将控制权交回主管。
""",
    name="hotel_assistant"
)

supervisor = create_supervisor(
    agents=[flight_assistant, hotel_assistant],
    model=model,
    prompt="""
你负责管理航班和酒店助手，工作流程：
1. 从用户请求中提取关键信息：
   - 航班：出发地、目的地
   - 酒店：城市、酒店名称
2. 先调用航班助手，将航班参数（出发地、目的地）传给它；
3. 航班完成后，调用酒店助手，将酒店参数（城市、酒店名称）传给它；
4. 汇总结果回复用户。
"""
).compile()

result = supervisor.invoke({
    "messages": [
        HumanMessage(content="我订一张飞机票，从北京到上海的，并且在上海帮忙订万达酒店")
    ]
})
# print(result)
# 假设 result 是你的结果字典
for msg in result['messages']:
    # 确定角色（用户/助手名称）
    if isinstance(msg, HumanMessage):
        role = "用户"
    else:
        role = msg.name
        # 提取内容（工具调用类消息可能没有content，用工具名代替）
    content = msg.content if msg.content else f"[调用工具: {msg.tool_calls[0]['name']}]"

    print(f"{role}: {content}")
