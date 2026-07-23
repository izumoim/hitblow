"""ゲームの進行（入力・表示・ループ）。

★ チームで足す機能は **自分の担当の場所**に書く（1機能=1ファイル）。
"""

from .core import judge, make_secret


def play():

    # ===== ① 開始時に足す（難易度・あいさつ など）: ここに書く =====
    from .difficulty import DifficultyManager
    from .limit import LimitManager

    difficulty = DifficultyManager()
    digits = difficulty.select_digits()

    secret = make_secret(digits)

    print(f"Hit & Blow（{digits} 桁・重複なし）")

    limit_manager = LimitManager(digits)
    print(limit_manager.get_initial_message())

    tries = 0

    while True:
        guess = input("予想 > ").strip()

        # ===== ② 入力コマンドに足す（ヒント など）: ここに書く（import もここに） =====

        if limit_manager.is_final_turn(tries):
            if len(guess) == digits and guess.isdigit():
                temp_hit, temp_blow = judge(secret, guess)

                if temp_hit != digits:
                    tries += 1
                    print(f"  Hit={temp_hit}  Blow={temp_blow}")
                    limit_manager.print_game_over(secret)
                    break

        if len(guess) != digits or not guess.isdigit():
            print(f"{digits} 桁の数字で入力してね")
            continue

        tries += 1

        hit, blow = judge(secret, guess)

        print(f"  Hit={hit}  Blow={blow}")

        if hit == digits:

            # ===== ③ 勝利時に足す（スコア・履歴 など）: ここに書く =====
            from .score import calculate_score
            # limit_manager から最大試行回数を取得して計算関数へ渡す
            score = calculate_score(digits, tries, limit_manager.max_tries)
            print(f"正解！ {tries} 回で当たり（答え {secret}）")
            print(f"獲得スコア: {score} 点")
            break