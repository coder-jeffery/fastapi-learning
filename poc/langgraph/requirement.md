1.  conda create -n chapter_11 python=3.11
2. conda activate chapter_11
3.安装依赖

pip install langchain
pip install dotenv
pip install langgraph-supervisor
pip install langchain_openai
pip install langgraph.prebuilt import create_react_agent
from langgraph_supervisor import create_supervisor
pip install langgraph-swarm

把env文件中的DASHSCOPE_API_KEY="" 换成你的qwen的api_key