# Google 开发，无需预分词，直接从原始文本训练（支持中英文混合）。
# 支持 BPE 和 unigram 两种算法。
# 代表模型：T5、mT5、ALBERT、XLNet
# 优点：端到端处理，适合多语言。


# 主流 NLP 框架中的分词器
    # BERT / RoBERTa	WordPiece / BPE	需先用空格分词（英文），中文直接字符级
    # GPT 系列	BPE	基于字节（byte-level BPE），无需预分词
    # T5 / mT5	SentencePiece	直接处理原始文本，支持多语言
    # LLaMA / Mistral	BPE（byte-level）	使用 tokenizer.model（SentencePiece 格式但实际是 BPE）
    # ChatGLM	自定义 BPE	中英混合优化
    # Qwen	tiktoken 兼容 BPE	类似 GPT-4 的分词方式

# import sentencepiece as spm
# sp = spm.SentencePieceProcessor(model_file='your_model.model')
# sp.encode("Hello world")  # → [IDs]