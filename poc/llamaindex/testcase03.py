# from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
# from llama_index.embeddings.huggingface import HuggingFaceEmbedding
# from llama_index.llms.ollama import Ollama
#
# # 1. 加载数据
# documents = SimpleDirectoryReader("data/").load_data()
#
# # 2. 配置嵌入模型和 LLM
# embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-large-zh")
# llm = Ollama(model="qwen:7b")
#
# # 3. 构建索引
# index = VectorStoreIndex.from_documents(documents, embed_model=embed_model)
#
# # 4. 创建查询引擎
# query_engine = index.as_query_engine(llm=llm, similarity_top_k=3)
#
# # 5. 提问
# response = query_engine.query("公司年假政策是什么？")
# print(response)