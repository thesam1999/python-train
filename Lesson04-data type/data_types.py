# String data type

# literal assigment
import math
first = "Dave"
last = "Gray"

# print(type(first))  # type函數 確認first是字串值
# print(type(first) == str)
# print(isinstance(first, str))  # 檢查first是否為 str類型會返回True or False

# constructure function
# pizza = (str("Pepperoni")) # 簡單的寫 pizza = Pepperoni
# print(type(pizza))  # 選擇pizza 按ctrl+d 連按可以選擇之後的pizza 選完後輸入cake選中的pizza都變cake

# print(type(pizza) == str)
# print(isinstance(pizza, str))  # 檢查first是否為 str類型會返回True or False

# concatenation 把兩個字串合併成一個大字串
fullname = first + " " + last
print(fullname)

fullname += "!"
print(fullname)

# Casting a number to a string把數字轉換成字串
decade = str(1980)
print(type(decade))
print(decade)

statement = "I like rock music from the " + decade + "s."
print(statement)

# Multiple lines 讓字串可以分行顯示用三個引號
multiline = '''
Hey, how are you?

I was just checking in.
                            All good?
'''
print(multiline)

# Escaping special characters跳脫字元  \' 讓'變成字串  \t縮排  \n換行 \\就是顯示\
sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at\\located?'
print(sentence)


# String Menthods

print(first)
print(first.lower())  # 全部變小寫
print(first.upper())  # 全部變大寫
print(first)

print(multiline.title())  # 把每個字串的開頭變大寫
print(multiline.replace("good", "ok"))  # 把Good換成OK
print(multiline)

print(len(multiline))  # len 顯示muliline 的長度，每個字串都會算到，包含空白鍵

multiline += "                                       "
multiline = "           " + multiline
print(len(multiline))


print(len(multiline.strip()))  # 刪除 multiline的空格
print(len(multiline.lstrip()))  # 刪除 multiline的最左邊的空格
print(len(multiline.rstrip()))  # 刪除 multiline的最右邊空格

print(" ")

# Build a menu
title = "menu".upper()
print(title.center(20, "="))  # 創造20個字串，把title放中間其他16個字串用 = 填滿

# ljust 靠左對齊 包含coffee有16個字串 空白用.填滿，$1靠右對齊共4個字串空白保持空白
print("Coffee".ljust(16, ".") + "$1".rjust(4))
print("Muffin".ljust(16, ".") + "$2".rjust(4))
print("Cheesecake".ljust(16, ".") + "$4".rjust(4))

print("")

# string index values
print(first[1])  # start 0 開始，所以1是第2個字
print(first[-1])  # 顯示字串的最後一個字
print(first[1:-1])  # 顯示第二個字串到最後一個字串之間的內容(但不包含最後一個)
print(first[1:])  # 從第二個字串到最後

# Some methods return boolean data
print(first.startswith("D"))
print(first.endswith("Z"))


# # Boolean data type
myvalue = True
x = bool(False)  # 把X變成boolean的 False
print(type(x))
print(isinstance(myvalue, bool))

# Numeric data types

# integer type
price = 100
best_price = int(80)  # int 整數類型的意思
print(best_price)
print(type(price))
print(isinstance(best_price, int))

# # float type
gpa = 3.28
y = float(1.14)
print(type(gpa))

# complex type
comp_value = 5+3j
print(type(comp_value))
print(comp_value.real)  # 顯示實數值
print(comp_value.imag)  # 顯示虛數值

# # Built-in functions for numbers

print(abs(gpa))  # gpa的絕對值

print(abs(gpa * -1))

print(round(gpa))  # 四捨五入取整數

print(round(gpa, 1))  # 四捨五入取到小數點後1位


print(math.pi)
print(math.sqrt(64))  # 開根號
print(math.ceil(gpa))  # 數字無條件進位
print(math.floor(gpa))  # 無條件捨去

# Casting a string to a number
zipcode = "10001"
zip_value = int(zipcode)
print(type(zip_value))

# Error if you attempt to cast incorrect data
# zip_value = int("New York")
