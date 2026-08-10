#註解
"""
這是多行註解
"""

# 這是單行註解
from xmlrpc.client import boolean


print("Hello, World!")  # print是在終端機顯示文字的指令
# ctrl + ? 可以快速註解或取消註解


# 基本型態
print(1)        # float 這是整數, -1, 0, 1, 2, 3, 4
print(1.0)      # float 這是浮點數
print(1.234)    # float 這是浮點數
print("apple")  # str 這是字串 "abc123"
print(True)     # bool 這是布林值 True/False
print(False)    # bool 這是布林值 True/False


#變數
a = 10      #  新增一個儲存空間並取名為a, "="的功能是將右邊數字10存入左邊的a
print(a)    #  在終端機顯示a所存的值
a = "apple" #  將a的值改為""apple"
print(a)    #  在終端機顯示a所存的值


# 運算子
print(1 + 1)      #  加法
print(1 - 1)      #  減法
print(1 * 1)      #  乘法
print(1 / 1)      #  除法
print(1 // 1)     #  取商
print(1 % 1)      #  取餘數
print(1 ** 1)     #  次方


#優先順序
# 1. ()          括號
# 2. **          次方
# 3. *, /, //, % 乘 除 取商 取餘數
# 4. +, -        加 減


#字串運算,+、*
print("apple" + "pen") # 字串相加
print("apple" * 3)     # 字串乘法


#字串格式化
name = "Evan"
age = 12
print(f"Hello, my name is {name} and I am {age} years old.  ")  #  f-string 
#可以將變數或其他型態的資料放到f字串裡面的{}，這樣就可以在字串中顯示   


#更多功能
print(len("apple"))    # len()是ㄧ個函式，可以計算字串的長度
print(len("，"))       # len()是ㄧ個函式，可以計算字串的長度
# type()               # type()可以查看資料的型態
print(type(1))         # <class 'int'>
print(type(1.0))       # <class 'float'>
print(type("apple"))   # <class 'str'>
print(type(True))      # <class 'bool'>


# 型態轉換
print(int(1.0))        # float轉int
print(float(1))        # int轉float
print(str(1))          # int轉str
print(bool(1))         # int轉bool
print(int(1.234))      # float轉int
print(float("1.234"))  # str轉float
print(str(1.234))      # float轉str
print(bool(1.234))     # float轉bool
# print(int("hello"))  # 這行會報錯，因為字串裡面如果有非數字的字元，無法轉換成數字
print(bool(0))      # 這行會顯示 False
print(bool(2**3))     # 這行會顯示 False
print(bool(1))      # 這行會顯示 True


print("輸入開始")
# input()是ㄧ個函式，可以讓使用者輸入文字
#  ()裡面的文字試提示訊息會先顯示在終端機才會等待使用者輸入
a = input("請輸入一些文字: ")  
print("輸入結束")
print(int(a) + 10) 
print(type(a))         # 證明透過input()輸入內容都是字串

#練習題
r = input("請輸入圓的半徑: ")
面積 = 3.14 * float(r) ** 2
print(f"圓的面積是 {面積}")