"""回数制限を管理する機能モジュール。"""

class LimitManager:
    def __init__(self, digits):
        # 桁数に応じて制限回数を変更できるよう、辞書で定義します。
        self.limits = {
            3: 10,
            4: 12,
            5: 15
        }
        self.max_tries = self.limits.get(digits, 10)

    def get_initial_message(self):
        """ゲーム開始時にユーザーへ提示するメッセージを返します。"""
        return f"【お知らせ】回答の回数制限は {self.max_tries} 回です。"

    def is_final_turn(self, current_tries):
        """
        現在のターンが最終ターン（制限回数の直前）かどうかを判定します。
        """
        return current_tries == self.max_tries - 1

    def print_game_over(self, secret):
        """ゲームオーバー時のメッセージを出力します。"""
        print(f"\nゲームオーバーです。正解は {secret} でした。")