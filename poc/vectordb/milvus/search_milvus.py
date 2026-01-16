import texts
from pymilvus import connections, Collection
from sentence_transformers import SentenceTransformer

connections.connect(host="localhost", port="19530")
collection = Collection("text_embeddings_20251216")
print(collection.schema)

model = SentenceTransformer('all-MiniLM-L6-v2')

embeddings = model.encode(texts).tolist()

query_text = "如何用AI降低银行的合规成本？"

query_embedding = model.encode([query_text]).tolist()

search_params = {"metric_type": "COSINE", "params": {"ef": 64}}
results = collection.search(
    data=query_embedding,
    anns_field="embedding",
    param=search_params,
    limit=4,  # 返回最相似的2条
    output_fields=["text"]
)

print(results)

