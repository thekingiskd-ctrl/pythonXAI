# 🐍 Python 課堂筆記整理：Streamlit、迴圈、隨機數與字典

這份筆記把你今天學到的內容整理成**國中生也容易理解的版本**。可以把它想成一本「Python 小工具箱」：遇到不同問題，就拿出不同工具來使用。

---

## 一、📐 Streamlit 的 Columns 欄位

### 1. `st.columns()` 是做什麼的？

`st.columns()` 可以把網頁畫面切成好幾個欄位。

想像你的書桌：

```text
┌───────────────┬───────────────┐
│     col1      │     col2      │
│               │               │
└───────────────┴───────────────┘
```

最基本的寫法：

```python
col1, col2 = st.columns(2)
```

代表把畫面平均分成 **2 欄**。

---

### 2. 在不同欄位放東西

```python
col1.button("按鈕1")
col2.button("按鈕2")
```

就可以讓兩個按鈕分別出現在不同欄位。

也可以使用 `with`：

```python
with col1:
    st.button("按鈕1")
    st.write("這是第一欄")

with col2:
    st.button("按鈕2")
    st.write("這是第二欄")
```

### ⭐ `with` 可以想成：

> 「接下來的東西，都放進這個欄位裡。」

---

## 二、📏 Columns 可以設定寬度比例

不一定每一欄都要一樣寬。

```python
col1, col2 = st.columns([1, 2])
```

意思是：

```text
┌────────┬────────────────┐
│ col1   │      col2      │
│  1份   │       2份      │
└────────┴────────────────┘
```

所以：

* `1 : 1` → 一樣寬
* `1 : 2` → 第二欄是第一欄的 2 倍
* `1 : 2 : 3` → 三欄依照 1、2、3 的比例分配

例如：

```python
col1, col2, col3 = st.columns([1, 2, 3])
```

---

# 三、🔁 用 `for` 迴圈建立很多 Columns

如果要建立很多欄位，不需要一直寫：

```python
col1
col2
col3
col4
```

可以使用：

```python
cols = st.columns(4)

for i in range(len(cols)):
    with cols[i]:
        st.button(f"按鈕{i+1}", key=f"btn{i+10}")
```

### 這裡有幾個重要觀念：

`len(cols)`：

> 計算 `cols` 裡面有幾個欄位。

如果：

```python
cols = st.columns(4)
```

那麼：

```text
cols[0]
cols[1]
cols[2]
cols[3]
```

就是 4 個欄位。

⚠️ Python 的編號通常從 **0 開始**。

---

# 四、🔑 `key` 是什麼？

在 Streamlit 中，如果頁面上有很多相同的按鈕，最好幫每個元件設定不同的 `key`。

例如：

```python
st.button("按鈕1", key="btn1")
st.button("按鈕2", key="btn2")
```

可以把 `key` 想成：

> 🪪 元件的「身分證字號」。

每個元件最好都有不同的 `key`，這樣 Streamlit 才知道你按的是哪一個。

---

# 五、⌨️ `st.text_input()` 文字輸入框

如果希望使用者輸入文字，可以使用：

```python
text = st.text_input("請輸入文字")
```

例如：

```python
text = st.text_input("請輸入文字", value="這是預設文字")
st.write(f"你輸入的文字是{text}")
```

### `value`

`value` 是設定輸入框一開始顯示什麼。

```python
value="這是預設文字"
```

所以使用者一開始會看到：

```text
┌──────────────────────┐
│ 這是預設文字          │
└──────────────────────┘
```

---

# 六、🎈 `st.balloons()`

```python
st.balloons()
```

會在 Streamlit 網頁上出現氣球動畫。

例如：

```python
if st.button("恭喜"):
    st.balloons()
```

意思是：

> 如果使用者按下「恭喜」，就放氣球！

---

# 七、💾 `st.session_state`

這是今天非常重要的一個觀念。

Streamlit 的程式在互動時，可能會重新執行。

如果單純使用普通變數：

```python
ans = 1
```

重新執行程式後，`ans` 可能又回到 `1`。

這時可以使用：

```python
st.session_state
```

它可以想成：

> 🧠 Streamlit 的「記憶本」。

---

## 1. 建立記憶中的變數

```python
if "ans1" not in st.session_state:
    st.session_state.ans1 = 1
```

意思是：

> 如果記憶本裡還沒有 `ans1`，就建立它，並設定為 1。

---

## 2. 修改記憶中的數字

```python
if st.button("按下去ans加1"):
    st.session_state.ans1 += 1
```

每按一次：

```text
1 → 2 → 3 → 4 → 5 ...
```

