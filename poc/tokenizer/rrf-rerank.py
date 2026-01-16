def rrf_fusion(results_list, weights=None, k=60):
    """
    results_list: List[List[doc_id]]，每个子列表是一个检索器的 top-K 结果（按相关性降序）
    weights: 各检索器的权重，长度需与 results_list 一致
    k: RRF 平滑参数
    """
    if weights is None:
        weights = [1.0] * len(results_list)

    rrf_score = {}

    for result, weight in zip(results_list, weights):
        for rank, doc_id in enumerate(result):
            rrf_score[doc_id] = rrf_score.get(doc_id, 0) + weight / (k + rank + 1)

    # 按得分降序排序
    sorted_docs = sorted(rrf_score.items(), key=lambda x: x[1], reverse=True)
    return [doc_id for doc_id, _ in sorted_docs]


# 示例使用
bm25_results = ["A", "B", "C"]
vector_results = ["B", "D", "A"]
final_ranking = rrf_fusion([bm25_results, vector_results], weights=[0.3, 0.7])
print(final_ranking)  # 可能输出: ['B', 'A', 'D', 'C']