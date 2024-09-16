
import sys
import random
from enum import Enum  # Enum代表Enumeration列舉，通常Enum用來定義一個列舉類別，每個成員都有一個名稱和一個值,ex:星期幾、顏色、方向


class RPS(Enum):
    ROCK = 1  # 因為命名這些變數都不會改變，所以全用大寫
    PAPER = 2
    SCISSORS = 3


print(RPS(2))  # !!數值要用括號，不能用.
print(RPS.ROCK)
print(RPS['ROCK'])
print(RPS.ROCK.value)

# sys.exit()


print("")

playerchoice = input(
    # CTRL+Z 可以把過長的程式碼換行，方便閱讀，但不影響程式碼
    "Enter...\n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n")
# input是一個函數，會顯上括號裡的內容，將使用者輸入的內容當作字串回傳playerchoice

player = int(playerchoice)  # 在if裡不能用字串跟數字比大小，所以這裡把回傳字串，改成整數值(integer)

if player < 1 or player > 3:  # |代表或的意思
    sys.exit("You must enter 1, 2 or 3.")  # sys.exit 代表停止執行程式，並向使用者顯示 ()裡面的訊息

computerchoice = random.choice("123")  # 隨機以字串的形式回傳1~3的數字，

computer = int(computerchoice)

print("")
print("You choice " + str(RPS(player)).replace('RPS.', ' ') + ".")
print("Python choice " + str(RPS(computer)).replace('RPS.', ' ') + ".")

print("")

if player == 1 and computer == 3:
    print("🎉You win!")
elif player == 2 and computer == 1:
    print("🎉You win!")
elif player == 3 and computer == 2:
    print("🎉You win!")
elif player == computer:
    print("😮Tie game!")
else:
    print("🐍Python wins!")
