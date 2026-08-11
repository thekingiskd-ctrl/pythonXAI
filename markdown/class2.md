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