然後：

```python
st.write(st.session_state.ans1)
```

就可以顯示目前的數字。

---

# 八、🔄 `st.rerun()`

```python
st.rerun()
```

意思是：

> 🔄 要 Streamlit 立刻重新執行一次程式。

例如：

```python
if st.button("重新整理"):
    st.rerun()
```

可以把它想成按下「重新整理」的按鈕。

---

# 九、🛒 實作：簡單點餐機

你今天的程式其實已經把很多觀念組合在一起了。

例如：

```python
st.session_state.cart = []
```

建立一個購物籃。

這個：

```python
[]
```

是 **List（串列）**，可以拿來存很多餐點。

加入餐點：

```python
st.session_state.cart.append(new_item)
```

`append()` 的意思是：

> ➕ 把新東西加到 List 的最後面。

例如：

```text
購物籃：

[]
↓
["漢堡"]
↓
["漢堡", "薯條"]
↓
["漢堡", "薯條", "可樂"]
```

---

## 刪除餐點：`pop()`

```python
st.session_state.cart.pop(i)
```

`pop()` 可以刪除指定位置的資料。

例如：

```python
cart = ["漢堡", "薯條", "可樂"]
cart.pop(1)
```

結果：

```python
["漢堡", "可樂"]
```

因為 `1` 是「薯條」的位置。

---

# 十、➕ 算數指定運算子

這些寫法可以讓程式更簡短。

| 寫法        | 等同於          | 意思   |
| --------- | ------------ | ---- |
| `a += 1`  | `a = a + 1`  | 加 1  |
| `a -= 1`  | `a = a - 1`  | 減 1  |
| `a *= 2`  | `a = a * 2`  | 乘 2  |
| `a /= 2`  | `a = a / 2`  | 除以 2 |
| `a //= 2` | `a = a // 2` | 取整數商 |
| `a %= 2`  | `a = a % 2`  | 取餘數  |
| `a **= 2` | `a = a ** 2` | 平方   |

### ⭐ 最常用：

```python
i += 1
```

就是：

```python
i = i + 1
```

在迴圈中非常常見。

---

# 十一、📚 Python 運算子的優先順序

當一行程式裡有很多運算時，Python 會按照優先順序計算。

由高到低：

```text
1. ()
2. **
3. * / // %
4. + -
5. == != > < >= <=
6. not
7. and
8. or
9. = += -= *= /= //= %= **=
```

例如：

```python
2 + 3 * 4
```

不是：

```text
(2 + 3) × 4 = 20
```

而是先乘法：

```text
2 + (3 × 4)
= 14
```

### ⭐ 不確定順序時，直接加括號！

```python
(2 + 3) * 4
```

結果就是：

```text
20
```

---

# 十二、🔁 `while` 迴圈

`while` 的意思可以理解成：

> 「只要條件是真的，就一直做。」

例如：

```python
i = 0

while i < 5:
    print(i)
    i += 1
```

執行結果：

```text
0
1
2
3
4
```

流程：

```text
i = 0
 ↓
i < 5？ → 是 → 印出 i → i + 1
 ↓
i = 1
 ↓
i < 5？ → 是
 ↓
...
 ↓
i = 5
 ↓
i < 5？ → 否
 ↓
結束
```

### ⚠️ 很重要

`while` 裡面要記得讓條件有機會變成 `False`。

例如：

```python
i = 0

while i < 5:
    print(i)
```

這可能會變成**無限迴圈**，因為 `i` 永遠都是 0。

---

# 十三、🛑 `break`

`break` 的意思：

> 🛑 立刻跳出目前的迴圈。

例如：

```python
for i in range(5):
    print(i)

    if i == 3:
        break
```

結果：

```text
0
1
2
3
```

當 `i == 3` 時，遇到：

```python
break
```

就直接離開迴圈。

---

## `while True` + `break`

這是一個很常見的寫法：

```python
while True:
    # 做一些事情

    if 某個條件:
        break
```

意思是：

> 先讓迴圈一直跑，直到符合某個條件，再用 `break` 結束。

---

# 十四、🎲 `random` 隨機數

Python 可以使用 `random` 產生隨機數。

```python
import random as rm
```

意思是：

> 匯入 `random` 模組，並取一個比較短的名字 `rm`。

所以原本：

```python
random.randint()
```

可以寫成：

```python
rm.randint()
```

---

## 1. `randrange()`

```python
rm.randrange(7)
```

會產生：

```text
0～6
```

注意：**7 不包含在內。**

```python
rm.randrange(1, 6)
```

會產生：

```text
1～5
```

---

## 2. `randint()`

