# recursion代表遞歸

def add_one(num):
    if num >= 9:
        return num + 1  # 在function裡會傳遞返回值，並立即停止函數的執行
    total = num + 1
    print(total)

    # 如果移除這裡的return，add_one(total)只是調用add_one 函数，不會有返回值最后，mynewtotal 将是 None，因为函数没有返回值，print(mynewtotal) 将输出
    return add_one(total)


mynewtotal = add_one(0)
print(mynewtotal)
