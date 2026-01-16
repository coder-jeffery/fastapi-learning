import re
from typing import List
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage
import os
from dotenv import load_dotenv
""""
让大模型LLM自主语义分割
"""

load_dotenv()

# 配置qwen-max模型参数（阿里云灵积平台兼容OpenAI格式）

API_SECRET = os.getenv("DASHSCOPE_API_KEY")
API_BASE_URL = "https://dashscope.aliyuncs.com/compatible-mode/v1"  # 阿里云兼容端点
def split_text_with_qwen(long_text: str, max_chunk_words: int = 500) -> List[str]:
    # 初始化ChatOpenAI客户端（兼容模式）
    chat = ChatOpenAI(
        model_name="qwen-max",
        base_url=API_BASE_URL,
        api_key=API_SECRET,
        temperature=0.3,
        max_tokens=2048
    )

    # 构建提示词
    prompt = f"""请将以下文本分割成多个语义完整的块，要求：
1. 每个块围绕一个核心主题，避免拆分完整的事件描述或逻辑单元；
2. 每个块长度控制在200-{max_chunk_words}字之间；
3. 用"### 块X"（X为序号，从1开始）作为每个块的开头，仅输出分割结果，不添加额外说明。

文本：{long_text}
"""

    # 调用模型
    response = chat.invoke([HumanMessage(content=prompt)])
    segmented_text = response.content.strip()
    # 解析结果
    chunks = re.split(r'### 块\d+', segmented_text)
    chunks = [chunk.strip() for chunk in chunks if chunk.strip()]
    return chunks

def process_long_document(document_path: str, max_initial_chunk: int = 3000) -> List[str]:
    """处理超长文档：先粗分再精细化分割"""
    # 读取文档
    with open(document_path, "r", encoding="utf-8") as f:
        full_text = f.read()

    # 粗分处理
    initial_chunks = []
    start = 0
    text_length = len(full_text)
    while start < text_length:
        end = start + max_initial_chunk
        if end < text_length:
            end = full_text.rfind('。', start, end) or end
        initial_chunks.append(full_text[start:end].strip())
        start = end

    # 精细化分割
    final_chunks = []
    for chunk in initial_chunks:
        if chunk:
            final_chunks.extend(split_text_with_qwen(chunk))

    return final_chunks


# 使用示例
if __name__ == "__main__":
    try:
        chunks = process_long_document("news.txt")
        print(f"qwen-max分割完成，共生成 {len(chunks)} 个块")
        for i, chunk in enumerate(chunks[:2], 1):
            print(f"\n=== 块{i} ===\n{chunk[:200]}...")
    except Exception as e:
        print(f"处理失败：{str(e)}")
