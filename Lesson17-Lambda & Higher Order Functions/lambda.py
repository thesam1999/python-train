
from functools import reduce
def squared(num): return num * num
# lambda叫匿名函數，輸入lambda num : num * num，會自動轉換成上面的function


print(squared(2))


def add_two(num): return num + 2
# lambda num : num + 2


print(add_two(12))


def sum_total(a, b): return a + b
# lambda a, b : a + b


print(sum_total(10, 8))

#######################
# high order function是可以接收函數作為參數或返回一個函數作為結果的函數
# 閉包本身不是高階函數，但高階函數可以返回閉包，這樣可以結合這兩個概念來創建靈活和強大的程式碼結構。
# parent function就是一個高階函數

# lambda通常用在另一個函數中使用


def funcBuilder(x):
    return lambda num: num + x
# 類似閉包，我們想要晚一點再來使用這個方程式


add_ten = funcBuilder(10)  # 這裡是傳遞10這個值給x
add_twenty = funcBuilder(20)
# 因為funcBuilder(10)會回傳lambda這個函數
# 因此add_ten可以看成lambda num: num + 10
print(add_ten(7))
print(add_twenty(7))

########################
# map()、filter()、reduce()都是高階函數

numbers = [3, 7, 12, 18, 20, 21]

# 第一個參數是要接受函數，第二個參數接收一個資料集合EX:List、tuple、dict、set、Pandas DataFrame
squared_nums = map(lambda num: num * num, numbers)
# 會迭代(interate)該data collection的每個元素
# 結果要選擇你要輸出的資料類型 EX: List()、tuple()...
print(list(squared_nums))

###############################

odd_nums = filter(lambda num: num % 2 != 0, numbers)
# % modulus operator 是返回餘數，上面函數是確認返回值是奇數的話會顯示True
# filter只回傳是True的元素
print(list(odd_nums))

#############################


numbers = [1, 2, 3, 4, 5, 1]

total = reduce(lambda acc, curr: acc + curr, numbers, 10)  # 第三個參數是選定起始值
# reduce把第一個元素跟第二個元素相加得到的結果變成acc，繼續相加第3個元素
print(total)

print(sum(numbers, 10))


names = ['Dave Gray', 'Sara Ito', 'John Jacob Jingleheimerschmidt']

char_count = reduce(lambda acc, curr: acc + len(curr), names, 0)
# 第三個參數要加0，否則第一個acc會是字串，這樣會顯示錯誤，
print(char_count)
