import numpy as np

class BM25lesson03:
    '''
    Z-Score+Sigmoid归一化

    '''

    def zscore_sigmoid_normalize(scores):
        """
        Z-Score + Sigmoid 归一化：将任意值域分值映射到 0-1
        :param scores: 原始分值列表（如 BM25 分值）
        :return: 归一化后的分值列表、均值μ、标准差σ
        """
        # 转换为 numpy 数组，方便数学计算
        scores_np = np.array(scores, dtype=np.float64)

        # 步骤1：计算 Z-Score 所需的均值μ和标准差σ（对应公式中的μ、σ）
        mu = np.mean(scores_np)  # 均值μ
        sigma = np.std(scores_np)  # 标准差σ
        print(f"Z-Score 计算：均值μ = {mu:.2f}，标准差σ = {sigma:.2f}")

        # 处理极端情况：所有分值相同（σ=0，避免除以 0）
        if sigma == 0:
            return np.zeros_like(scores_np).tolist(), mu, sigma

        # 步骤2：计算 Z-Score（对应公式 z = (x - μ)/σ）
        z_scores = (scores_np - mu) / sigma
        print(f"Z-Score 结果：{[round(z, 2) for z in z_scores]}")

        # 步骤3：Sigmoid 压缩（对应公式 s = 1/(1+e^-z)）
        sigmoid_scores = 1 / (1 + np.exp(-z_scores))

        # 转换回列表，方便后续融合使用
        return sigmoid_scores.tolist(), mu, sigma

    # 复用之前的普通 Min-Max 和截断 Min-Max 函数（对比用）
    def normal_min_max_normalize(scores):
        """普通 Min-Max 归一化"""
        scores_np = np.array(scores)
        min_val = np.min(scores_np)
        max_val = np.max(scores_np)
        if max_val == min_val:
            return np.zeros_like(scores_np).tolist()
        return ((scores_np - min_val) / (max_val - min_val)).tolist()

    def truncated_min_max_normalize(scores, truncate_percentile=95):
        """截断 Min-Max 归一化"""
        scores_np = np.array(scores)
        truncate_threshold = np.percentile(scores_np, truncate_percentile)
        truncated_scores = np.where(scores_np > truncate_threshold, truncate_threshold, scores_np)
        min_trunc = np.min(truncated_scores)
        max_trunc = np.max(truncated_scores)
        if max_trunc == min_trunc:
            return np.zeros_like(truncated_scores).tolist()
        return ((truncated_scores - min_trunc) / (max_trunc - min_trunc)).tolist()

    # ===================== 1. 模拟带极端值的 BM25 分值 =====================
    # 场景：10 个文档的 BM25 分值，前9个正常（0-20），第10个为极端值（100）
    bm25_scores = [15.2, 8.7, 20.5, 3.1, 0.0, 18.9, 12.4, 7.8, 19.3, 100.0]
    print("=== 原始 BM25 分值 ===")
    print([round(s, 2) for s in bm25_scores])
    print("-" * 60)

    # ===================== 2. 普通 Min-Max 归一化（对比） =====================
    normal_norm = normal_min_max_normalize(bm25_scores)
    print("=== 普通 Min-Max 归一化结果 ===")
    print([round(s, 2) for s in normal_norm])
    print("→ 问题：极端值（100）导致正常分值几乎都接近 0，区分度丢失")
    print("-" * 60)

    # ===================== 3. 截断 Min-Max 归一化（对比） =====================
    truncated_norm = truncated_min_max_normalize(bm25_scores, 95)
    print("=== 截断 Min-Max 归一化结果（95% 分位数） ===")
    print([round(s, 2) for s in truncated_norm])
    print("→ 改进：保留了正常分值的区分度，但依赖分位数调优")
    print("-" * 60)

    # ===================== 4. Z-Score+Sigmoid 归一化（核心） =====================
    zscore_sigmoid_norm, mu, sigma = zscore_sigmoid_normalize(bm25_scores)
    print("=== Z-Score+Sigmoid 归一化结果 ===")
    print([round(s, 2) for s in zscore_sigmoid_norm])
    print("→ 优势：无需调参，极值影响小，正常分值区分度高")