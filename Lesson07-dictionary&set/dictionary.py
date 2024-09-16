# Dictionaries
band = {
    "vocals": "Plant",
    "guitar": "Page"
}

band2 = dict(vocals="Plant", guitar="Page")

print(band)
print(band2)
print(type(band))
print(len(band2))

# Access items
print(band["vocals"])  # 呼叫字典要這樣用
print(band.get("guitar"))

# list all keys
print(band.keys())  # 顯示所有關鍵字

# list all value
print(band.values())  # 顯示所有值

# list of key/value pairs as tuples 以tuple的形式顯示
print(band.items())

# verify a key exists
print("guitar" in band)
print("triangle" in band)

# Change values
band["vocals"] = "converdale"
band.update({"bass": "JPJ"})  # 也可以用vocal或是 guitar替代，或是創新的key跟value
print(band)

# Remove items
print(band.pop("bass"))  # pop會回傳移除的值
print(band)

band["drums"] = "Bonham"
print(band)

print(band.popitem())
print(band)

# Delete and clear

band["drums"] = "Bonham"
del band["drums"]
print(band)

band2.clear()
print(band2)

del band2

# Copy dictionaries

# 不好的複製
# band2 = band  # create a reference 不是複製，因為只要這樣寫只要band2改變 band也會一起改變
# print("Bad Copy!")
# print(band2)
# print(band)

# band2["drums"] = "Dave"
# print(band)

band2 = band.copy()
band2["drums"] = "Dave"
print("Good copy!")
print(band)
print(band2)

# or use the dict() constructor function
band3 = dict(band)
print("Good copy!")
print(band3)

# Nested dictionaries 嵌套字典

member1 = {
    "name": "Plant",
    "instrument": "vocals"
}
member2 = {
    "name": "Page",
    "instrument": "guitar"
}
band = {
    "member1": member1,
    "member2": member2
}
print(band)  # 在一在一個字典裡嵌入兩個字典
# 要在member1這個辭典裡找name，第一個bracket代表第一層，第二個bravket代表第二層
print(band["member1"]["name"])

# Sets 集合

nums = {1, 2, 3, 4}

nums2 = set((1, 2, 3, 4))

print(nums)
print(nums2)
print(type(nums))
print(len(nums))

# No duplicate allowed  集合裡不允許重複
nums = {1, 2, 2, 3}  # 重複數字會被忽略
print(nums)

# True is a dupe(duplicate縮寫) of 1, False is a dupe of zero
nums = {1, True, 2, False, 3, 4, 0, }
print(nums)  # set會自動排序，且因為False在前面因此會顯示False忽略後面0

# check if a value is in a set
print(2 in nums)

# but you cannot refer to an element in the set with an index position or a key
# 可以在集合裡確定有沒有一個值，但不能(像list)問第1個位置或是地2個位置的值是什麼

# Add a new element to a set
nums.add(8)
print(nums)

# Add elements from one set to another
morenums = {5, 6, 7}
nums.update(morenums)  # 把morenums替換成一個list或是tuple或是dictionary都可以
print(nums)
morenums = {5, 6, 7}

# you can use update with lists, tuples, and dictionaries, too.

# Merge two sets to create a new set
one = {1, 2, 3}
two = {5, 6, 7}

mynewset = one.union(two)  # union結合兩種不同集合
print(mynewset)

# Keep only the duplicates
one = {1, 2, 3}
two = {2, 3, 4}

one.intersection_update(two)
print(one)  # 把one集合改成 one跟two都重複的集合

# Keep everything except the duplicates
one = {1, 2, 3}
two = {2, 3, 4}
one.symmetric_difference_update(two)
print(one)
