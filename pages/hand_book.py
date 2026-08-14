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

import streamlit as st
with st.expander("Class 3 課程筆記"):
    st.write(
        """

    # 🐍 Python 今日上課筆記：從「做圖案」到「整理資料」

今天學到的內容很多，可以把它想成 4 大主題：

1. 🎨 用 **Streamlit** 做網頁小程式
2. 🔺 用 `for` 迴圈做出金字塔
3. 📦 用 **List（串列）** 整理很多資料
4. 🖥️ 用 Streamlit 的 **columns、button、text_input** 做互動介面

---

# 一、Streamlit 是什麼？

`streamlit` 可以幫我們把 Python 程式變成一個簡單的網頁。

首先要先：

```python
import streamlit as st
```

意思就是：

> 「把 Streamlit 工具拿進來使用，並且幫它取一個簡短的名字叫 `st`。」

之後很多指令都會寫成：

```python
st.指令()
```

---

# 二、做一個網頁標題

```python
st.title("數字金字塔")
```

`st.title()` 可以在網頁上顯示**大標題**。

例如：

```python
st.title("我的第一個網站")
```

網頁上就會出現：

# 我的第一個網站

---

# 三、讓使用者輸入數字：`st.number_input()`

```python
a = st.number_input(
    "請輸入一個整數（1到9）",
    min_value=1,
    max_value=9,
    step=1
)
```

這個指令可以讓使用者在網頁上**輸入數字**。

### 幾個重要設定：

| 指令            | 意思        |
| ------------- | --------- |
| `min_value=1` | 最小可以輸入 1  |
| `max_value=9` | 最大可以輸入 9  |
| `step=1`      | 每次增加或減少 1 |

輸入的數字會被放進變數 `a` 裡。

例如輸入：

```text
5
```

就代表：

```python
a = 5
```

---

# 四、用 `st.write()` 顯示文字

```python
st.write("數字金字塔：")
```

`st.write()` 可以在網頁上顯示文字、數字或其他資料。

例如：

```python
st.write("大家好！")
st.write(123)
```

---

# 五、`for` 迴圈：讓電腦重複做事情 🔁

例如：

```python
for i in range(1, a + 1):
    st.write(f"{i}" * i)
```

這裡的 `for` 可以想成：

> 「請電腦重複做這件事情。」

如果：

```python
a = 5
```

那麼：

```python
range(1, a + 1)
```

就是：

```python
range(1, 6)
```

會得到：

```text
1
2
3
4
5
```

---

# 六、`"字"` × 數字：可以重複文字

這個很重要：

```python
"*" * 3
```

結果會是：

```text
***
```

再例如：

```python
"哈" * 4
```

結果：

```text
哈哈哈哈
```

所以：

```python
f"{i}" * i
```

就是把數字 `i` 重複 `i` 次。

例如：

```text
1
22
333
4444
55555
```

這樣就能做出「數字金字塔」！ 🔺

---

# 七、`f""` 是什麼？

例如：

```python
name = "小明"
st.write(f"你好，{name}！")
```

會顯示：

```text
你好，小明！
```

`f""` 可以讓我們把變數放進文字裡。

例如：

```python
i = 5
f"{i}"
```

就可以把 `i` 放到文字中。

---

# 八、箭頭金字塔 🔺

今天還做了一個比較厲害的圖案：

```text
    *
   ***
  *****
 *******
    *
    *
    *
```

這裡使用了：

```python
" " * 數量
```

和：

```python
"*" * 數量
```

### `" "` 是什麼？

它是一個**空白**。

例如：

```python
" " * 4
```

就是：

```text
    （4個空白）
```

所以我們可以利用「空白」把星星往右邊推。

---

# 九、`\n` 是什麼？

在程式裡：

```python
"\n"
```

代表：

> **換到下一行**

例如：

```python
a = "AAA\nBBB"
```

會變成：

```text
AAA
BBB
```

所以製作金字塔時，可以利用 `\n` 讓每一層換到下一行。

---

# 十、List（串列）📦

List 可以想成：

> **一個可以裝很多東西的大盒子。**

例如：

```python
L = [1, 2, 3]
```

裡面有：

```text
1
2
3
```

也可以放不同種類的資料：

```python
L = [1, True, "a", 1.23]
```

甚至 List 裡面還可以放另一個 List：

```python
L = [1, 2, 3, ["a", "b", "c"]]
```

---

# 十一、空的 List

```python
print([])
```

這代表：

> 一個裡面什麼東西都沒有的 List。

就像一個**空盒子**。

---

# 十二、List 的編號：Index

List 裡面的每個東西都有自己的「編號」。

⚠️ **Python 的編號是從 0 開始！**

例如：

```python
L = [1, 2, 3, "a", "b", "c"]
```

它的編號是：

| Index | 內容    |
| ----: | ----- |
|     0 | `1`   |
|     1 | `2`   |
|     2 | `3`   |
|     3 | `"a"` |
|     4 | `"b"` |
|     5 | `"c"` |

所以：

```python
L[0]
```

得到：

```text
1
```

而：

```python
L[3]
```

得到：

```text
a
```

### ⭐ 要記住：

> **List 的第一個元素是 index 0，不是 1！**

---

# 十三、List 切片 `[:]`

切片就是：

> 從 List 裡面「切一部分」出來。

例如：

```python
L = [1, 2, 3, "a", "b", "c"]
```

## `L[1:4]`

```python
L[1:4]
```

會得到：

```python
[2, 3, "a"]
```

因為：

* 從 index `1` 開始
* 到 index `4` **之前停止**
* 所以不包含 index 4

可以記成：

> `開始:結束`

而且**結束的位置不包含在裡面**。

---

# 十四、切片還可以設定「每次跳幾格」

```python
L[1:4:2]
```

意思是：

> 從 index 1 到 index 4 之前，每次跳 2 格。

結果：

```python
[2, "a"]
```

---

# 十五、`L[::2]` 是什麼？

```python
L[::2]
```

意思是：

> 從頭到尾，每次跳 2 格拿一個。

例如：

```python
L = [1, 2, 3, "a", "b", "c"]
```

index：

```text
0  1  2  3   4   5
1  2  3  a   b   c
```

拿 index：

```text
0 → 2 → 4
```

所以得到：

```python
[1, 3, "b"]
```

---

# 十六、`len()`：計算有幾個東西

```python
L = [1, 2, 3, "a", "b", "c"]
print(len(L))
```

結果：

```text
6
```

`len()` 就是：

> **計算 List 裡面有幾個元素。**

⚠️ 注意：

List 有 6 個元素，但是最後一個 index 是 `5`。

因為 index 從 `0` 開始。

```text
元素數量：6
最後 index：5
```

---

# 十七、走訪 List：一個一個拿出來

有兩種常見方法。

## 方法一：使用 index

```python
for i in range(0, len(L), 2):
    print(L[i])
```

這種方法可以取得：

> 「我現在拿的是第幾個位置。」

所以如果我們需要知道 index，就很適合使用這種方法。

---

## 方法二：直接拿 List 裡的東西

```python
for i in L:
    print(i)
```

意思是：

> 「把 L 裡面的東西，一個一個拿出來。」

例如：

```python
L = [1, 2, 3]
```

會依序拿：

```text
1
2
3
```

### ⭐ 小技巧

如果**需要知道位置**：

```python
for i in range(len(L)):
```

如果**只想拿資料**：

```python
for i in L:
```

---

# 十八、`=` 複製資料時要小心 ⚠️

這是今天比較重要的觀念。

## 一般數字

```python
a = 1
b = a
b = 2

print(a, b)
```

結果：

```text
1 2
```

因為把 `a` 的數字給 `b` 後，改變 `b` 不會改變 `a`。

---

# 十九、List 使用 `=` 的特別情況

例如：

```python
a = [1, 2, 3]
b = a
```

這時候不是單純做一份新的 List。

可以想成：

> `a` 和 `b` 都在指向同一個盒子。

所以：

```python
b[0] = 2
```

結果：

```python
a
```

也會變成：

```python
[2, 2, 3]
```

---

# 二十、`.copy()`：真正複製一份 List

如果希望 `a` 和 `b` 是兩個不同的 List，可以使用：

```python
a = [1, 2, 3]
b = a.copy()
```

這樣就像：

> 把原本的盒子複製成另一個新的盒子。

所以：

```python
b[0] = 2
```

只會改變 `b`：

```text
a = [1, 2, 3]
b = [2, 2, 3]
```

### ⭐ 記憶方法

```python
b = a
```

👉 共用同一個 List

```python
b = a.copy()
```

👉 做一份新的 List

---

# 二十一、`.append()`：在 List 最後面加入東西

```python
L = [1, 2, 3]
L.append(4)
```

結果：

```python
[1, 2, 3, 4]
```

可以把 `append()` 想成：

> **在盒子最後面放進一個新東西。**

---

# 二十二、`.remove()`：移除指定的東西

```python
L = ["a", "b", "c", "d", "a"]
L.remove("a")
```

會移除**第一個找到的 `"a"`**。

結果：

```python
["b", "c", "d", "a"]
```

所以：

> `remove()` 是「找內容來刪除」。

---

# 二十三、`.pop()`：按照 index 刪除

```python
L = ["a", "b", "c", "d", "a"]
L.pop(0)
```

會刪除：

```text
index 0
```

也就是第一個 `"a"`。

所以：

> `pop()` 是「找位置來刪除」。

如果沒有寫 index：

```python
L.pop()
```

就會刪除**最後一個元素**。

---

# 二十四、`.sort()`：排序 🔢

```python
L = [1, 3, 2, 4, 5]
L.sort()
```

結果：

```python
[1, 2, 3, 4, 5]
```

`sort()` 預設會：

> **從小排到大。**

⚠️ 而且 `sort()` 會直接改變原本的 List。

---

# 二十五、Streamlit 的分欄：`st.columns()`

現在開始進入網頁設計！

```python
col1, col2 = st.columns(2)
```

意思是：

> 把網頁分成 **2 欄**。

可以想像成：

```text
┌────────────┬────────────┐
│   col1     │    col2    │
│            │            │
└────────────┴────────────┘
```

---

# 二十六、在不同欄位放按鈕

```python
col1.button("按鈕1", key="btn1")
col2.button("按鈕2", key="btn2")
```

就可以把按鈕分別放到不同欄位。

---

# 二十七、可以設定欄位寬度比例

```python
col1, col2 = st.columns([1, 2])
```

這表示：

```text
col1 : col2
 1   :  2
```

所以第二欄會比第一欄寬。

例如：

```text
┌───────┬──────────────┐
│ col1  │     col2     │
└───────┴──────────────┘
```

---

# 二十八、也可以分成 3 欄

```python
col1, col2, col3 = st.columns([1, 2, 3])
```

意思是三個欄位的寬度比例：

```text
1 : 2 : 3
```

第三欄最寬。

---

# 二十九、用 `for` 一次建立很多欄位

例如：

```python
cols = st.columns(4)
```

會產生 4 個欄位：

```text
cols[0]
cols[1]
cols[2]
cols[3]
```

接著：

```python
for i in range(len(cols)):
```

就可以用迴圈一個一個處理這些欄位。

這是一個非常重要的想法：

> **如果有很多相同的東西，就不要一直複製貼上，可以使用 `for`。**

---

# 三十、`with` 是什麼？

例如：

```python
with col1:
    st.button("按鈕1")
    st.write("這是 col1")
```

可以把 `with col1:` 想成：

> 「接下來這些東西，都放進 `col1` 裡面。」

例如：

```python
with col2:
    st.button("按鈕2")
    st.write("這是 col2")
```

這些內容就會放在第二欄。

---

# 三十一、`st.button()`：做一個按鈕 🔘

```python
st.button("按我")
```

就會在網頁上出現一個按鈕。

也可以搭配 `if`：

```python
if st.button("按我"):
    st.balloons()
```

意思是：

> 如果使用者按下按鈕，就放氣球！ 🎈

---

# 三十二、`key` 是什麼？

例如：

```python
st.button("按鈕1", key="btn1")
```

`key` 就像按鈕的：

> **專屬名字或身分證號。**

如果網頁裡有很多按鈕，最好給它們不同的 `key`，讓程式知道每一個按鈕是哪一個。

例如：

```python
key="btn1"
key="btn2"
key="btn3"
```

---

# 三十三、`st.markdown()`：顯示 Markdown 文字

```python
st.markdown("---")
```

這可以用來顯示分隔線。

效果大約像：

---

也可以放一些特別格式的文字。

今天的箭頭金字塔就是使用：

```python
st.markdown(f"`\n箭頭金字塔：\n{a}`")
```

把做好的文字圖案顯示在網頁上。

---

# 三十四、`st.text_input()`：讓使用者輸入文字 ✏️

```python
text = st.text_input(
    "請輸入文字",
    value="這是預設文字"
)
```

這會產生一個文字輸入框。

使用者可以輸入：

```text
你好
```

輸入的內容會放到：

```python
text
```

裡面。

---

# 三十五、顯示使用者輸入的內容

```python
st.write(f"你輸入的文字是{text}")
```

假設使用者輸入：

```text
小明
```

就會顯示：

```text
你輸入的文字是小明
```

這裡又用到了我們前面學過的：

```python
f"文字 {變數}"
```

---

# 🧠 今日 Python 指令總整理

| 指令                       | 小學生版意思             |
| ------------------------ | ------------------ |
| `import streamlit as st` | 把 Streamlit 工具拿來使用 |
| `st.title()`             | 顯示大標題              |
| `st.write()`             | 顯示文字或資料            |
| `st.markdown()`          | 顯示 Markdown 格式     |
| `st.number_input()`      | 讓使用者輸入數字           |
| `st.text_input()`        | 讓使用者輸入文字           |
| `st.button()`            | 建立按鈕               |
| `st.balloons()`          | 放氣球 🎈             |
| `st.columns()`           | 把網頁分成幾欄            |
| `with`                   | 把內容放進指定的欄位         |
| `for`                    | 重複做事情              |
| `range()`                | 產生一連串的數字           |
| `len()`                  | 計算有幾個元素            |
| `append()`               | 在 List 最後面加入東西     |
| `remove()`               | 找指定的內容並刪除          |
| `pop()`                  | 找指定的 index 並刪除     |
| `sort()`                 | 幫 List 排序          |
| `copy()`                 | 複製一份新的 List        |
| `print()`                | 在 Python 執行結果中顯示資料 |

---

# ⭐ 今日最重要的 10 個觀念

### ① Python 的 List index 從 0 開始

```text
L = [10, 20, 30]

index
 0    1    2
```

---

### ② `len()` 是算「有幾個」

```python
len([10, 20, 30])
```

答案：

```text
3
```

不是最後的 index。

---

### ③ `L[開始:結束]`

結束的位置**不包含**。

```python
L[1:4]
```

就是：

> 從 1 開始拿，到 4 之前停止。

---

### ④ `append()` 是加入

```python
L.append(4)
```

👉 在最後面加入 `4`

---

### ⑤ `remove()` 是按照「內容」刪除

```python
L.remove("a")
```

👉 找 `"a"` 來刪。

---

### ⑥ `pop()` 是按照「位置」刪除

```python
L.pop(0)
```

👉 刪除 index 0。

---

### ⑦ `sort()` 是排序

```python
L.sort()
```

👉 預設從小到大。

---

### ⑧ `for` 可以重複做事情

```python
for i in range(5):
    print(i)
```

👉 讓電腦重複執行。

---

### ⑨ `with` 可以指定內容放在哪裡

```python
with col1:
    st.write("你好")
```

👉 「你好」放在 `col1` 裡。

---

### ⑩ `st.columns()` 可以把網頁切成好幾欄

```python
col1, col2 = st.columns(2)
```

👉 網頁變成兩欄。

---

# 🎯 把今天學的東西想成一個「工具箱」

可以把今天學到的 Python 想成一個工具箱：

```text
🐍 Python 工具箱
│
├── 🔁 for
│   └── 重複做事情
│
├── 📦 List
│   ├── [ ] 建立 List
│   ├── [] 取得資料
│   ├── len() 計算數量
│   ├── append() 加東西
│   ├── remove() 刪東西
│   ├── pop() 刪東西
│   ├── sort() 排順序
│   └── copy() 複製
│
└── 🌐 Streamlit
    ├── title() 標題
    ├── write() 顯示內容
    ├── number_input() 輸入數字
    ├── text_input() 輸入文字
    ├── button() 按鈕
    ├── columns() 分欄
    ├── with 放入指定欄位
    └── balloons() 放氣球
```

**最重要的是：不要只背指令，要理解每個指令「是在做什麼」。** 今天這些內容已經可以開始做出有「輸入、計算、顯示、按鈕、分欄」的小型互動網頁了。

如果你願意，我也可以把這份筆記再整理成一份「國小生考前複習版」，加入**小測驗、填空題與常見錯誤題**。 
"""
    ) 




    import streamlit as st
