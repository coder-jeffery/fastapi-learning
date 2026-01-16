# from pymilvus import Collection
from mpmath.libmp import to_str
from pymilvus import (
    connections,
    FieldSchema, CollectionSchema, DataType,
    Collection, utility
)
import random
import numpy as np


# 文本相似检索：将文本转为 128 维向量，存入 embedding 字段，检索时通过查询向量匹配该字段；
# 图像特征检索：将图像特征转为 128 维向量，存入该字段，实现以图搜图；
# 推荐系统：将用户 / 商品特征转为 128 维向量，存入该字段，实现相似用户 / 商品推荐

# 小维度（64/128 维）：适配轻量级模型，检索速度快，适合简单文本 / 小规模数据；
# 中维度（256/384 维）：平衡速度与效果，是文本嵌入的主流选择（如 MiniLM-L6-v2）；
# 高维度（768/1536 维）：适配大模型嵌入（如 BERT/OpenAI/Qwen），效果更好但检索 / 存储成本更高。


# ----------------------------
# 1. 初始化 Milvus 连接
# ----------------------------
# 使用 Milvus Lite（自动创建本地 milvus.db 文件）
connections.connect("default", host="localhost", port="19530")  # 本地文件模式

collection_name = "user_collection"

if utility.has_collection(collection_name):
    # 删除所有数据（假设主键字段名为 "id"） | 清空某个 Collection 的所有数据（保留集合结构）
    print(f"集合 '{collection_name}' 存在")
    utility.drop_collection(collection_name)  # 如果 id 是整数  |  id是字符串 expr="id != ''"
    print(f"集合 '{collection_name}' 删除成功")
else:
    print(f"集合 '{collection_name}' 不存在")
    # utility.connections.create_collection(collection_name)
    # print(f"集合 '{collection_name}' 创建成功🏅")


if not utility.has_collection(collection_name):
    #定义 schema 定义字段
    user_id = FieldSchema(
        name="user_id",
        dtype=DataType.INT64,
        is_primary=True,
        auto_id=False  # 我们自己提供 user_id
    )

    username = FieldSchema(
        name="username",
        dtype=DataType.VARCHAR,
        max_length=100
    )

    bio = FieldSchema(
        name="bio",
        dtype=DataType.VARCHAR,
        max_length=500
    )

    embedding = FieldSchema(
        name="embedding",
        dtype=DataType.FLOAT_VECTOR,
        dim=128  # 向量维度
    )

    schema = CollectionSchema(
        collection_name=collection_name,
        fields=[
            user_id,username,bio,embedding
        ],
        description="User table with vector embedding"
    )

    # #创建集合
    collection = Collection(collection_name, schema=schema)
    collection.flush()
    print(f"集合 {collection_name} 创建成功")

    # 插入测试数据
    # 模拟生成一些用户数据
    users = [
        {
            "user_id": 1,
            "username": "alice",
            "bio": "AI researcher",
            "embedding": [random.random() for _ in range(128)]
        },
        {
            "user_id": 2,
            "username": "bob",
            "bio": "Data engineer",
            "embedding": [random.random() for _ in range(128)]
        },
        {
            "user_id": 3,
            "username": "charlie",
            "bio": "ML engineer",
            "embedding": [random.random() for _ in range(128)]
        }
    ]

    # 准备插入的数据（按字段组织）
    insert_data = {
        "user_id": [u["user_id"] for u in users],
        "username": [u["username"] for u in users],
        "bio": [u["bio"] for u in users],
        "embedding": [u["embedding"] for u in users]
    }

    # # # 插入
    # Convert dictionary to list of lists (pay attention to order of fields in schema)
    data_to_insert = [
        insert_data["user_id"],
        insert_data["username"],
        insert_data["bio"],
        insert_data["embedding"]
    ]
    collection.insert(data_to_insert)

    collection.flush()  # 确保数据落盘，可查
    print("✅ 数据插入成功，共插入", len(users), "条记录")
    
    # 创建索引
    index_params = {
        "metric_type": "L2",
        "index_type": "IVF_FLAT",
        "params": {"nlist": 1024}
    }

    collection.create_index(
        field_name="embedding", 
        index_params=index_params
    )

    print("✅ 索引创建成功")

    # # 查询 user_id 为 1 和 2 的用户
    collection.load()
    result = collection.query(
        expr="username=='alice'",
        output_fields=["user_id", "username", "bio", "embedding"]
    )

    for row in result:
        print(row)




#彻底删除整个 Collection（包括结构和数据）
# utility.drop_collection("text_collection")

# 刷新（可选，确保删除生效）
# collection.flush()