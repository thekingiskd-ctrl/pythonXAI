import streamlit as st
with st.expander("Class 1 課程筆記"):
    st.write(
        """
# 🐍 Python 初學者筆記

Python 是一種可以讓我們告訴電腦「要做什麼」的程式語言。今天學到的內容有：註解、print、基本資料型態、變數、運算子、運算順序、字串、f-string、len、type、型態轉換、input，以及使用 Streamlit 製作簡單的網頁。

---

# 一、💬 註解

註解就是寫在程式裡面的「說明文字」。註解主要是寫給人看的，Python 不會執行註解。

## 1. 單行註解

在文字前面加上 `#`：

```python
# 這是單行註解
print("Hello!")
```

Python 看到 `#` 後面的內容，就會知道這是註解。

## 2. 多行註解

如果想寫很多行的說明，可以使用三個雙引號：

```python
\"""
這是多行註解
可以寫很多行
\"""
```

## 3. 快速註解

在編輯器中可以使用 `Ctrl + ?` 快速加入或取消註解。

---

# 二、🖨️ print()

`print()` 是非常常用的指令，可以把東西顯示在終端機上。

例如：

```python
print("Hello, World!")
```

電腦就會顯示：

```text
Hello, World!
```

可以把 `print()` 想成：

> 📢「把這個東西說出來給我看！」

---

# 三、📦 Python 的基本資料型態

Python 裡面的資料有很多種類，就像我們生活中有「數字、文字、是或不是」等不同種類。

今天主要學到 4 種基本資料型態：

| Python 名稱 | 中文意思 | 範例            |
| ----------- | -------- | --------------- |
| `int`       | 整數     | `1`、`0`、`-1`  |
| `float`     | 浮點數   | `1.0`、`3.14`   |
| `str`       | 字串     | `"apple"`       |
| `bool`      | 布林值   | `True`、`False` |

## 1. `int`：整數

整數就是沒有小數點的數字。

```python
print(1)
print(0)
print(-1)
print(100)
```

例如 `1`、`2`、`3`、`0`、`-5` 都是 `int`。

⚠️ 要注意：

```python
1
```

是 `int`，不是 `float`。

---

## 2. `float`：浮點數

浮點數就是通常帶有小數點的數字。

```python
print(1.0)
print(1.234)
print(3.14)
```

例如 `1.0`、`1.234`、`3.14` 都是 `float`。

---

## 3. `str`：字串

字串就是文字。

文字通常會放在引號 `" "` 或 `' '` 裡面。

```python
print("apple")
print("Hello")
print("abc123")
```

要注意：

```python
123
```

是數字。

但是：

```python
"123"
```

是字串，也就是文字。

---

## 4. `bool`：布林值

布林值只有兩種：

```python
True
False
```

可以把它想成：

```text
True  = 是、對、真的
False = 不是、錯、假的
```

例如：

```python
print(True)
print(False)
```

---

# 四、📦 變數

變數可以想像成一個「有名字的盒子」。

我們可以把資料放進盒子裡，之後再使用這個盒子的名字找到資料。

例如：

```python
a = 10
```

可以想成：

```text
📦 a
└── 10
```

也就是把 `10` 放進名字叫做 `a` 的盒子裡。

然後：

```python
print(a)
```

就可以把 `a` 裡面的資料顯示出來。

結果：

```text
10
```

## ⭐ `=` 是什麼意思？

在 Python 裡：

```python
a = 10
```

可以理解成：

> 「把右邊的 10 放進左邊的 a 裡。」

例如：

```python
a = 10
print(a)

a = "apple"
print(a)
```

第一次會顯示：

```text
10
```

後來我們把 `a` 裡面的資料換成 `"apple"`，所以第二次會顯示：

```text
apple
```

所以變數裡面的資料是可以改變的。

---

# 五、➕ 運算子

Python 可以幫我們做數學運算。

| 符號 | 名稱   | 功能             |
| ---- | ------ | ---------------- |
| `+`  | 加法   | 把數字加起來     |
| `-`  | 減法   | 把數字減掉       |
| `*`  | 乘法   | 數字相乘         |
| `/`  | 除法   | 數字相除         |
| `//` | 取商   | 只留下除法的商   |
| `%`  | 取餘數 | 找出除完剩下多少 |
| `**` | 次方   | 計算幾次方       |

## 1. 加法 `+`

```python
print(1 + 1)
```

結果：

```text
2
```

## 2. 減法 `-`

```python
print(5 - 2)
```

結果：

```text
3
```

## 3. 乘法 `*`

```python
print(3 * 2)
```

結果：

```text
6
```

## 4. 除法 `/`

```python
print(5 / 2)
```

結果：

```text
2.5
```

## 5. 取商 `//`

```python
print(5 // 2)
```

5 ÷ 2 = 2 …… 1

所以：

```text
5 // 2 = 2
```

`//` 只留下「商」。

## 6. 取餘數 `%`

```python
print(5 % 2)
```

5 ÷ 2 = 2 …… 1

所以：

```text
5 % 2 = 1
```

`%` 是用來找「剩下多少」。

## 7. 次方 `**`

```python
print(2 ** 3)
```

意思是：

```text
2 × 2 × 2
```

答案是：

```text
8
```

所以：

```text
2 ** 3 = 8
```

---

# 六、🧠 運算的優先順序

如果一個算式裡面有很多不同的運算，Python 會按照一定的順序計算。

順序是：

```text
1. ()
2. **
3. * / // %
4. + -
```

可以記成：

> ⭐ 括號 → 次方 → 乘除 → 加減

例如：

```python
print(2 + 3 * 4)
```

Python 會先算：

```text
3 × 4 = 12
```

再算：

```text
2 + 12 = 14
```

所以答案是：

```text
14
```

---

# 七、🍎 字串也可以運算

字串除了拿來顯示文字之外，也可以做一些簡單的運算。

## 1. 字串相加 `+`

```python
print("apple" + "pen")
```

結果：

```text
applepen
```

可以把它想成把兩段文字接在一起。

```text
apple + pen
↓
applepen
```

## 2. 字串乘法 `*`

```python
print("apple" * 3)
```

結果：

```text
appleappleapple
```

意思就是讓 `"apple"` 重複 3 次。

所以可以記成：

> `+` → 把文字接起來
> `*` → 讓文字重複

---

# 八、🎨 f-string：把資料放進文字裡

有時候我們想要在一句話裡面放入變數。

例如：

```python
name = "Evan"
age = 12
```

我們想顯示：

```text
Hello, my name is Evan and I am 12 years old.
```

可以使用 f-string：

```python
print(f"Hello, my name is {name} and I am {age} years old.")
```

注意兩個地方：

第一，在字串前面加上：

```text
f
```

第二，把變數放進：

```text
{}
```

裡面。

例如：

```python
f"我的名字是 {name}"
```

Python 就會把 `{name}` 換成 `name` 裡面的資料。

所以可以記成：

> ⭐ `f` + `"文字 {變數}"` = 把資料放進句子裡

---

# 九、📏 len()

`len()` 是一個函式，可以幫我們計算資料的「長度」。

例如：

```python
print(len("apple"))
```

apple 有 5 個字母，所以：

```text
5
```

也可以計算中文字：

```python
print(len("你好"))
```

結果：

```text
2
```

可以把 `len()` 想成：

> 🔍「幫我數一數！」

---

# 十、🔎 type()

`type()` 可以幫我們查看資料的型態。

例如：

```python
print(type(1))
```

會知道 `1` 是：

```text
int
```

再看看：

```python
print(type(1.0))
```

會知道 `1.0` 是：

```text
float
```

其他例子：

```python
print(type("apple"))
print(type(True))
```

分別是：

```text
str
bool
```

所以可以把 `type()` 想成：

> 🔎「你到底是哪一種資料？」

---

# 十一、🔄 型態轉換

有時候我們需要把資料從一種型態變成另一種型態。

這就叫做：

> 🔄 型態轉換

主要有以下幾種：

```text
int()
float()
str()
bool()
```

## 1. `int()`：變成整數

```python
print(int(1.0))
```

結果：

```text
1
```

也可以：

```python
print(int(1.234))
```

結果：

```text
1
```

⚠️ 注意：小數部分會被去掉，不是四捨五入。

---

## 2. `float()`：變成浮點數

```python
print(float(1))
```

結果：

```text
1.0
```

也可以把數字文字變成浮點數：

```python
print(float("1.234"))
```

結果：

```text
1.234
```

---

## 3. `str()`：變成字串

```python
print(str(1))
```

會把數字 `1` 變成文字 `"1"`。

例如：

```python
str(1.234)
```

會把數字變成字串。

---

## 4. `bool()`：變成布林值

```python
print(bool(1))
```

結果：

```text
True
```

```python
print(bool(0))
```

結果：

```text
False
```

初學時可以先記住：

```text
0 → False
非 0 的數字 → True
```

例如：

```python
print(bool(2 ** 3))
```

因為 `2 ** 3` 是 8，而 8 不是 0，所以結果是：

```text
True
```

---

# 十二、⚠️ 不是所有資料都可以轉換

例如：

```python
print(int("hello"))
```

這會發生錯誤。

因為 `"hello"` 是文字，而且裡面不是數字，Python 沒辦法把它變成整數。

但是：

```python
print(int("123"))
```

就可以成功，因為 `"123"` 裡面是數字文字。

所以要記得：

> 🔢 可以轉換成數字的文字，內容必須是可以理解成數字的資料。

---

# 十三、⌨️ input()

`input()` 可以讓使用者輸入資料。

例如：

```python
a = input("請輸入一些文字: ")
```

程式會先顯示：

```text
請輸入一些文字:
```

然後等待使用者輸入。

## ⭐ 非常重要！

`input()` 得到的資料，**預設都是字串 `str`**。

例如使用者輸入：

```text
10
```

Python 實際上會把它當成：

```python
"10"
```

而不是：

```python
10
```

所以如果我們想拿輸入的內容來計算，就需要先轉換型態。

例如：

```python
a = input("請輸入一個數字: ")
print(int(a) + 10)
```

如果輸入：

```text
5
```

答案就是：

```text
15
```

也可以使用：

```python
float(a)
```

把輸入的內容轉成浮點數。

---

# 十四、🧮 圓的面積練習

今天還做了一個計算圓面積的練習：

```python
r = input("請輸入圓的半徑: ")
面積 = 3.14 * float(r) ** 2
print(f"圓的面積是 {面積}")
```

這個程式有幾個步驟。

第一步：

```python
r = input("請輸入圓的半徑: ")
```

請使用者輸入圓的半徑。

第二步：

```python
float(r)
```

因為 `input()` 得到的是字串，所以要把它變成數字。

第三步：

```python
3.14 * float(r) ** 2
```

使用圓面積公式：

```text
圓面積 = 3.14 × 半徑²
```

第四步：

```python
print(f"圓的面積是 {面積}")
```

把計算結果顯示出來。

這個練習一次使用了很多今天學到的東西：

```text
input()
↓
變數
↓
float()
↓
**
↓
數學運算
↓
f-string
↓
print()
```

---

# 十五、🌐 Streamlit

前面的 Python 程式大多是在「終端機」看到結果。

Streamlit 是一個可以幫助我們把 Python 程式做成「網頁」的工具。

首先：

```python
import streamlit as st
```

這是在告訴 Python：

> 「我要使用 Streamlit 這個工具。」

`st` 是我們幫 Streamlit 取的簡稱。

---

# 十六、🏷️ st.title()

`st.title()` 可以在網頁上建立一個大標題。

例如：

```python
st.title("這是標題")
```

可以想成：

> 🏷️「在網頁上放一個大標題。」

---

# 十七、✍️ st.write()

`st.write()` 可以在網頁上顯示很多不同種類的資料。

例如：

```python
st.write("Hello!")
```

它可以處理：

- 文字
- 數字
- Markdown
- 表格資料等

可以把它想成：

> 📝「把東西寫到網頁上。」

---

# 十八、📄 st.text()

`st.text()` 可以顯示純文字。

例如：

```python
st.text("這是一段文字")
```

它主要就是把文字直接顯示出來，不會特別處理 Markdown 的格式。

可以把它想成：

> ✏️「原本是什麼樣子，就把文字顯示出來。」

---

# 十九、🎨 st.markdown()

`st.markdown()` 可以使用 Markdown 語法，讓網頁上的文字變得更漂亮。

例如：

```python
st.markdown("**這是粗體文字**")
```

可以讓文字變成粗體。

Markdown 還可以做很多事情，例如：

```text
# 最大標題

## 第二大標題

### 第三大標題
```

也可以做項目清單：

```text
- 第一個項目
- 第二個項目
- 第三個項目
```

也可以做粗體：

```text
**粗體文字**
```

斜體：

```text
*斜體文字*
```

連結：

```text
[Google](https://www.google.com)
```

還可以顯示程式碼：

````text
```python
print("Hello World!")
````

````

---

# 二十、📚 今天學到的函式總整理

函式可以想像成「已經做好的小工具」，我們只要使用它，就可以完成特定的工作。

| 函式 | 功能 | 記憶方式 |
|---|---|---|
| `print()` | 顯示資料 | 📢 秀出來 |
| `len()` | 計算長度 | 🔢 數一數 |
| `type()` | 查看資料型態 | 🔎 你是哪一種？ |
| `int()` | 轉成整數 | 🔢 變整數 |
| `float()` | 轉成浮點數 | 🔢 變小數 |
| `str()` | 轉成字串 | 🔤 變文字 |
| `bool()` | 轉成布林值 | ✅❌ 是或不是 |
| `input()` | 讓使用者輸入 | ⌨️ 換你輸入 |

Streamlit 的常用指令：

| 指令 | 功能 |
|---|---|
| `st.title()` | 🏷️ 顯示大標題 |
| `st.write()` | 📝 顯示各種內容 |
| `st.text()` | 📄 顯示純文字 |
| `st.markdown()` | 🎨 使用 Markdown 格式 |

---

# ⭐ 二十一、今天最重要的觀念

今天學到的 Python，可以想像成一個「程式工具箱」。

`print()` 就像是 📢 喇叭，負責把東西說出來。

變數就像是 📦 有名字的盒子，可以把資料放進去。

`type()` 就像 🔎 放大鏡，可以查看資料是哪一種。

`len()` 就像 📏 尺，可以幫我們計算長度。

`input()` 就像 ⌨️ 麥克風，讓使用者把資料輸入給程式。

`int()`、`float()`、`str()`、`bool()` 就像 🔄 變身工具，可以把資料變成不同的型態。

`+`、`-`、`*`、`/`、`//`、`%`、`**` 就像 🧮 計算工具，可以幫我們做不同的數學運算。

f-string 則可以把 📦 變數裡面的資料放進一句話裡。

Streamlit 則可以把我們原本在終端機裡執行的 Python 程式，做成比較漂亮的 🌐 網頁。

---

# 🏆 最後總整理

今天學到的 Python 基礎內容，可以整理成：

```text
🐍 Python
│
├── 💬 註解
│   ├── # 單行註解
│   └── \""" 多行註解 \"""
│
├── 🖨️ print()
│   └── 顯示資料
│
├── 📦 資料型態
│   ├── int → 整數
│   ├── float → 浮點數
│   ├── str → 字串
│   └── bool → True / False
│
├── 📦 變數
│   └── a = 10
│
├── 🧮 運算子
│   ├── + → 加
│   ├── - → 減
│   ├── * → 乘
│   ├── / → 除
│   ├── // → 取商
│   ├── % → 取餘數
│   └── ** → 次方
│
├── 🔤 字串
│   ├── + → 接在一起
│   └── * → 重複
│
├── 🎨 f-string
│   └── 把變數放進文字
│
├── 🛠️ 函式
│   ├── len()
│   ├── type()
│   └── input()
│
├── 🔄 型態轉換
│   ├── int()
│   ├── float()
│   ├── str()
│   └── bool()
│
└── 🌐 Streamlit
    ├── st.title()
    ├── st.write()
    ├── st.text()
    └── st.markdown()
````

## 🎯 一句話記住今天的課程

Python 程式常常會按照「⌨️ 輸入 → 📦 儲存 → 🧮 計算 → 🔄 處理資料 → 🖨️ 顯示結果」的方式運作。今天學會這些基本工具之後，就可以繼續學習 `if`、`for`、`while`、`list` 等更厲害的功能，慢慢做出真正有趣的 Python 程式！

    """
    )



