person = "Dave"
coins = 3

print("\n" + person + " has " + str(coins) + " coins left.")

message = "\n%s has %s coins left." % (
    person, coins)  # person這個變數插入第一個%s，coins插入第二個$s
print(message)

# 下面是format的方法

message = "\n{} has {} coins left.".format(
    person, coins)
print(message)

message = "\n{1} has {0} coins left.".format(coins, person)
print(message)

message = "\n{person} has {coins} coins left.".format(
    coins=coins, person=person)  # 把 curly bracket裡的參數，等於我要求的變數
print(message)

player = {'person': 'Dave', 'coins': 3}

message = "\n{person} has {coins} coins left.".format(
    **player)
print(message)

################
# f-Strings! This is the way.
# 下面是f-string 格式化字符串

message = f"\n{person} has {coins} coins left."
print(message)

message = f"\n{person} has {2*5} coins left."
print(message)

message = f"\n{person.lower()} has {2*5} coins left."
print(message)  # 可以在 curly bracket做任何事，不只是傳遞值


# 外面要用double quote 裡面要用single quote ，如果外面用single quote會顯示錯誤
message = f"\n{player['person']} has {2*5} coins left."
print(message)

#################
# You can pass formatting option.

num = 10
# 想要結果有一個固定格式在最後放: .2代表小數點兩位f代表 fix固定位置
print(f"\n2.25 time{num} is {2.25*num:.2f}\n")

for num in range(1, 11):
    print(f"2.25 time{num} is {2.25*num:.2f}")

for num in range(1, 11):
    print(f"{num} divided by4.52 is {num/4.52:.2%}")  # %代表百分比

# 更多相關用法可以到w3 school去看
# https://www.w3schools.com/python/ref_string_format.asp
