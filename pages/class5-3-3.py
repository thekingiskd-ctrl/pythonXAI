import streamlit as st


# =========================
# 商品資料
# =========================

products = [
    "apple",
    "banana",
    "bg",
    "orange"
]

images = [
    "image/apple.png",
    "image/banana.png",
    "image/bg.png",
    "image/orange.png"
]


# =========================
# 初始化庫存
# =========================

if "stock" not in st.session_state:
    st.session_state.stock = {
        "apple": 10,
        "banana": 10,
        "bg": 10,
        "orange": 10
    }


# =========================
# 購物平台
# =========================

st.title("購物平台")

number = st.number_input(
    "請輸入欄位數",
    min_value=1,
    max_value=5,
    step=1
)


# =========================
# 商品欄位
# =========================

for start in range(0, len(products), number):

    cols = st.columns(number)

    for i in range(number):

        index = start + i

        if index < len(products):

            with cols[i]:

                # 商品圖片
                st.image(images[index], width=150)

                # 商品名稱
                st.subheader(products[index])

                # 商品價格
                st.write("價格：10 元")

                # 商品庫存
                st.write(
                    "庫存：",
                    st.session_state.stock[products[index]]
                )

                # 購買按鈕
                if st.button(
                    "購買" + products[index],
                    key="buy" + products[index]
                ):

                    if st.session_state.stock[products[index]] > 0:

                        st.session_state.stock[products[index]] -= 1

                        st.rerun()

                    else:

                        st.warning("庫存不足！")


# =========================
# 新增商品庫存
# =========================

st.title("新增商品庫存")


col1, col2 = st.columns(2)


# 第一欄：選擇商品
with col1:

    product = st.selectbox(
        "選擇商品",
        products
    )


# 第二欄：新增數量
with col2:

    add_stock = st.number_input(
        "新增庫存數量",
        min_value=1,
        step=1
    )


# =========================
# 新增庫存按鈕
# =========================

if st.button("新增庫存"):

    st.session_state.stock[product] += add_stock

    st.success(
        "已新增 "
        + str(add_stock)
        + " 個 "
        + product
    )

    st.rerun()


# =========================
# 目前商品庫存
# =========================

st.subheader("目前商品庫存：")


for product in products:

    st.write(
        product
        + "："
        + str(st.session_state.stock[product])
        + "件"
    )