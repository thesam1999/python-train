value = 1
# while value <= 10:
#     print(value)  # 要讓value在某個時刻會大於10否則會無限迴圈
#     if value == 5:
#         break #讓迴圈停止
#     value += 1

# while value <= 10:
#     value += 1  # 起始值是2，因為先加1才有print
#     if value == 5:  # 不會有5，因為一達到5會跳過剩餘迴圈，重新開始，就不會接觸到print
#         continue
#     print(value)
# else:  # 沒有縮排因為是在while迴圈結束時，才會執行，else不會在迴圈裡一起執行
#     # else只有在while迴圈案其應有的方式完成，else才會執行，如果中有有break那就不會執行else

#     print("Value is now equal to " + str(value))

names = ["Dave", "Sara", "John"]
# for x in names:
#     print(x)

# for x in "Mississippi":
#     print(x)

# for x in names:
#     if x == "Sara":
#         break
#     print(x)

# for x in names:
#     if x == "Sara":
#         continue  # continue時，會重新跑迴圈，故不會經過print，跳過print(Sara)
#     print(x)

# for x in range(4): #從0揩使到4時，會停止，迴圈不會往下跑
#     print(x)

# for x in range(2, 4): #從2開始，到4時會停下來不會往下跑
#     print(x)

# for x in range(5, 101, 5):  # 從5開始到101停止，被次迴圈會增加5
#     print(x)
# else:
#     print("Glad that\'s over!")

# 嵌套循環
names = ["Dave", "Sara", "John"]
actions = ["codes", "eats", "sleeps"]

for name in names:  # 外部迴圈跑第一次時，會跑完內部迴圈，再跑外部迴圈第二次
    for action in actions:
        print(name + " " + action)

for action in actions:
    for name in names:
        print(name + " " + action + ".")
