import faiss
import numpy as np

# 假设你有 3 个用户
embeddings = np.array([
    [0.1, 0.2],
    [0.3, 0.4],
    [0.5, 0.6]
], dtype='float32')

usernames = ["alice", "bob", "charlie"]
bios = ["AI lover", "Engineer", "Student"]

# 创建 Faiss 索引
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

# 搜索
query = np.array([[0.15, 0.25]], dtype='float32')
distances, indices = index.search(query, k=2)

# 获取 metadata
for i, idx in enumerate(indices[0]):
    print(f"Top {i+1}: username={usernames[idx]}, bio={bios[idx]}, dist={distances[0][i]}")