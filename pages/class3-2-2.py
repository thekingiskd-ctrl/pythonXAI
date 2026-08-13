import streamlit as st

# 1. 頂部重新整理區域
if st.button("重新整理", key="refresh_btn"):
    st.success("已完成重新整理！")
    st.rerun()

# 2. 主標題
st.title("點餐機")

# 初始化 session_state 購物籃清單
if "cart" not in st.session_state:
    st.session_state.cart = []

# 3. 輸入餐點與「加入」按鈕（使用欄位並排）
col1, col2 = st.columns([3, 1])

with col1:
    item_input = st.text_input("請輸入餐點", value="")

with col2:
    # 放置微調留白使按鈕與輸入框對齊
    st.write("")
    st.write("")
    if st.button("加入", key="add_btn"):
        if item_input.strip() != "":
            st.session_state.cart.append(item_input)
            st.rerun()

st.write("---")

# 4. 較小的標題：購物籃
st.header("購物籃")

# 5. 購物籃內容顯示區與「刪除」按鈕
if not st.session_state.cart:
    st.write("")
else:
    for i in range(len(st.session_state.cart)):
        item_col, btn_col = st.columns([3, 1])
        
        with item_col:
            st.write(f"{st.session_state.cart[i]}")
            
        with btn_col:
            # 每個刪除按鈕需要獨立的 key
            if st.button("刪除", key=f"delete_{i}"):
                st.session_state.cart.pop(i)
                st.rerun()