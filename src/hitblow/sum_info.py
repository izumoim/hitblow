"""数字の和を計算する機能モジュール。"""

def calculate_sum(number_str):
    """
    渡された数字文字列の各桁の和を計算して返します。
    （例: "123" -> 1 + 2 + 3 = 6）
    """
    return sum(int(digit) for digit in number_str)