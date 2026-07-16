"""ゲームの進行（入力・表示・ループ）。

★ チームで足す機能は **自分の担当の場所**に書く（1機能=1ファイル）。
   下の「ここに足す」場所は3か所（① 開始時 ② 入力コマンド ③ 勝利時）。
   ペアごとに**別の場所**を直すので、並行作業でも衝突しない。
   import も自分の場所の近くに書くこと（ファイル先頭にまとめない＝衝突回避）。
"""

from .core import judge, make_secret

def play(digits=3):
    secret = make_secret(digits)
    print(f"Hit & Blow（{digits} 桁・重複なし）")

    # ===== ① 開始時に足す（難易度・あいさつ など）: ここに書く =====
    from .limit import LimitManager
    limit_manager = LimitManager(digits)
    print(limit_manager.get_initial_message())

    tries = 0
    while True:
        guess = input("予想 > ").strip()

        # ===== ② 入力コマンドに足す（ヒント など）: ここに書く（import もここに） =====
        # 最終ターンの場合、結果表示後のフローを制御するために判定を先読みします。
        if limit_manager.is_final_turn(tries):
            # 正しい形式の場合のみ判定を行います。不正な場合はベースの処理に任せて再入力を促します。
            if len(guess) == digits and guess.isdigit():
                temp_hit, temp_blow = judge(secret, guess)
                if temp_hit != digits:
                    # 不正解の場合はここで結果を表示し、ゲームオーバー処理を行って終了します。
                    # （正解の場合はベースの処理に任せ、③の勝利時処理へ進ませます）
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

            print(f"正解！ {tries} 回で当たり（答え {secret}）")
            break