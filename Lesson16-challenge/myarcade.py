import argparse
import sys
import myguess_number
from rps import rps


def myarcade(name):
    print(f"\n{name}, welcome to the Arcade! 🤖\n")

    def game_start():

        playgame = input(
            f"\nPlease choose a game:\n1 = Rock Paper Scissors\n2 = Guess My Number\n\nOr press \"x\" to exit the Arcade\n\n")
        if playgame.lower() not in ["1", "2", "x"]:
            print(f"{name}, please enter 1, 2, or x.")
            return game_start()

        if playgame == "1":
            guess_number = myguess_number.my_guess_number_game(name)
            guess_number()
            print(f"\n{name}, welcome back to the Arcade menu.\n")
            return game_start()  # 重新執行myarcade()這個函數，因此裡面記得加name
        elif playgame == "2":
            rpsgame = rps(name)
            rpsgame()  # 跟上面 guess_number不同用法
            print(f"\n{name}, welcome back to the Arcade menu.\n")
            return game_start()
        elif playgame.lower() == "x":
            print(f"\nSee you next time!\n\nBye {name}! 👋")
            sys.exit()

    game_start()


parser = argparse.ArgumentParser(
    description="Provide a personalized guess number game."
)

parser.add_argument(
    "-n", "--name", metavar="name",
    required=True, help="The name of the player."
)

if __name__ == "__main__":
    args = parser.parse_args()

    myarcade(args.name)
