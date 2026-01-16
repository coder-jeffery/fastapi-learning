import os
import requests
from dotenv import load_dotenv
"""
#### 3.1 代码演示（使用 deepseek + CoT 技术）  
- 以下示例展示如何用 Python 实现思维链提示，解决数学应用题：
"""
# 加载环境变量
load_dotenv()
api_key = os.getenv("DEEPSEEK_API_KEY")
if not api_key:
    print("请在 .env 文件中设置 DEEPSEEK_API_KEY")
    exit(1)


def solve_with_cot(problem):
    # 构建思维链提示
    prompt = f"""
你是一个数学解题专家，请用中文分步推理并解答问题。格式：
问题：[问题描述]
思考：[逐步推理过程]
答案：[最终答案]
现在请解答：
问题：{problem}
思考：
答案：
"""

    # 准备 API 请求
    url = "https://api.deepseek.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "system", "content": "你是一个专业的数学解题助手，请使用思维链进行一步一步推理，显示推理过程"},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.3,
        "max_tokens": 300,
        "stream": False
    }

    try:
        # 发送请求
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()  # 检查HTTP错误

        # 解析响应
        response_data = response.json()
        return response_data['choices'][0]['message']['content']

    except requests.exceptions.RequestException as e:
        print(f"API请求失败: {e}")
        return None
    except KeyError:
        print("API响应格式错误")
        print("完整响应:", response_data)
        return None


# 测试问题
problems = [
    "一箱鸡蛋有48个，每周用掉15个。4周后还剩几个鸡蛋？",
    "火车以80公里/小时的速度行驶，3小时后还剩240公里到达目的地。总路程是多少公里？",
    "班级有30名学生，60%是男生，男生中有1/3戴眼镜。戴眼镜的男生有多少人？"
]

for i, problem in enumerate(problems, 1):
    print(f"\n{'=' * 40}")
    print(f"问题 {i}: {problem}")
    print(f"{'=' * 40}")

    result = solve_with_cot(problem)

    if result:
        print("\n模型解答：")
        print(result)
    else:
        print("获取解答失败")

    print("\n")