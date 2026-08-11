import streamlit as st 

# st.number_input()可以讓使用者輸入數字，設定step=1可以讓使用者只能輸入整數
# min value=0可以設定最小值為0，max_value=100可以設定最大值為100
number = st.number_input("請輸入一個數字", step=1, min_value=0, max_value=100)
# st.markdown()可以在網頁使用markdown語法顯示文字
st.markdown(f"你輸入的數字是：{number}")

import streamlit as st 
st.markdown("---")
st.markdown("###練習")
a = st.number_input("請輸入你得分數", step=1, min_value=0, max_value=100)
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

st.markdown("---")
st.markdown("### Button 練習")
#st.button()可以在網頁上顯示一個按鈕使用者可以點擊按鈕
#key是按鈕的辨識名稱，可以用來區分不同的按鈕
#如果使用者點擊按鈕，會回傳True，否則回傳False
st.button("Click me!",key="button")
if st.button("Click me!",key="balloons"):
    st.balloons()
if st.button("Click me!",key="snow"):
    st.snow()
    st.markdown("---")