```python
rm.randint(1, 6)
```

會產生：

```text
1～6
```

⚠️ 和 `randrange()` 不一樣。

### 記憶方法：

```text
randrange(1, 6)
→ 1～5

randint(1, 6)
→ 1～6
```

---

# 十五、🎯 猜數字遊戲

今天的程式已經可以做出一個簡單的猜數字遊戲。

```python
answer = rm.randint(1, 100)
```

讓電腦偷偷選一個：

```text
1～100
```

的數字。

接著：

```python
while True:
```

讓遊戲一直進行。

如果：

```python
answer > a
```

代表玩家猜太小。

如果：

```python
answer < a
```

代表玩家猜太大。

否則：

```python
else:
    print("答對了")
    break
```

代表猜中了，跳出迴圈。

---

# 十六、🛡️ `try` 和 `except`

如果使用者輸入錯誤資料，程式可能會發生錯誤。

例如：

```python
num = int(input("請輸入數字"))
```

如果使用者輸入：

```text
hello
```

Python 就無法把 `"hello"` 變成整數。

這時可以：

```python
try:
    num = int(input("請輸入數字"))
except:
    print("請輸入數字！")
```

### 可以把它想成：

```text
try
 ↓
「我試著執行這段程式」
 ↓
成功 → 繼續
失敗 → except
```

---

# 十七、⏭️ `continue`

`continue` 的意思：

> 跳過這一次，直接開始下一次迴圈。

例如：

```python
while True:
    try:
        num = int(input("請輸入數字"))
    except:
        print("輸入錯誤")
        continue
```

如果輸入錯誤：

```text
輸入錯誤
↓
continue
↓
重新進入下一次迴圈
```

---

# 十八、📖 Dictionary 字典

Python 的 Dictionary 通常簡稱：

```python
dict
```

它是一種用：

> 🔑 `key` → `value`

來儲存資料的方法。

例如：

```python
d = {
    "a": 1,
    "b": 2,
    "c": 3
}
```

可以想成：

```text
key       value

"a"  →     1
"b"  →     2
"c"  →     3
```

生活中的例子：

```text
學生姓名 → 成績
小明     → 90
小美     → 85
小華     → 95
```

---

# 十九、🔑 Key 和 Value

### Key

`key` 是用來「找到資料」的。

例如：

```python
d["a"]
```

就是找到：

```text
"a" → 1
```

得到：

```text
1
```

### Value

`value` 就是實際存放的資料。

例如：

```python
"a": 1
```

其中：

```text
"a" = key
1   = value
```

---

# 二十、👀 取得 Dictionary 的資料

## `keys()`

取得所有 key：

```python
d.keys()
```

也可以搭配迴圈：

```python
for key in d.keys():
    print(key)
```

---

## `values()`

取得所有 value：

```python
d.values()
```

例如：

```python
for value in d.values():
    print(value)
```

---

## `items()`

如果想要同時取得 key 和 value：

```python
for key, value in d.items():
    print(key, value)
```

這非常常用。

---

# 二十一、➕ 新增和修改 Dictionary

### 新增

```python
d["d"] = 4
```

如果 `"d"` 原本不存在，就會新增：

```text
"d" → 4
```

### 修改

```python
d["a"] = 5
```

如果 `"a"` 已經存在，就會把原本的 value 修改掉。

---

# 二十二、🗑️ `pop()` 刪除 Dictionary 資料

```python
d.pop("a")
```

可以刪除 key 為 `"a"` 的資料。

如果找不到：

```python
d.pop("e", "Not found")
```

就會回傳：

```text
Not found
```

這樣可以避免找不到資料時直接出錯。

---

# 二十三、🔍 `in` 檢查資料

```python
"a" in d
```

可以檢查 Dictionary 裡面有沒有 `"a"` 這個 **key**。

例如：

```python
if "a" in d:
    print("找到了")
```

⚠️ 對 Dictionary 使用 `in` 時，主要是檢查 **key**，不是 value。

---

# 二十四、🪆 Dictionary 裡面還可以放 Dictionary

這是非常重要的進階概念。

例如：

```python
d = {
    "a": [1, 2, 3],
    "b": {
        "c": 4,
        "d": 5
    }
}
```

可以想像成一個大資料夾：

```text
d
├── a → [1, 2, 3]
│
└── b
    ├── c → 4
    └── d → 5
```

所以：

```python
d["b"]["c"]
```

就可以找到：

```text
4
```

---

# 二十五、🎓 成績登記系統

你今天的成績系統是一個非常好的例子。

```python
grade = {
    "小明": {
        "國文": [90, 80, 70],
        "數學": [85, 75, 65],
        "英文": [95, 85, 75]
    }
}
```

