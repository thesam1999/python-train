# customer error
class JustNotCoolError(Exception):  # 繼承Exception類
    pass
# 這樣自定義了一種ERROR
# exception也是一種類


x = 2
try:  # 執行try裡的程式碼，except是如果執行程式碼時發生異常要怎麼辦
    # raise在特定的情況下主動形成錯誤，()裡是傳遞發生錯誤時的訊息
    raise JustNotCoolError("This just isn't cool, man.")
    # raise Exception("I'm a custom exception!")
    # print(x / 0)
    # if not type(x) is str:
    #     raise TypeError("Only strings are allowed.")

# 用except這個方法可以在try裡的程式碼發生錯誤時，執行except裡的程式，而不會讓系統崩潰
except NameError:  # except裡面也可以指定在什麼異常的情況下
    print('NameError means something is probably undefined.')
except ZeroDivisionError:
    print('Please do not divide by zero.')
except Exception as error:  # 只捕獲從 Exception 類別繼承的異常。這意味著它不會捕獲像 SystemExit、KeyboardInterrupt 或 GeneratorExit 這些並非從 Exception 派生的異常
    print(error)  # 如果只有except會会捕获所有的异常，包括所有类型的内置异常和系统退出信号，这种做法非常宽泛，甚至会捕获像 SystemExit 和 KeyboardInterrupt 这样的系统级异常，导致一些重要的信号被静默处理。没有错误信息：没有 as 语法时，你无法获取或打印异常的具体信息，因此调试时可能很难追踪到错误的来源。

else:  # 如果沒有error會執行的程式
    print('No errors!')
finally:  # 不論有沒有發生Error都執行
    print("I'm going to print with or without an error.")
