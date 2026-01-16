from sentence_transformers import SentenceTransformer
from pymilvus import (
    connections,
    FieldSchema, CollectionSchema, DataType,
    Collection, utility
)
import numpy as np

# ----------------------------
# 1. 初始化 Milvus 连接
# ----------------------------
# 使用 Milvus Lite（自动创建本地 milvus.db 文件）
connections.connect("default", host="localhost", port="19530")  # 本地文件模式

collection_name = "text_embeddings"

# 删除已有集合（可选，用于测试）
if utility.has_collection(collection_name):
    utility.drop_collection(collection_name)

# ----------------------------
# 2. 定义 Schema
# ----------------------------
dim = 384  # all-MiniLM-L6-v2 的输出维度

fields = [
    FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=True),
    FieldSchema(name="text", dtype=DataType.VARCHAR, max_length=65535),
    FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=dim)
]

schema = CollectionSchema(fields, description="Text embedding collection")
collection = Collection(collection_name, schema)

# 创建索引（HNSW 适合高精度，IVF_FLAT 适合大数据）
index_params = {
    "index_type": "HNSW",
    "metric_type": "COSINE",  # 或 L2
    "params": {"M": 8, "efConstruction": 64}
}
collection.create_index("embedding", index_params)
collection.load()

# ----------------------------
# 3. 加载 Embedding 模型
# ----------------------------
model = SentenceTransformer('all-MiniLM-L6-v2')  # 轻量级，适合金融文本

# ----------------------------
# 4. 插入数据
# ----------------------------
texts = [
    "外资银行在合规科技（RegTech）领域大量投入AI系统。",
    "大模型量化技术可显著降低推理成本，满足数据本地化要求。",
    "智能反欺诈系统利用图神经网络识别跨境洗钱行为。",
    "生成式AI在财富管理中的应用需严格遵循MiFID II披露规则。"
]

embeddings = model.encode(texts).tolist()

# 插入数据（id 自增，无需提供）
insert_result = collection.insert([texts, embeddings])
print(f"Inserted {len(insert_result.primary_keys)} records.")

# ----------------------------
# 5. 执行查询
# ----------------------------
query_text = "如何用AI降低银行的合规成本？"
query_embedding = model.encode([query_text]).tolist()

search_params = {"metric_type": "COSINE", "params": {"ef": 64}}
results = collection.search(
    data=query_embedding,
    anns_field="embedding",
    param=search_params,
    limit=2,  # 返回最相似的2条
    output_fields=["text"]
)

print("\n🔍 查询结果：")
for i, result in enumerate(results[0]):
    print(f"{i+1}. 相似度: {1 - result.distance:.4f} | 文本: {result.entity.get('text')}")