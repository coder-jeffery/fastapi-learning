import numpy as np


class BM25lesson02:
    '''
截断归一化
            np.percentile  - > np.clip
    1.计算截断阈值：统计数据的目标分位数（如 95% 分位数），作为截断上限；
    2.截断极值：将所有超过该阈值的分值替换为阈值（低于阈值的分值保持不变）；
    3.Min-Max 归一化：对截断后的数据执行普通 Min-Max 归一化，映射到 0-1。

    '''
    import numpy as np

    def truncated_min_max_normalize(scores, truncate_percentile=95):
        """
        截断归一化：先按分位数截断极值，再做 Min-Max 归一化
        :param scores: 原始分值列表（如 BM25 分值）
        :param truncate_percentile: 截断分位数（常用 90/95/99）
        :return: 截断归一化后的分值列表、截断阈值、截断后的 min/max
        """
        # 转换为 numpy 数组（方便分位数计算）
        scores_np = np.array(scores)

        # 步骤1：计算截断阈值（指定分位数对应的分值）
        truncate_threshold = np.percentile(scores_np, truncate_percentile)
        print(f"截断阈值（{truncate_percentile}% 分位数）：{truncate_threshold:.2f}")

        # 步骤2：截断极值（超过阈值的替换为阈值）
        truncated_scores = np.where(scores_np > truncate_threshold, truncate_threshold, scores_np)

        # 步骤3：对截断后的数据做 Min-Max 归一化
        min_truncated = np.min(truncated_scores)
        max_truncated = np.max(truncated_scores)

        # 处理极端情况：所有分值相同（避免除以 0）
        if max_truncated == min_truncated:
            normalized_scores = np.zeros_like(truncated_scores)
        else:
            normalized_scores = (truncated_scores - min_truncated) / (max_truncated - min_truncated)

        # 转换回列表，方便后续处理
        return normalized_scores.tolist(), truncate_threshold, (min_truncated, max_truncated)

    def normal_min_max_normalize(scores):
        """普通 Min-Max 归一化（对比用）"""
        scores_np = np.array(scores)
        min_val = np.min(scores_np)
        max_val = np.max(scores_np)
        if max_val == min_val:
            return np.zeros_like(scores_np).tolist()
        return ((scores_np - min_val) / (max_val - min_val)).tolist()

    # ===================== 1. 模拟带极端值的 BM25 分值 =====================
    # 场景：10 个文档的 BM25 分值，前9个分值正常（0-20），第10个为极端值（100）
    bm25_scores = [15.2, 8.7, 20.5, 3.1, 0.0, 18.9, 12.4, 7.8, 19.3, 100.0]
    print("原始 BM25 分值：", [round(s, 2) for s in bm25_scores])
    print("-" * 50)

    # ===================== 2. 普通 Min-Max 归一化（对比） =====================
    normal_normalized = normal_min_max_normalize(bm25_scores)
    print("普通 Min-Max 归一化结果：", [round(s, 2) for s in normal_normalized])
    print("→ 问题：极端值（100）导致大部分正常分值归一化后接近 0，失去区分度")
    print("-" * 50)

    # ===================== 3. 截断归一化（95% 分位数） =====================
    truncated_normalized, truncate_thresh, (min_trunc, max_trunc) = truncated_min_max_normalize(
        bm25_scores, truncate_percentile=95
    )
    print(f"截断后的数据范围：[{min_trunc:.2f}, {max_trunc:.2f}]")
    print("截断归一化结果：", [round(s, 2) for s in truncated_normalized])
    print("→ 优势：正常分值的区分度被保留，极端值影响被消除")

bm25 = [8.2,5.1,12.5,2.3,6.7,25.1]
bm25score  = np.array(bm25)
p  = 95
trunc_threshold = np.percentile(bm25score, p)
print(trunc_threshold)
bm25_truncated = np.clip(bm25score, min=None, max = trunc_threshold)
print(bm25_truncated)

# 4. 截断后执行 Min-Max 归一化
bm25_min = bm25_truncated.min()
bm25_max = bm25_truncated.max()

bm25_norm = (bm25_truncated - bm25_min) / (bm25_max - bm25_min)
print("\n截断归一化后的 BM25 得分（0~1）：", np.round(bm25_norm, 2))

