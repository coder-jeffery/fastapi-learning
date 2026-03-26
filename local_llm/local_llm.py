import argparse
import os
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent
PROJECT_HOME = PROJECT_ROOT / ".crewai_home"
PROJECT_HOME.mkdir(exist_ok=True)

# Keep CrewAI's local SQLite storage inside the project so it remains writable.
os.environ["HOME"] = str(PROJECT_HOME)

try:
    from crewai import Agent, Task, Crew
except ModuleNotFoundError as exc:
    if exc.name == "crewai":
        venv_python = PROJECT_ROOT / "local_llm_env" / "bin" / "python"
        message = [
            "Missing dependency: crewai",
            f"Use the project virtualenv: {venv_python} {Path(__file__).name}",
            "Or install dependencies with: python3 -m pip install -r requirements.txt",
        ]
        raise SystemExit("\n".join(message)) from exc
    raise

# --- 1. 配置环境变量，让 CrewAI 自动连接 Ollama ---
# 设置模型名称，确保这个名字和你用 'ollama pull' 下载的名字一致
MODEL_NAME = os.environ.get("OLLAMA_MODEL_NAME", "Qwen:1.8b")

os.environ['OPENAI_API_BASE'] = 'http://localhost:11434/v1' # 注意：Ollama 的兼容路径通常是 /v1
os.environ['OPENAI_API_KEY'] = 'NA'
os.environ['OLLAMA_MODEL_NAME'] = MODEL_NAME
# 设置 Ollama 的服务地址
os.environ['OLLAMA_BASE_URL'] = 'http://localhost:11434'


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run a local CrewAI workflow with custom input.")
    parser.add_argument("--topic", help="调研主题，例如：本地AI Agent")
    parser.add_argument("--words", type=int, default=500, help="文章字数，默认 500")
    parser.add_argument("--style", default="博客文章", help="输出形式，例如：博客文章、播客稿、短视频文案")
    return parser.parse_args()


def prompt_if_missing(value: str | None, prompt_text: str, default: str | None = None) -> str:
    if value:
        return value
    suffix = f" [{default}]" if default else ""
    user_input = input(f"{prompt_text}{suffix}: ").strip()
    if user_input:
        return user_input
    if default is not None:
        return default
    raise SystemExit(f"{prompt_text}不能为空")


args = parse_args()
topic = prompt_if_missing(args.topic, "请输入调研主题", "本地AI Agent")
style = prompt_if_missing(args.style, "请输入输出形式", "博客文章")
word_count = args.words

# --- 2. 定义智能体 (Agents) ---
# 注意：这里不再需要传入 llm=local_llm 参数
researcher = Agent(
    role='研究分析师',
    goal='查找关于指定主题的准确、全面的信息',
    backstory='你是一位注重细节、擅长信息搜集的专业研究员。',
    llm=f'ollama/{MODEL_NAME}',
    verbose=True
)

writer = Agent(
    role='内容创作者',
    goal='基于研究资料，撰写一篇清晰、有吸引力的博客文章',
    backstory='你是一位优秀的作家，擅长将复杂信息转化为通俗易懂的内容。',
    llm=f'ollama/{MODEL_NAME}',
    verbose=True
)

reader = Agent(
    role='读者' ,
    goal = '基于上述材料总结文章',
    backstory ='你是一位优秀的阅读者',
    llm=f'ollama/{MODEL_NAME}',
    verbose=True
)



# --- 3. 定义任务 (Tasks) ---
research_task = Task(
    description=f'调研“{topic}”的最新发展趋势和核心优势。',
    agent=researcher,
    expected_output='一份包含关键发现的详细调研摘要。'
)

writing_task = Task(
    description=f'根据研究员提供的资料，撰写一篇{word_count}字左右的{style}。',
    agent=writer,
    expected_output=f'一篇润色完成的{style}。',
    context=[research_task]
)

reader_task = Task(
    description=f'阅读并总结研究内容，输出一份适合读者快速理解的{style}摘要。',
    agent=reader,
    expected_output=f"一份简洁清晰的{style}摘要。",
    context=[research_task]
)

# --- 4. 创建并启动团队 (Crew) ---
my_crew = Crew(
    agents=[researcher, writer, reader],
    tasks=[research_task, writing_task, reader_task],
    verbose=True
)

# 开始执行！
print("🚀 Agent团队开始工作...")
print(f"主题: {topic}")
print(f"输出形式: {style}")
print(f"目标字数: {word_count}")
result = my_crew.kickoff()
print("\n\n✨ 最终成果：")
print(result)
