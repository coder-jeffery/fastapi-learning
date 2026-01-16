# from pymilvus import Collection
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

collection_name = "user_collection"

if utility.has_collection(collection_name):
    # 删除所有数据（假设主键字段名为 "id"） | 清空某个 Collection 的所有数据（保留集合结构）
    print(f"集合 '{collection_name}' 存在")
    utility.drop_collection(collection_name)  # 如果 id 是整数  |  id是字符串 expr="id != ''"
    print(f"集合 '{collection_name}' 删除成功")
    utility.flush_all()
else:
    print(f"集合 '{collection_name}' 不存在")
