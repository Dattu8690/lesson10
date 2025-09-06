import streamlit as st

st.title("English解読マシーン")

if 'eitango' in st.session_state and st.session_state.eitango:
    st.success(f"{st.session_state.user_name}")
    st.write("サイドページで翻訳し、表示します。")


eitango = {
    "Hello":"ハロー",
    "apple":"アップル",
    "book" : "ブック",
    "school":"スクール",
    "friend":"フレンド",
    "teacher": "ティーチャー",
    "study":"スタディ",
    "play":"プレイ",
    "eat":"イート",
    "happy":"ハッピー",
    "beautiful":"ビューティフル"}