with st.expander("Class 4 課程筆記"):
    st.write(
        """
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
"""
    )

    import streamlit as st
with st.expander("Class 4 課程筆記"):
    st.write(
        """
可以！如果你的意思是希望我把剛才的內容整理成**更有條理、比較容易抄筆記／整理重點的版本**，我建議用「指令 → 功能 → 簡單例子」的方式。

# 🐍 Python 今日課程筆記

## 一、🤖 OpenAI AI 聊天

### 1. 匯入工具

```python
import openai
```

👉 使用 OpenAI 的 AI 功能。

```python
import os
```

👉 使用電腦的環境變數。

```python
from dotenv import load_dotenv
```

👉 讀取 `.env` 裡面的設定。

---

### 2. 讀取 API Key

```python
load_dotenv()
```

👉 把 `.env` 裡面的資料讀進 Python。

```python
openai.api_key = os.getenv("OPENAI_API_KEY")
```

👉 取得 OpenAI 的 API Key。

🔑 **API Key 就像一把鑰匙，可以讓程式使用 AI 服務。**

---

## 二、🔄 `while` 迴圈

```python
while True:
```

👉 讓程式一直重複執行。

例如聊天機器人就可以一直讓我們輸入問題。

```python
user_inputs = input("You: ")
```

👉 讓使用者輸入文字。

---

## 三、🛑 `break`

```python
if user_inputs.lower() in ["exit", "quit"]:
    break
```

👉 如果使用者輸入 `exit` 或 `quit`，就離開迴圈。

### `.lower()`

```python
"EXIT".lower()
```

結果：

```text
exit
```

👉 把英文全部變成小寫。

---

# 四、💬 呼叫 AI

```python
response = openai.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": user_inputs},
    ],
)
```

這段就是：

👉 **把問題送給 AI。**

### `model`

```python
model="gpt-4o-mini"
```

👉 選擇要使用哪一個 AI 模型。

### `messages`

👉 告訴 AI 對話內容。

---

# 五、👤 三種 `role`

### `system`

```python
{"role": "system", "content": "Please use English"}
```

👉 告訴 AI「你要怎麼做」。

例如：

> 請使用英文回答。

### `user`

```python
{"role": "user", "content": "Hello"}
```

👉 使用者說的話。

### `assistant`

```python
{"role": "assistant", "content": "Hello! How are you?"}
```

👉 AI 回答的話。

---

# 六、📚 AI 對話紀錄

```python
messages = []
```

👉 建立一個空的列表，用來存放聊天紀錄。

### `append()`

```python
messages.append(
    {"role": "user", "content": user_inputs}
)
```

👉 把新的資料放進列表最後面。

所以聊天紀錄就會變成：

```text
使用者：你好
AI：哈囉！
使用者：你叫什麼名字？
AI：我是 AI。
```

AI 每次回答完，也可以把回答放回 `messages` 裡。

👉 這樣 AI 就能知道前面聊過什麼。

---

# 七、📺 `print()`

```python
print(f"AI: {assistant_message}")
```

👉 把 AI 的回答顯示在終端機。

### `f""`

```python
f"AI: {assistant_message}"
```

👉 可以把變數放進文字裡。

---

# 八、🌐 Streamlit

```python
import streamlit as st
```

👉 使用 Streamlit 製作網頁。

---

## 常用 Streamlit 指令

| 指令                  | 功能     |
| ------------------- | ------ |
| `st.title()`        | 大標題    |
| `st.subheader()`    | 小標題    |
| `st.write()`        | 顯示文字   |
| `st.image()`        | 顯示圖片   |
| `st.button()`       | 建立按鈕   |
| `st.text_input()`   | 文字輸入框  |
| `st.number_input()` | 數字輸入框  |
| `st.selectbox()`    | 下拉式選單  |
| `st.chat_input()`   | 聊天輸入框  |
| `st.chat_message()` | 聊天泡泡   |
| `st.columns()`      | 建立欄位   |
| `st.warning()`      | 顯示警告   |
| `st.success()`      | 顯示成功訊息 |

---

# 九、💬 Streamlit 聊天泡泡

```python
st.chat_message("user").write("你好！")
```

👉 顯示使用者的聊天訊息。

```python
st.chat_message("assistant").write("哈囉！")
```

👉 顯示 AI 的聊天訊息。

也可以加入頭像：

```python
st.chat_message(
    "user",
    avatar="🪄"
).write("你好！")
```

---

# 十、🧠 `st.session_state`

這個非常重要！

```python
st.session_state
```

👉 可以把它想成 Streamlit 的**小記憶本**。

例如：

```python
if "history" not in st.session_state:
    st.session_state["history"] = []
```

意思是：

👉 如果還沒有 `history`，就建立一個空列表。

---

### 商品庫存

```python
if "stock" not in st.session_state:
    st.session_state.stock = {
        "apple": 10,
        "banana": 10,
        "bg": 10,
        "orange": 10
    }
```

👉 一開始每個商品都有 10 件。

---

# 十一、📦 商品列表

```python
products = [
    "apple",
    "banana",
    "bg",
    "orange"
]
```

👉 用列表存放商品名稱。

圖片也可以用列表：

```python
images = [
    "image/apple.png",
    "image/banana.png",
    "image/bg.png",
    "image/orange.png"
]
```

---

# 十二、🖼️ 顯示圖片

```python
st.image(images[index], width=150)
```

👉 把商品圖片顯示出來。

---

# 十三、🔢 `number_input`

```python
number = st.number_input(
    "請輸入欄位數",
    min_value=1,
    max_value=5,
    step=1
)
```

👉 建立數字輸入框。

* `min_value=1` → 最小值 1
* `max_value=5` → 最大值 5
* `step=1` → 每次增加 1

---

# 十四、📐 `columns`

```python
cols = st.columns(number)
```

👉 根據 `number` 建立欄位。

例如：

```text
number = 1
```

就一欄。

```text
number = 2
```

就兩欄。

```text
number = 4
```

就四欄。

---

# 十五、🔁 `for` 迴圈

```python
for product in products:
```

👉 把商品一個一個拿出來。

例如：

```text
apple
banana
bg
orange
```

就會一個一個處理。

---

# 十六、➕ `+=`

```python
st.session_state.stock[product] += add_stock
```

👉 增加庫存。

例如：

```text
原本：10
增加：5
結果：15
```

---

# 十七、➖ `-=`

```python
st.session_state.stock[products[index]] -= 1
```

👉 購買一個商品，庫存減少 1。

例如：

```text
原本：10
購買：1
結果：9
```

---

# 十八、🔘 按鈕

```python
if st.button("購買" + products[index]):
```

👉 建立購買按鈕。

按下去之後：

```python
st.session_state.stock[products[index]] -= 1
```

👉 庫存減少 1。

---

# 十九、⚠️ 判斷庫存

```python
if st.session_state.stock[products[index]] > 0:
```

👉 如果庫存大於 0，就可以購買。

如果沒有庫存：

```python
st.warning("庫存不足！")
```

👉 顯示「庫存不足！」。

---

# 二十、🔄 `st.rerun()`

```python
st.rerun()
```

👉 讓 Streamlit 重新執行一次程式。

例如：

```text
原本庫存：10件
↓
按下購買
↓
庫存：9件
↓
st.rerun()
↓
畫面更新成 9件
```

---

# ⭐ 今天最重要的重點

可以把今天學到的東西記成這張「小抄」：

```text
Python
│
├── import        → 匯入工具
├── while         → 一直重複
├── if            → 判斷
├── break         → 離開迴圈
├── for           → 一個一個處理
├── append()      → 加入列表
├── +=            → 增加
├── -=            → 減少
└── print()       → 顯示文字

OpenAI
│
├── openai        → 使用 AI
├── model         → 選擇 AI 模型
├── messages      → 對話紀錄
├── system        → AI 的規則
├── user          → 使用者
└── assistant     → AI

Streamlit
│
├── st.title()          → 大標題
├── st.subheader()      → 小標題
├── st.write()          → 顯示文字
├── st.image()          → 顯示圖片
├── st.button()         → 按鈕
├── st.number_input()   → 數字輸入
├── st.text_input()     → 文字輸入
├── st.selectbox()      → 下拉選單
├── st.columns()        → 欄位
├── st.chat_input()     → 聊天輸入
├── st.chat_message()   → 聊天泡泡
├── st.session_state    → 記住資料
├── st.warning()        → 警告
├── st.success()        → 成功訊息
└── st.rerun()          → 重新執行
```

這樣整理後會比較像**上課時可以直接抄到筆記本的版本**，每個指令旁邊都有「它是做什麼的」，之後寫 Python 時可以直接回來查。

"""
    )