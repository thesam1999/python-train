

from math import pi  # import math
import sys
import random as rdm
from enum import Enum
import kansas
from rps7 import rock_paper_scissors

print(pi)  # print(math.pi)
# rdm.choice("123")

# for item in dir(rdm):
#     print(item)  # :dir (directory)目錄的縮寫，可以顯示module 所有內容

# # 詳細的module介紹 看這裡
# # https://docs.python.org/3/py-modindex.html

print(kansas.capital)
kansas.randomfunfact()

print(__name__)  # 結果是main代表 這是我們現在運行的文件
print(kansas.__name__)

rock_paper_scissors()
