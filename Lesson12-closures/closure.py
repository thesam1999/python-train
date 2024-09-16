# Closure is a function having access to the scope of its parent
# function after the parent function has returned.

def parent_funcction(person, coins):
    coins = 3

    def play_game():
        nonlocal coins  # 要有這個代表可以改變 parents function的 coins，再加上 return就可以形成 closure
        coins -= 1

        if coins > 1:
            print("\n" + person + " has " + str(coins) + "coins left.")
        elif coins == 1:
            print("\n" + person + " has " + str(coins) + " coin left.")
        else:
            print("\n" + person + " is out of coins.")

    return play_game  # 不能加()，因為這代表是回傳 play_game這個函數本身，不是立刻執行，而是稍後在執行
    # 使用return play_game為了讓外部可以調用和修改coins跟person

# 閉包的組成條件：
# 必須有嵌套的函數，即一個函數在另一個函數內部定義。
# 內部函數必須引用外部函數的變數。
# 外部函數返回這個內部函數，讓它在外部調用。


# 這樣可以創建一個閉包，讓tommy這個函數可以記住person為"Tommy"時coins的變量
# 用tommy這個變數去接住， parent_funcction最後回傳未執行play_game函數
tommy = parent_funcction("Tommy", 3)
jenny = parent_funcction("Jenny", 5)  # 因此可以把tommy這個變數看成是play_game這個函數
# 因此tommy()看成play_game()
tommy
tommy()
tommy()

jenny()

tommy()
