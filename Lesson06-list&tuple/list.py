users = ['Dave', 'John', 'Sara']

data = ['Dave', 42, True]

emptylist = []


print("Dave" in users)  # 某字串是否在某便數裡，回傳boolean
print("Dave" in data)
print("Dave" in emptylist)

print(users[0])
print(users[-1])
print(users[-2])

print(users.index('Sara'))

print(users[0:2])  # 最後一個屬性不會顯示
print(users[1:])
print(users[-3:-1])

print(len(data))

users.append('Elsa')  # 在users最後加上Elsa
print(users)

users += ['Jason']  # 要記得加brackets，否則會變成加上'J','a','s','o','n'
print(users)

users.extend(['Rober', 'Jimmy'])  # 可以新增一個List到users裡
print(users)

# users.extend(data)
# print(users)

users.insert(0, 'Bob')  # insert插入list裡面，插入BOB到第一個位置(0,Bob)
print(users)

users[2:2] = ['Eddie', 'Alex']  # bracket notation括號表示法 [2:2]代表在第三個位置插入你要的值
print(users)

users[1:3] = ['Robert', 'JPJ']  # slice代表取代list第一個到第二個位置，第三個位置並沒有被取代
print(users)

users.remove('Bob')  # 移除list裡的 Bob
print(users)

print(users.pop())  # 移除最後一個value，並回傳最後一個值
print(users)

del users[0]
print(users)

# del data (代表把data這個變數刪掉)
# print(data)

data.clear()  # 清除 data這個list裡的value
print(data)

users[1:2] = ['dave']
users.sort()  # 依照字母順序排列(先大寫排序在小寫)
print(users)

users.sort(key=str.lower)  # 不分大小寫，僅依照字母順序排列(str.lower)代表所有資料類型皆為字串才能這樣用
print(users)

nums = [4, 42, 78, 1, 5]
nums.reverse()
print(nums)

# nums.sort(reverse=True)  # reverse=True 代表由大到小排列
# print(nums)

print(sorted(nums, reverse=True))  # sorted是返回一個新的排序後的列表，而不改變原來的 nums 列表
print(nums)

numscopy = nums.copy()  # 這三種方法都是創一個新變數，並複製nums這個list，以保留nums這個list裡的值不變
mynums = list(nums)
mycopy = nums[:]

print(numscopy)
print(mynums)
mycopy.sort()
print(mycopy)
print(nums)


print(type(nums))

mylist = list([1, "Neil", True])
print(mylist)

# Tuples  跟List很像，差別在於turple一旦創建後就不可以更改

mytuple = tuple(('Dave', 42, True))

anothertuple = (1, 4, 2, 8, 2, 2)

print(mytuple)
print(type(mytuple))
print(type(anothertuple))


newlist = list(mytuple)  # 把tuple包裝成list，並給這個list新變數，這樣就可以增加、減少、刪除list裡面的值
newlist.append('Neil')
newtuple = tuple(newlist)
print(newtuple)

# 元組解包(unpacking tuple) One會取得元祖中的第一個元素，即1，最後*hey是使用了擴展解包語法，表示hey會取得元祖中剩下的所有元素
(one, two, *hey) = anothertuple
print(one)
print(two)
print(hey)

(one, *two, hey) = anothertuple
print(one)
print(two)
print(hey)  # 取得最後一個元素，其他中間元素會分給two

print(anothertuple.count(2))  # 計算2在tuple出現幾次
