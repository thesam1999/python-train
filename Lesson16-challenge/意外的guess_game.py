import argparse  # 參數解析，parser是解析器的意思
import random as rdm
import sys


def guess_number(name="Playerone"):
    game_count = 0
    wins = 0

    def gamebegin():
        nonlocal game_count
        nonlocal wins
        game_count += 1

        playerchoice = input(
            f"\n{name}, guess which number I'm thinking of... 1, 2, or 3. ")

        if playerchoice not in ["1", "2", "3"]:
            print(f"{name}, please enter 1, 2, or 3.")
            return guess_number()

        number = (1, 2, 3)
        Ichoose = rdm.choice(number)
        print(f"\n{name} , you chose {playerchoice
                                      }.\nI was thinking about the number {Ichoose}.")

        if int(playerchoice) == Ichoose:  # input回傳值是字串，rdm是回傳數字
            print(f"\n🎉{name}, you win! ")
            wins += 1
        else:
            print(f"Sorry, {name}. Better luck next time. 😢")

        print(f"\nGame count: {game_count}")
        print(f"\n{name}'s wins: {wins}")
        print(f"\nYour winning percentage: {wins/game_count:.2%}")
        # while錯誤的縮排
    while True:
        gamebegin()
        again = input(f"\nPlay again. {name}?\n\nY for Yes or\nQ for Quit\n")
        # 不能用is not，這種比較是沒有意義的，因為 again.lower() 是一個字符串，而 ["y", "q"] 是一個列表，兩者永遠不會是同一個對象，因此這個條件永遠會評估為 True，導致 continue 永遠執行，從而造成無限循環或不正確的行為。
        if again.lower() not in ["y", "q"]:
            continue
        # is not是用來比較兩個對象的身分，即內存中的位置(即他們的內存位置)，即使內容相同，但他們來源不同那就是不同。            break
        else:
            break

    if again.lower() == "y":
        return gamebegin()
    else:
        print(f"🎉🎉🎉🎉\nThank you for playing!\n\nBye {name}!👋")
        sys.exit()


parser = argparse.ArgumentParser(
    description="Provide a personal guess number game!"
)

parser.add_argument(
    "-n", "--name", metavar="name",
    required=True, help="Please input the name of player."

)

if __name__ == "__main__":

    args = parser.parse_args()

    game = guess_number(args.name)  # 要這樣寫，才能記住之前遊戲的技術和勝利次數
    game()
