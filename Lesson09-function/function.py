def hello_world():  # 命名函數要全部小寫，分隔單字用underscore
    print("Hello World!")


hello_world()


# def sum(num1, num2):
#     print(num1+num2)

# sum(2,3)
# sum(1,7)
# sum(100,3)


def sum(num1=0, num2=0):  # 都先假設成0 這樣即使沒有入數字也不會顯示錯誤
    if (type(num1) is not int or type(num2) is not int):
        return 0
    return num1 + num2  # return 相較 print可以返回該值，並用在其他程式上


total = sum(7, 2)
print(total)


def multiple_items(*args):  # 不知道會塞入多少參數，用* 不一定要arg(argument縮寫，但這個位置要稱作parameters)
    print(args)
    print(type(args))


multiple_items("Dave", "John", "Sara")


def mult_named_items(**kwargs):  # keyword argument，用兩個*代表命名多個參數
    print(kwargs)
    print(type(kwargs))


mult_named_items(first="Dave", last="Gray")
