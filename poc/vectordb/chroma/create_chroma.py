import chromadb

# 1. 初始化Chroma客户端（持久化到本地磁盘）
client = chromadb.PersistentClient(path="chroma_data")

# 2. 创建/获取集合（Collection）
collection = client.get_or_create_collection(name="chroma_rag_collection")

# 3. 插入文本数据（自动转向量，无需手动处理）
collection.add(
    documents=[
        "Chroma是轻量级向量数据库，专为RAG设计",
        "Chroma支持元数据过滤和相似性检索",
        "Chroma兼容LangChain，可快速集成到大模型应用"
    ],
    metadatas=[
        {"category": "intro"},
        {"category": "feature"},
        {"category": "integration"}
    ],
    ids=["id1", "id2", "id3"]  # 自定义ID，可选自动生成
)

# 4. 相似性检索
results = collection.query(
    query_texts=["Chroma如何集成到RAG？"],  # 查询文本（自动转向量）
    n_results=2,  # 返回Top-2相似结果
    where={"category": {"$in": ["feature", "integration"]}}  # 元数据过滤
)

print("检索结果：", results)