import argparse
import sys
import random as rdm


def my_guess_number_game(name='Player'):
    game_count = 0
    wins = 0

    def game_begin():
        nonlocal game_count
        nonlocal wins
        player = input(
            f"\n{name}, guess what number I'm thinking of 1, 2 or 3.\n\n ")

        if player not in ["1", "2", "3"]:
            return game_begin()
        my_choice = rdm.choice("123")

        print(f"{name}, you chose {
              player}.\nI was thinking about the number {my_choice}.\n")
        game_count += 1
        if int(player) == my_choice:
            wins += 1
            print(f"🎉{name}, you win!")
        else:
            print(f"Sorry, {name}. Better luck next time. 😢\n")

        print(f"Game count: {game_count}\n")
        print(f"{name}'s wins: {wins}\n")
        print(f"Your winning percentage: {wins/game_count:.2%}\n")

        while True:
            again = input(f"Play again, {name}?\n\nY for Yes or\nQ for Quit\n")
            if again.lower() not in ["y", "q"]:
                continue
            else:
                break
        if again.lower() == "y":
            return game_begin()  # 如果用my_guess_number_game()會重新建立一新遊戲，而不是在舊有的遊戲繼續

        else:
            if __name__ == "__main__":
                print(f"\n🎉🎉🎉🎉\nThank you for playing!\n\nBye {name}! 👋")
                sys.exit()  # break只能用在中斷迴圈或是switch，但return可以用在函數上，且可以回傳值
            else:
                return
    return game_begin


parser = argparse.ArgumentParser(
    description="Provide a personalized guess number game."
)

parser.add_argument(
    "-n", "--name", metavar="name",
    required=True, help="The name of the player."
)

if __name__ == "__main__":
    args = parser.parse_args()

    mygame = my_guess_number_game(args.name)
    mygame()
