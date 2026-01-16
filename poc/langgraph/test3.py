
from langgraph.prebuilt import create_react_agent
from langgraph_swarm import create_swarm, create_handoff_tool
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()
DASHSCOPE_API_KEY = os.getenv("DASHSCOPE_API_KEY")
base_url = os.getenv("BASE_URL")
model_name = os.getenv("MODEL_NAME")

model = ChatOpenAI(
    model=model_name,
    api_key=DASHSCOPE_API_KEY,
    temperature=0.0,
    base_url=base_url
)


# 工具定义
def book_hotel(hotel_name: str):
    """Book a hotel by name"""
    return f"Successfully booked a stay at {hotel_name}."


def book_flight(from_airport: str, to_airport: str):
    """Book a flight between two airports"""
    return f"Successfully booked a flight from {from_airport} to {to_airport}."


# 创建通用的转移工具
def create_transfer_tool(target_agent: str):
    """动态创建转移工具"""
    return create_handoff_tool(
        agent_name=target_agent,
        description=f"Transfer user to the {target_agent.replace('_', ' ')}.",
    )


# 创建路由代理 - 核心改进
def create_router_agent():
    """创建智能路由代理，决定将用户请求路由到哪个专业代理"""
    router_prompt = """你是一个智能路由助手。根据用户的问题内容，决定将请求路由到最合适的专业助手：

可用的专业助手：
- hotel_assistant: 处理酒店预订相关请求（包含酒店、住宿、旅馆等关键词）
- flight_assistant: 处理航班预订相关请求（包含航班、机票、飞行、机场等关键词）

分析用户的问题，如果主要涉及酒店预订，使用 transfer_to_hotel_assistant 工具。
如果主要涉及航班预订，使用 transfer_to_flight_assistant 工具。
如果同时涉及两者，先处理最紧急或最明确的部分，然后转移。

请仔细分析用户意图后做出路由决定。"""

    return create_react_agent(
        model=model,
        tools=[
            create_transfer_tool("hotel_assistant"),
            create_transfer_tool("flight_assistant")
        ],
        prompt=router_prompt,
        name="router_agent"
    )


# 创建专业代理
flight_assistant = create_react_agent(
    model=model,
    tools=[book_flight, create_transfer_tool("hotel_assistant")],
    prompt="""你是专业的航班预订助手。专注于处理：
1. 查询航班信息
2. 预订机票
3. 航班改签
4. 机票退订

如果用户提到酒店预订，请使用 transfer_to_hotel_assistant 工具将用户转接给酒店专家。""",
    name="flight_assistant"
)

hotel_assistant = create_react_agent(
    model=model,
    tools=[book_hotel, create_transfer_tool("flight_assistant")],
    prompt="""你是专业的酒店预订助手。专注于处理：
1. 查询酒店信息
2. 预订酒店房间
3. 酒店价格比较
4. 酒店退订

如果用户提到航班预订，请使用 transfer_to_flight_assistant 工具将用户转接给航班专家。""",
    name="hotel_assistant"
)

# 创建路由代理
router_agent = create_router_agent()

# 创建智能群组
swarm = create_swarm(
    agents=[router_agent, flight_assistant, hotel_assistant],
    default_active_agent="router_agent",  # 默认从路由代理开始
    routing_policy="intelligent"
).compile()


# 测试函数
def test_swarm(user_message):
    print(f"\n{'=' * 50}")
    print(f"测试输入: {user_message}")
    print(f"{'=' * 50}")

    result = swarm.invoke({
        "messages": [HumanMessage(content=user_message)]
    })

    for msg in result['messages']:
        if isinstance(msg, HumanMessage):
            role = "用户"
        else:
            role = f"助手({msg.name})" if hasattr(msg, 'name') and msg.name else "助手"

        content = msg.content if msg.content else ""
        if hasattr(msg, 'tool_calls') and msg.tool_calls:
            tool_info = f" [调用工具: {', '.join([tool['name'] for tool in msg.tool_calls])}]"
            content += tool_info

        if content.strip():
            print(f"{role}: {content}")


# 测试不同场景
test_cases = [
    # "我想订一个从北京到上海的航班",
    # "请帮我预订希尔顿酒店的房间",
    # "我需要订从纽约到伦敦的机票，并且想在伦敦预订万豪酒店",
    # "查询一下明天北京飞广州的航班",
    # "推荐一些好的商务酒店"
]

for test_case in test_cases:
    test_swarm(test_case)