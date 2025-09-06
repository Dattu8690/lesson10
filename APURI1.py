import streamlit as st

st.title("English解読マシーン")

if 'English' not in st.session_state:
    st.session_state.English = ""

En = st.text_input("翻訳したい英単語を入力してください")
if st.button("翻訳"):

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