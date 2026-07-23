"""難易度（桁数）選択を管理するモジュール。"""

class DifficultyManager:
    def select_digits(self):
        """プレイヤーに桁数を選ばせる。"""
        while True:
            choice = input("桁数を選んでください（3 / 4 / 5）> ").strip()

            if choice in ("3", "4", "5"):
                return int(choice)

            print("3・4・5 のいずれかを入力してください。")