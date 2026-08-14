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
