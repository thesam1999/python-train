value = "y"  # 也可以改成True，結果都是代表True
count = 0
while value:
    count += 1
    print(count)
    if count == 5:
        break
    else:
        value = 0  # 也可以改成False
        continue  # 還是會把value回傳到while只是回傳值是False因此停止回圈
