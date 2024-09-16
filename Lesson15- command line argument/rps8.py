import sys
import random
from enum import Enum


def rps(name='Playone'):
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():
        nonlocal name
        nonlocal player_wins
        nonlocal python_wins

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        playerchoice = input(
            f"\n{name}, please enter... \n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n")

        if playerchoice not in ["1", "2", "3"]:
            print(f"{name}, please enter 1, 2, or 3.")
            return play_rps()

        player = int(playerchoice)

        computerchoice = random.choice("123")

        computer = int(computerchoice)

        print(f"\n{name},you chose {
              str(RPS(player)).replace('RPS.', '').title()}.")
        print(
            f"Python chose {str(RPS(computer)).replace('RPS.', '').title()}.\n"
        )  # Enum是"枚舉類別"而不是基本的數值型別，雖然 f-string 可以自動將整數或浮點數轉換為字串，但它不會自動將自訂物件（如 Enum）轉換為可讀的名稱

        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins
            nonlocal python_wins
            if player == 1 and computer == 3:
                player_wins += 1
                return f"🎉 {name} win!"
            elif player == 2 and computer == 1:
                player_wins += 1
                return f"🎉 {name} win!"
            elif player == 3 and computer == 2:
                player_wins += 1
                return f"🎉 {name} win!"
            elif player == computer:
                return "😲 Tie game!"
            else:
                python_wins += 1
                return f"🐍 Python wins!\nSorry, {name}..😢"

        game_result = decide_winner(player, computer)

        print(game_result)

        nonlocal game_count
        game_count += 1

        print(f"\nGame count: {game_count}")
        # 這裡不用str()，因為f-string會自動將整束轉為字串
        print(f"\n{name}'s wins: {player_wins}")
        print(f"\nPython wins: {python_wins}")

        print("\nPlay again, {name}?")

        while True:
            playagain = input("\nY for Yes or \nQ to Quit\n")
            if playagain.lower() not in ["y", "q"]:
                continue
            else:
                break

        if playagain.lower() == "y":
            return play_rps()
        else:
            print("\n🎉🎉🎉🎉")
            print("Thank you for playing!\n")
            sys.exit("Bye! {name}! 👋")

    return play_rps


# rock_paper_scissors = rps()

if __name__ == "__main__":
    # 這段argparse是一個 boilerplate 樣板文件，指編寫中經常重複使用的標準化代碼或文字。這些內容通常沒有太大的變化，具有高度通用性，並且可以在不同的專案中重複使用。
    # 所以直接從hello_person裡面複製過來就好

    import argparse

    # argumentparser 參數解析器
    parser = argparse.ArgumentParser(
        description="Provides a personalized game experence."
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person playing the game. "
    )

    args = parser.parse_args()

    rock_paper_scissors = rps(args.name)
    rock_paper_scissors()
