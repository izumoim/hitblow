"""スコア計算機能モジュール。"""

def calculate_score(digits, tries, max_tries):
    """
    最大試行回数、実際の試行回数、桁数に基づいてスコアを計算します。
    計算式: (最大の試行回数 - 実際の試行回数) * 桁数 * 100
    """
    score = (max_tries - tries) * digits * 100 + 100
    return max(0, score)