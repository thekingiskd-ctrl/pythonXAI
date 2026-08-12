print([])                           # 這是一個空的list 
print([1, 2, 3])                    # 這是一個有3個元素的list
print([1, 2, 3, "a", "b", "c"])     # 這是一個有6個元素的list 
print([1, 2, 3, ["a", "b", "c"]])   # 這是一個有4個元素的list
print([1, True, "a", 1.23])         # 這是一個有4個元素的list套

# list 讀取元素，元素的index從0開始
L = [1, 2, 3, "a", "b", "c"]
print([])  # 1
print([])  # 2 
print([])  # 3
print([])  # "a"

L = [1, 2, 3, "a", "b", "c"]
# 就是取index 0到最後，每次取2個元素，所以是[1, 3, 'b']
print(L[::2])
# 就是取index 1到3的元素，不包含index 4，所以是[2, 3, 'a']
print(L[1:4])
# 就是取index 1到3的元素，不包含index 4，每次取2個元素，所以是[2, 'a']
print(L[1:4:2])
# 跟range一樣的用法，只是符號不同

# list 取長度，也就是list中有幾個元素，不是index的最大值
L = [1, 2, 3, "a", "b", "c" ]
print(len(L))   # 6

# list走訪元素
# 可以透過取得index的方式來找list中的資料
# 也可以直接把list當做一個范圍來取得資料
# 這兩種方式都可以，但是看使用的情況是否會需要index決定要用哪一種方式
L = [1, 2, 3, "a", "b","c"]
for i in range(0, len(L), 2):
    print(L[i])

for i in L:
    print(i)

# call by value
a = 1
b = a  # 複製a的值給b
b = 2
print(a, b)

# call by reference
a = [1, 2, 3]
b = a  # 把a跟b指向同一個記憶體位置，所以改變b的值，a也會跟著改變
b[0] = 2
print(a, b)

a = [1, 2, 3]
b = a.copy()  # 複製a的值給b，但是b跟a指向不同的記憶體位置
b[0] = 2
print(a, b)

# list的append
L = [1, 2, 3]
L.append(4)   #把4加到L的最後面
print(L)

# list移除元素方式有兩種
# 1. 使用remove，可以移除指定的元素
L = ["a", "b", "c", "d", "a"]
L.remove("a")   #移除第一個a 
# 代表remove會從頭開始找，找到第一個符合的元素就會移除
# 2. 使用pop，可以移除指定的index的元素
L = ["a", "b", "c", "d", "a"]
L.pop(0)   # 移除index 0的元素
# 代表pop會移除指定的index的元素
# 如果不指定index， 則會移除最後一個元素
# L.pop()   # 移除最後一個元素


# sort：將 List 中的元素進行排序，預設是由小到大（升序排列）
# 注意：這個方法會直接修改原本的 List，不會產生新的 List
L = [1, 3, 2, 4, 5]
L.sort()
print(L)
