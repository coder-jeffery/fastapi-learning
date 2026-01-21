import numpy as np


'''

Min-Max归一化：
    norm_bm25 = (bm25 - min_bm25) / (max_bm25 - min_bm25)
    

'''
# ===================== 1. 模拟检索结果 =====================
# 假设检索到 5 个文档，每个文档的 BM25 分（0-∞）和向量余弦相似度（0-1）
documents = [
    {"id": 1, "bm25": 15.2, "vector_sim": 0.92},  # 关键词+语义都优
    {"id": 2, "bm25": 8.7, "vector_sim": 0.85},   # 语义优，关键词一般
    {"id": 3, "bm25": 20.5, "vector_sim": 0.60},  # 关键词优，语义一般
    {"id": 4, "bm25": 3.1, "vector_sim": 0.78},   # 语义较好，关键词差
    {"id": 5, "bm25": 0.0, "vector_sim": 0.90},   # 语义优，无关键词匹配
]

# ===================== 2. BM25 归一化（Min-Max） =====================
# 提取本次检索的 BM25 分值，计算批次内的 min/max
bm25_scores = [doc["bm25"] for doc in documents]
min_bm25 = min(bm25_scores)
max_bm25 = max(bm25_scores)

# 处理极端情况：所有 BM25 分值相同（避免除以 0）
if max_bm25 == min_bm25:
    norm_bm25_scores = [0.0 for _ in bm25_scores]
else:
    norm_bm25_scores = [(s - min_bm25) / (max_bm25 - min_bm25) for s in bm25_scores]

# 为每个文档添加归一化后的 BM25 分
for i, doc in enumerate(documents):
    doc["norm_bm25"] = norm_bm25_scores[i]
    # print(doc)

# print(documents)

# ===================== 3. 加权线性融合 =====================
alpha = 0.4  # BM25 权重（语义型场景，α 取 0.3-0.5）
for doc in documents:
    # 综合分数 = 0.4*归一化BM25 + 0.6*向量相似度
    doc["final_score"] = alpha * doc["norm_bm25"] + (1 - alpha) * doc["vector_sim"]

# ===================== 4. 按综合分数降序排序 =====================
sorted_docs = sorted(documents, key=lambda x: x["final_score"], reverse=True)

# ===================== 输出结果 =====================
print("综合排序结果（final_score 越高越相关）：")
for doc in sorted_docs:
    print(f"文档{doc['id']} | BM25归一化：{doc['norm_bm25']:.2f} | 向量相似度：{doc['vector_sim']:.2f} | 综合分数：{doc['final_score']:.2f}")