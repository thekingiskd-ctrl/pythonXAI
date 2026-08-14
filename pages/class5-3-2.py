import streamlit as st
import openai    # pip install openai

# from utils import get_openai_api_key

openai.api_key = st.secrets["OPENAI_API_KEY"]

if "history" not in st.session_state:         # 初始化對話紀錄
    st.session_state["history"] = []          # 如果對話記錄不存在，創建一個空列表

if"system_message" not in st.session_state:   # 初始化系統訊息
    st.session_state.system_message = (       #　如果系統訊息不存在，預設系統訊息
        "Please use English"   #
    )
if "model" not in st.session_state:           # 初始化模型
    st.session_state.model = "gpt-4o-mini"    # 如果AI模型不存在，設置預設模型 


#
col1, col2, col3 = st.columns([4, 2, 1])
with col1:
    st.session_state.system_message = st.text_input("System Message", st.session_state.system_message)
with col2:
    st.session_state.model = st.selectbox("AI model",
        ["gpt-4o-mini", "gpt-4o", "gpt-4o-search-preview",],
        )
with col3:
    if st.button("🗑️"):
        st.session_state.history = []
        st.rerun()

for message in st.session_state.history:
    if message["role"] == "user":
        st.chat_message("user", avatar="🪄").write(message["content"])
    else:
        st.chat_message("assistant", avatar="✨").write(message["content"])

prompt = st.chat_input("Please write here")
if prompt:
    st.session_state.history.append(
        {"role": "user", "content": prompt}
    )

    response = openai.chat.completions.create(
        model=st.session_state.model,
        messages=[{"role": "system", "content": st.session_state.system_message}]
        + st.session_state.history,
    )

    assistant_message = response.choices[0].message.content
    st.session_state.history.append(
        {"role": "assistant", "content": assistant_message}
    )
    st.rerun()