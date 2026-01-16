# 需要restart kernal，因为state是全局保存的，清空

from langgraph.prebuilt import create_react_agent
from langgraph_swarm import create_swarm, create_handoff_tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
load_dotenv()
DASHSCOPE_API_KEY=os.getenv("DASHSCOPE_API_KEY")
base_url=os.getenv("BASE_URL")
model_name=os.getenv("MODEL_NAME")

model = ChatOpenAI(
    model=model_name,
    api_key=DASHSCOPE_API_KEY,
    temperature=0.0,
    base_url=base_url
)
def book_hotel(hotel_name: str):
    """Book a hotel"""
    return f"Successfully booked a stay at {hotel_name}."

transfer_to_hotel_assistant = create_handoff_tool(
    agent_name="hotel_assistant",
    description="Transfer user to the hotel-booking assistant.",
)
transfer_to_flight_assistant = create_handoff_tool(
    agent_name="flight_assistant",
    description="Transfer user to the flight-booking assistant.",
)
def book_flight(from_airport: str, to_airport: str):
    """Book a flight"""
    return f"Successfully booked a flight from {from_airport} to {to_airport}."

flight_assistant = create_react_agent(
    model=model,
    tools=[book_flight, transfer_to_hotel_assistant],
    prompt="You are a flight booking assistant",
    name="flight_assistant"
)
hotel_assistant = create_react_agent(
    model=model,
    tools=[book_hotel, transfer_to_flight_assistant],
    prompt="You are a hotel booking assistant",
    name="hotel_assistant"
)

swarm = create_swarm(
    agents=[flight_assistant, hotel_assistant],
    default_active_agent="flight_assistant",
    routing_policy="intelligent"
).compile()



result = swarm.invoke({
    "messages": [
        HumanMessage(content="book a flight from BOS to JFK and a stay at McKittrick Hotel")
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
