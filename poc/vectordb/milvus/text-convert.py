# from sentence_transformers import SentenceTransformer
# from transformers import AutoTokenizer, AutoModel
# # 或直接用 SentenceTransformer 加载 HuggingFace 模型
# model = SentenceTransformer('BAAI/bge-small-zh-v1.5')


from pymilvus import connections, FieldSchema, CollectionSchema, DataType, Collection, utility
from sentence_transformers import SentenceTransformer

# 1. 连接 Milvus
connections.connect("default", host="localhost", port="19530")  # 本地 Milvus

# 2. 定义文本数据
texts = [
    "人工智能是计算机科学的一个分支。",
    "机器学习是实现人工智能的一种方法。",
    "深度学习使用神经网络进行特征学习。"
]

# 3. 使用嵌入模型生成向量
model = SentenceTransformer('all-MiniLM-L6-v2')  # 轻量级英文模型；中文可用 'paraphrase-multilingual-MiniLM-L12-v2'
embeddings = model.encode(texts).tolist()  # 转为 list 以便插入

# 4. 定义集合结构（schema）
collection_name = "text_collection"

# 如果集合已存在，先删除（可选）
if utility.has_collection(collection_name):
    utility.drop_collection(collection_name)

# 定义字段
id_field = FieldSchema(
    name="id",
    dtype=DataType.INT64,
    is_primary=True,
    auto_id=True
)
embedding_field = FieldSchema(
    name="embedding",
    dtype=DataType.FLOAT_VECTOR,
    dim=len(embeddings[0])  # 例如 384（MiniLM 输出维度）
)
text_field = FieldSchema(
    name="text",
    dtype=DataType.VARCHAR,
    max_length=65535  # 支持长文本（Milvus 2.2+）
)

# 创建 schema 和 collection
schema = CollectionSchema(fields=[id_field, embedding_field, text_field], description="Text embedding collection")
collection = Collection(name=collection_name, schema=schema)

# 5. 插入数据
data = [
    embeddings,   # 向量字段
    texts         # 文本字段（与 schema 中顺序一致）
]

collection.insert(data)
collection.flush()  # 确保数据落盘

print(f"成功插入 {len(texts)} 条文本数据到 Milvus 集合 '{collection_name}'")


