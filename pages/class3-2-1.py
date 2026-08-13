import streamlit as st

# 1. 頂部重新整理按鈕
if st.button("重新整理", key="refresh_btn"):
    st.success("已重新整理！")
    st.rerun()

# 2. 標題
st.title("點餐機")

# 初始化購物籃 (List)
if "cart" not in st.session_state:
    st.session_state.cart = []

# 3. 輸入欄位與加入按鈕（並排呈現）
col1, col2 = st.columns([3, 1])
with col1:
    new_item = st.text_input("請輸入餐點", key="food_input")
with col2:
    # 預留垂直間距讓按鈕與輸入框對齊
    st.write("")
    st.write("")
    if st.button("加入", key="add_btn"):
        if new_item.strip():
            st.session_state.cart.append(new_item.strip())
            st.rerun()

st.write("---")

# 4. 購物籃標題（較小的標題）
st.subheader("購物籃")

# 5. 顯示購物籃內容與每項餐點旁邊的刪除按鈕
if not st.session_state.cart:
    st.write("")
else:
    for i in range(len(st.session_state.cart)):
        item_col, del_col = st.columns([3, 1])
        with item_col:
            st.write(f"{st.session_state.cart[i]}")
        with del_col:
            if st.button("刪除", key=f"delete_{i}"):
                st.session_state.cart.pop(i)
                st.rerun()