資料結構可以想成：

```text
grade
│
├── 小明
│   ├── 國文 → [90, 80, 70]
│   ├── 數學 → [85, 75, 65]
│   └── 英文 → [95, 85, 75]
│
├── 小美
│   └── ...
│
└── 小華
    └── ...
```

所以：

```python
grade["小明"]["數學"]
```

可以取得：

```python
[85, 75, 65]
```

如果要取得第一次數學成績：

```python
grade["小明"]["數學"][0]
```

結果：

```text
85
```

---

# 二十六、🧮 `sum()` 和 `len()`

計算平均成績時，這兩個指令非常重要。

例如：

```python
scores = [90, 80, 70]
```

### `sum()`

```python
sum(scores)
```

得到：

```text
240
```

也就是全部加起來。

### `len()`

```python
len(scores)
```

得到：

```text
3
```

代表有 3 個成績。

所以平均：

```python
avg = sum(scores) / len(scores)
```

就是：

```text
240 ÷ 3
= 80
```

---

# 二十七、🎯 `:.2f` 控制小數位數

例如：

```python
print(f"平均是{avg:.2f}")
```

`.2f` 的意思是：

> 顯示小數點後 2 位。

例如：

```text
80
```

可能顯示成：

```text
80.00
```

---

# 二十八、🖼️ Streamlit 顯示圖片

最後學到：

```python
st.image("圖片路徑", width=300)
```

例如：

```python
st.image(
    "C:/Users/user/Desktop/pythonXAI/image/apple.png",
    width=300
)
```

意思是：

> 在 Streamlit 網頁上顯示這張圖片，而且寬度設定為 300。

---

# ⭐ 今天最重要的觀念總整理

可以把今天學到的 Python 想成下面這張「工具箱」：

| 工具                 | 功能              | 好記的方法   |
| ------------------ | --------------- | ------- |
| `st.columns()`     | 分割網頁欄位          | 📐 切版面  |
| `with col1:`       | 在指定欄位放東西        | 📦 放進箱子 |
| `key`              | 識別 Streamlit 元件 | 🪪 身分證  |
| `st.text_input()`  | 輸入文字            | ⌨️ 輸入框  |
| `st.session_state` | 保存資料            | 🧠 記憶本  |
| `st.rerun()`       | 重新執行程式          | 🔄 重跑   |
| `st.balloons()`    | 氣球動畫            | 🎈 慶祝   |
| `+=`、`-=`          | 快速修改數字          | ➕➖      |
| `while`            | 條件成立就一直做        | 🔁 重複   |
| `break`            | 離開迴圈            | 🛑 停止   |
| `continue`         | 跳過這次迴圈          | ⏭️ 跳過   |
| `random`           | 產生隨機數           | 🎲 抽籤   |
| `try / except`     | 處理錯誤            | 🛡️ 防錯  |
| `dict`             | 用 key 找 value   | 📖 字典   |
| `keys()`           | 找所有 key         | 🔑      |
| `values()`         | 找所有 value       | 📦      |
| `items()`          | 同時找 key 和 value | 🔑📦    |
| `pop()`            | 刪除資料            | 🗑️     |
| `in`               | 檢查有沒有資料         | 🔍      |
| `sum()`            | 全部加起來           | ➕       |
| `len()`            | 計算有幾個           | 🔢      |
| `st.image()`       | 顯示圖片            | 🖼️     |

---

# 🧠 最後用一張圖記住今天的重點

```text
                    Python
                      │
        ┌─────────────┼─────────────┐
        │             │             │
     Streamlit      程式控制       資料儲存
        │             │             │
   ┌────┼────┐    ┌───┼────┐    ┌───┴────┐
   │    │    │    │   │    │    │        │
columns input state while break random  dict
   │         │       │    │      │        │
  排版      記憶     迴圈  停止   隨機    key/value
```

### 🌟 今天最值得記住的 5 個核心觀念

**① `columns`：**
把網頁畫面切成不同欄位。

**② `session_state`：**
讓 Streamlit 可以「記住」資料。

**③ `while + break`：**
讓程式重複執行，直到遇到 `break`。

**④ `try + except`：**
遇到使用者亂輸入時，讓程式比較不容易直接壞掉。

**⑤ `dict`：**
用「`key → value`」的方式整理資料，非常適合做成績表、會員資料、商品資料等。

你今天其實已經開始把 **Python 基礎語法 + Streamlit 網頁介面 + 小型程式實作** 組合起來了；下一步很適合把這些內容整理成「常用指令速查表＋練習題」。
