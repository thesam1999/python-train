
name = "Dave"  # Global scope 全域範圍
count = 1


# def greeting(firstname):  # 如果greeting(name) 就不會print Dave

#     color = "blue"
#     print(color)
#     print(name)
#     print(firstname)


# print(color) #會顯示錯誤，因為color是local scope（區域範圍）的變數
# greeting("John")  # greeting被視為全域範圍，但裡面color被視為local scope


# def another():
#     greeting("Dave")


# another()

def another():
    color = "blue"
    global count
    count += 1  # 前面要加上 global count才能修改；一般在function不能修改全域變數，只能替代如 count = 2就可以

    print(count)

    def greeting(name):  # 這叫nested function，也可以把greeting()這個函數放到全域範圍，但有可能造成polluting the global scope(汙染全域)，所以盡可能這樣放
        nonlocal color  # 代表可以修改parent function裡的變數
        color = "red"
        print(color)
        print(name)

    greeting("Dave")


another()
