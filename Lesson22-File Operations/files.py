import os  # 用於與操作系統進行交互，可以處理文件、目錄、環境變量
# 如創建、刪除文件和目錄，獲取當前工作目錄，或者執行系統命令。
# r = Read 讀取模式開啟檔案。檔案必須已經存在，否則會引發錯誤。
# a = Append 以追加模式開啟檔案。如果檔案不存在，會自動創建檔案。新的資料會被寫入到檔案的末尾，不會覆蓋原有內容。
# w = Write 以寫入模式開啟檔案。如果檔案存在，會清空其內容並重新寫入。如果檔案不存在，會自動創建檔案。
# x = Create 創建模式開啟檔案。如果檔案已存在，則引發錯誤。這個模式用於確保只在檔案不存在的情況下創建檔案。

# Read - error if it doesn't exist

# open("names.txt","r")是預設的，有打跟沒打都可以，只是預設以讀取模式開啟，還沒有開始讀取檔案內容。
f = open("names.txt")
# print(f.read()) # open() 是用來打開檔案的，但它本身並不執行任何讀取或寫入操作。當你打開檔案時，它只建立了一個檔案物件並將其指派給變數f，此時還沒有讀取檔案的內容。
# print(f.read(4)) #會嘗試從當前指標位置（因為前面有print(f.read())，因此現在檔案位置在末尾）開始讀取4個字元

# print(f.readline()) #讀取第一行
# print(f.readline()) # 現在位置在第二行，因此讀取第二行

# 用print(f)結果不會顯示檔案的內容，而是顯示檔案物件的資訊。因為open() 函數只是打開檔案，並返回一個檔案物件。這個物件是 Python 用來處理檔案的東西，它包含了檔案的路徑、模式（讀取、寫入等）以及檔案的一些其他屬性。它不會自動讀取檔案的內容。


for line in f:  # 用 for line in f: 時，Python 自動將檔案物件 f 視為一個可迭代物件。當你迭代它時，Python 將檔案逐行讀取，並將該行賦值給 line。這種行為是檔案物件的一個特殊特性。
    print(line)

f.close()  # 每次結束記得關閉檔案，否則會不小心在後續修改到檔案

try:
    f = open("names.txt")
    print(f.read())
except:
    print("The file you want to read doesn't exist")
finally:
    f.close()

# Append - creates the file if it doesn't exist
f = open("names.txt", "a")  # 果檔案不存在會創建一個
f.write("Neil\n")  # 每次執行會在檔案的末尾追加內容
f.close()

f = open("names.txt")
print(f.read())
f.close()

# Write (overwrite)
f = open("context.txt", "w")
f.write("I deleted all of the context")  # 把檔案內容全部覆蓋
f.close()

f = open("context.txt")
print(f.read())
f.close()

# Two ways to create a new file

# Opens a file for writing, creates the file if it does not exist
f = open("name_list.txt", "w")
f.close()

# Creates the specified file, but returns an error if the file exists，避免的方法如下
if not os.path.exists("dave.txt"):  # 檢查檔案名稱叫"dave.txt"是否存在，
    f = open("dave.txt", "x")  # 如果不存在則創建該檔案，這樣就部會顯示錯誤
    f.close()

# Delete a file

# avoid an error if it doesn't exist
if os.path.exists("dave.txt"):
    os.remove("dave.txt")  # 如果dave.txt檔案存在的話，則移除這個檔案
else:
    print("The file you wish to delete does not exist")


# with has built-in implicit exception handling
# close() will be automatically called

# with是一個上下文管理器（Context Manager）的語句，Python 自動處理文件的打開和關閉。即使發生異常，with 也會自動關閉文件，這樣不需要顧慮資源洩漏。
# __enter__: 在進入 with 區塊之前執行，通常用來初始化或分配資源。__exit__: 在離開 with 區塊時自動執行，用來清理或釋放資源。
with open("more_names.txt") as f:
    content = f.read()

with open("names.txt", "w") as f:
    f.write(content)
# 把names.txt得檔案內容變成more_names的檔案內容