with st.expander("Class2 課堂筆記"):
    st.write(
        """
   # 🐍 Python 初學者筆記（二）

## 今天學習：比較運算子、邏輯運算子、if 判斷、Streamlit、按鈕、for 迴圈

今天學到的內容主要是在教 Python 怎麼「做決定」以及怎麼「重複做事情」。例如我們可以讓電腦判斷密碼對不對、判斷 BMI 是哪一種情況、判斷考試分數是哪一個等級，也可以讓電腦重複執行相同的指令很多次。

---

# 一、🔍 比較運算子

比較運算子就是拿兩個資料來「比一比」。

比較之後，答案通常只有兩種：

```text
True  → 是、對、成立
False → 不是、錯、不成立
```

例如：

```python
print(1 == 1)
```

因為 1 和 1 一樣，所以答案是：

```text
True
```

## ⭐ 常見的比較運算子

| 符號   | 意思    | 範例       | 結果      |
| ---- | ----- | -------- | ------- |
| `==` | 是否相等  | `1 == 1` | `True`  |
| `!=` | 是否不相等 | `1 != 1` | `False` |
| `>`  | 大於    | `2 > 1`  | `True`  |
| `<`  | 小於    | `1 < 2`  | `True`  |
| `>=` | 大於或等於 | `1 >= 1` | `True`  |
| `<=` | 小於或等於 | `1 <= 1` | `True`  |

### 🧠 特別注意 `=` 和 `==`

這兩個很容易搞混！

```python
a = 10
```

`=` 是把資料放進變數。

可以想成：

> 📦 把 10 放進 a 裡。

但是：

```python
a == 10
```

`==` 是「比較」。

意思是：

> 🔍「a 裡面的東西是不是 10？」

所以：

```text
=   → 放資料
==  → 比較是不是一樣
```

---

# 二、⚠️ 比較時要注意資料型態

比較資料時，通常要注意兩邊是不是可以互相比較的型態。

例如數字可以和數字比較：

```python
print(10 > 5)
```

結果：

```text
True
```

文字也可以在適合的情況下互相比較。

初學時可以先記住：

> ⭐ 比較時，盡量讓兩邊是相同或可以互相比較的資料型態。

---

# 三、🧠 邏輯運算子

邏輯運算子可以把不同的「條件」組合起來。

今天學到三個：

```text
and
or
not
```

可以把它們想成三個不同的思考方式。

---

# 四、🤝 and：而且、同時

`and` 的意思是：

> 「兩個條件都要成立才算成立。」

例如：

```python
print(True and True)
```

兩個都是 True，所以答案：

```text
True
```

但是：

```python
print(False and True)
```

其中一個是 False，所以：

```text
False
```

完整整理：

| 第一個   | 第二個   | `and` 結果 |
| ----- | ----- | -------- |
| True  | True  | True     |
| True  | False | False    |
| False | True  | False    |
| False | False | False    |

### 🧠 記憶方法

`and` 就像老師說：

> 「你要**同時**完成作業和考試，才可以得到獎品。」

只要其中一個沒有完成，就不行。

所以：

> ⭐ `and` → **全部都要成立**

---

# 五、🔀 or：或者

`or` 的意思是：

> 「只要有一個條件成立，就算成立。」

例如：

```python
print(True or False)
```

因為其中一個是 True，所以答案：

```text
True
```

只有兩個都是 False 時，才會得到 False。

| 第一個   | 第二個   | `or` 結果 |
| ----- | ----- | ------- |
| True  | True  | True    |
| True  | False | True    |
| False | True  | True    |
| False | False | False   |

### 🧠 記憶方法

`or` 就像：

> 「你有**鉛筆或原子筆其中一個**就可以。」

只要一個條件成立就可以。

所以：

> ⭐ `or` → **至少一個成立**

---

# 六、🔄 not：反過來

`not` 的功能是把 True 和 False 反過來。

```python
print(not True)
```

結果：

```text
False
```

而：

```python
print(not False)
```

結果：

```text
True
```

可以記成：

```text
not True  → False
not False → True
```

### 🧠 記憶方法

> ⭐ `not` → 「反過來！」

---

# 七、🚦 if：讓電腦做判斷

`if` 非常重要。

它可以讓電腦根據條件做不同的事情。

例如：

```python
if 分數 >= 60:
    print("及格")
```

意思是：

> 如果分數大於或等於 60，就顯示「及格」。

Python 的基本寫法：

```python
if 條件:
    要做的事情
```

⚠️ `if` 後面要有 `:`。

而且下面要執行的程式通常需要**縮排**。

例如：

```python
if 10 > 5:
    print("10比較大")
```

---

# 八、🔀 elif：如果前面的條件不成立，再看看這個

`elif` 可以理解成：

> 「如果前面的條件不成立，那再檢查這個條件。」

例如：

```python
if 分數 >= 90:
    print("A")
elif 分數 >= 80:
    print("B")
else:
    print("其他")
```

Python 會從上面開始檢查。

如果第一個 `if` 已經成立，就會執行第一個結果，後面的 `elif` 不需要再檢查。

---

# 九、🚪 else：以上都不是

`else` 可以理解成：

> 「如果前面的條件全部都不符合，就做這件事。」

例如：

```python
if 分數 >= 60:
    print("及格")
else:
    print("不及格")
```

如果分數是 50：

```text
50 >= 60
```

是 False，所以會執行 `else`：

```text
不及格
```

---

# 十、🔐 密碼驗證練習

今天使用 `if`、`elif`、`else` 做了一個密碼驗證程式：

```python
password = input("請輸入密碼：")

if password == "1234":
    print("歡迎Jeffrey")
elif password == "5678":
    print("歡迎Tim")
elif password == "0000":
    print("歡迎chloe")
else:
    print("密碼錯誤")
```

這個程式的意思是：

第一步：

```python
password = input("請輸入密碼：")
```

讓使用者輸入密碼。

第二步：

```python
if password == "1234":
```

檢查密碼是不是 `"1234"`。

如果是：

```text
歡迎Jeffrey
```

如果不是，就繼續檢查下一個：

```python
elif password == "5678":
```

如果是：

```text
歡迎Tim
```

再不符合，就繼續往下檢查。

最後如果全部都不符合：

```python
else:
    print("密碼錯誤")
```

就會顯示：

```text
密碼錯誤
```

---

# 十一、🤔 多個 if 和 if + elif 有什麼不同？

這是一個很重要的觀念。

## 使用很多個 `if`

例如：

```python
if password == "1234":
    print("Jeffrey")

if password == "5678":
    print("Tim")

if password == "0000":
    print("chloe")
```

Python 會把每一個 `if` 都拿出來檢查。

也就是：

```text
檢查第一個
↓
檢查第二個
↓
檢查第三個
```

## 使用 `if + elif + else`

```python
if password == "1234":
    print("Jeffrey")
elif password == "5678":
    print("Tim")
elif password == "0000":
    print("chloe")
else:
    print("密碼錯誤")
```

Python 會從上面開始判斷。

一旦找到符合的條件，就會執行對應的程式，不需要再檢查後面的條件。

### 🧠 簡單記法

```text
很多個 if
→ 每個都會檢查

if + elif + else
→ 找到符合的就可以停下來
```

所以當我們的條件是「只能選其中一個答案」時，使用 `if + elif + else` 通常比較適合。

---

# 十二、📊 BMI 計算練習

今天也用 Python 做了 BMI 計算。

程式：

```python
height = float(input("請輸入身高(公尺)："))
weight = float(input("請輸入體重(公斤)："))

bmi = weight / (height ** 2)

if bmi < 18.5:
    print("體重過輕")
elif bmi < 24:
    print("體重正常")
else:
    print("體重過重")
```

這裡一次使用了很多以前學過的東西。

## 第一步：輸入身高

```python
height = float(input("請輸入身高(公尺)："))
```

`input()` 讓使用者輸入。

`float()` 把輸入的文字變成數字。

---

## 第二步：輸入體重

```python
weight = float(input("請輸入體重(公斤)："))
```

也是先輸入，再使用 `float()` 變成數字。

---

## 第三步：計算 BMI

```python
bmi = weight / (height ** 2)
```

BMI 的計算方式是：

```text
BMI = 體重 ÷ 身高²
```

這裡的：

```python
height ** 2
```

就是「身高的平方」。

---

## 第四步：判斷結果

```python
if bmi < 18.5:
    print("體重過輕")
elif bmi < 24:
    print("體重正常")
else:
    print("體重過重")
```

Python 會根據 BMI 的數字判斷要顯示哪一個結果。

---

# 十三、🌐 Streamlit 的 number_input()

之前學過 Streamlit 可以把 Python 做成網頁。

今天學到：

```python
st.number_input()
```

它可以在網頁上讓使用者輸入「數字」。

例如：

```python
number = st.number_input(
    "請輸入一個數字",
    step=1,
    min_value=0,
    max_value=100
)
```

這裡有幾個重要的設定。

### `step=1`

代表每次增加或減少 1。

例如：

```text
1 → 2 → 3 → 4 → 5
```

### `min_value=0`

設定最小值是 0。

也就是不能輸入小於 0 的數字。

### `max_value=100`

設定最大值是 100。

也就是不能輸入大於 100 的數字。

所以：

```python
st.number_input(
    "請輸入一個數字",
    step=1,
    min_value=0,
    max_value=100
)
```

可以想成：

> 🔢「請輸入 0 到 100 之間的整數。」

---

# 十四、🎨 Streamlit + if：分數等級

今天也練習讓使用者輸入分數，再自動判斷等級。

```python
a = st.number_input(
    "請輸入你的分數",
    step=1,
    min_value=0,
    max_value=100
)

if a >= 90:
    st.markdown("你的等級是A")
elif a >= 80:
    st.markdown("你的等級是B")
elif a >= 70:
    st.markdown("你的等級是C")
elif a >= 60:
    st.markdown("你的等級是D")
else:
    st.markdown("你的等級是F")
```

如果輸入：

```text
95
```

第一個條件：

```text
95 >= 90
```

成立，所以顯示：

```text
你的等級是A
```

如果輸入 85：

```text
85 >= 90 → False
85 >= 80 → True
```

所以顯示：

```text
你的等級是B
```

這就是 `if`、`elif` 和 `else` 很實用的地方。

---

# 十五、🔘 st.button()：建立按鈕

Streamlit 可以使用：

```python
st.button()
```

在網頁上建立一個按鈕。

例如：

```python
st.button("Click me!", key="button")
```

網頁上就會出現：

```text
[ Click me! ]
```

使用者可以按這個按鈕。

---

# 十六、🔑 key 是什麼？

如果網頁上有很多按鈕，Python 必須知道每個按鈕是哪一個。

所以可以使用：

```python
key="button"
```

來幫按鈕取一個辨識名稱。

例如：

```python
st.button("Click me!", key="balloons")
```

另一個：

```python
st.button("Click me!", key="snow")
```

雖然兩個按鈕的文字都一樣，但是它們的 `key` 不一樣，所以 Python 可以分辨它們。

可以把 `key` 想成：

> 🏷️「每個按鈕的身分證名字。」

---

# 十七、🎈 按鈕可以搭配 if

`st.button()` 在使用者按下按鈕時會得到 `True`。

如果沒有按，則是 `False`。

所以可以這樣寫：

```python
if st.button("Click me!", key="balloons"):
    st.balloons()
```

意思是：

> 如果使用者按下這個按鈕，就放氣球！

另一個：

```python
if st.button("Click me!", key="snow"):
    st.snow()
```

意思是：

> 如果使用者按下這個按鈕，就下雪！

所以可以想成：

```text
🔘 按鈕
   ↓
有按嗎？
   ↓
True / False
   ↓
if 判斷
   ↓
執行不同動作
```

---

# 十八、🎈 st.balloons()

```python
st.balloons()
```

會在 Streamlit 網頁上出現氣球動畫。

例如：

```python
if st.button("Click me!", key="balloons"):
    st.balloons()
```

按下按鈕後，就會看到氣球。

---

# 十九、❄️ st.snow()

```python
st.snow()
```

會在 Streamlit 網頁上出現下雪的效果。

例如：

```python
if st.button("Click me!", key="snow"):
    st.snow()
```

按下按鈕後，就會看到雪花。

---

# 二十、🔁 for 迴圈

`for` 迴圈是今天非常重要的新內容。

它的功能是：

> 🔁「把同一件事情重複做好幾次。」

例如我們想要印出：

```text
0
1
2
3
4
```

可以寫：

```python
for i in range(5):
    print(i)
```

這裡的 `for` 就是在告訴 Python：

> 「請重複做這件事情。」

---

# 二十一、📦 for + in

`for` 通常會和 `in` 一起使用。

基本寫法：

```python
for 變數 in 範圍:
    要重複做的事情
```

例如：

```python
for i in range(5):
    print(i)
```

這裡的 `i` 是「迴圈變數」。

每跑一次，`i` 就會拿到一個新的數字。

---

# 二十二、🔢 range(5)

`range(5)` 會產生：

```text
0
1
2
3
4
```

⚠️ 非常重要：

> `range(5)` **不包含 5**！

所以：

```python
for i in range(5):
    print(i)
```

結果：

```text
0
1
2
3
4
```

可以記成：

> ⭐ `range(5)` → 從 0 開始，到 5 的前一個數字結束。

---

# 二十三、🔢 range(1, 5)

`range()` 也可以設定開始和結束的位置。

```python
for i in range(1, 5):
    print(i)
```

會得到：

```text
1
2
3
4
```

一樣不包含最後的 `5`。

所以：

```text
range(1, 5)
→ 1, 2, 3, 4
```

---

# 二十四、⏭️ range(1, 10, 2)

`range()` 還可以設定第三個數字，代表「每次要跳幾格」。

```python
for i in range(1, 10, 2):
    print(i)
```

會得到：

```text
1
3
5
7
9
```

因為每次增加 2：

```text
1 → 3 → 5 → 7 → 9
```

所以：

```text
range(開始, 結束, 間隔)
```

可以記成：

> ⭐ `range(起點, 終點, 每次跳幾格)`

而且：

> ⚠️ 終點永遠不包含在範圍裡。

---

# 二十五、🔁 for 迴圈中的變數

例如：

```python
for i in range(5):
    a = i * 2

print(a)
```

Python 會重複執行：

```text
i = 0 → a = 0 × 2 → a = 0
i = 1 → a = 1 × 2 → a = 2
i = 2 → a = 2 × 2 → a = 4
i = 3 → a = 3 × 2 → a = 6
i = 4 → a = 4 × 2 → a = 8
```

最後一次：

```text
a = 8
```

所以最後：

```python
print(a)
```

會顯示：

```text
8
```

### ⭐ 很重要

每一次迴圈，`i` 都會換成下一個數字。

所以 `i` 可以想成：

> 🔄「現在這一輪拿到的數字。」

---

# 🧠 二十六、今天最重要的記憶法

### 🔍 比較運算子

```text
==  → 一樣嗎？
!=  → 不一樣嗎？
>   → 大於
<   → 小於
>=  → 大於或等於
<=  → 小於或等於
```

### 🧠 邏輯運算子

```text
and → 兩個都要成立
or  → 一個成立就可以
not → 反過來
```

可以記成：

> `and` = 「而且」
> `or` = 「或者」
> `not` = 「不是、反過來」

### 🚦 判斷

```text
if    → 如果
elif  → 不然再看看這個
else  → 上面都不是
```

### 🌐 Streamlit

```text
st.number_input() → 讓使用者輸入數字
st.button()       → 做按鈕
st.balloons()     → 放氣球
st.snow()         → 下雪
st.markdown()     → 顯示 Markdown 文字
```

### 🔁 迴圈

```text
for       → 重複做事情
in        → 從某個範圍拿資料
range()   → 製造一段數字範圍
```

---

# 🏆 二十七、今天的 Python 大整理

今天學到的內容可以想成：

```text
🐍 Python
│
├── 🔍 比較
│   ├── ==  一樣嗎？
│   ├── !=  不一樣嗎？
│   ├── >   大於
│   ├── <   小於
│   ├── >=  大於或等於
│   └── <=  小於或等於
│
├── 🧠 邏輯
│   ├── and → 都要成立
│   ├── or  → 一個成立就可以
│   └── not → 反過來
│
├── 🚦 判斷
│   ├── if
│   ├── elif
│   └── else
│
├── 🌐 Streamlit
│   ├── st.number_input()
│   ├── st.button()
│   ├── st.balloons()
│   ├── st.snow()
│   └── st.markdown()
│
└── 🔁 迴圈
    ├── for
    ├── in
    └── range()
```

## 🎯 一句話記住今天的課程

今天學到的是讓 Python **「會思考、會做選擇、會重複做事情」**的方法。

比較運算子可以讓 Python 比較資料，`and`、`or`、`not` 可以讓 Python 組合不同條件，`if`、`elif`、`else` 可以讓 Python 根據不同情況做不同的事情，而 `for` 迴圈則可以讓 Python 把相同的事情重複做好幾次。再搭配 Streamlit 的輸入框和按鈕，就可以做出會和使用者互動的小網頁。
"""
    ) 