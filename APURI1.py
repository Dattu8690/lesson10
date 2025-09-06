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

 eitango2 = {
    "Hello":"こんにちは",
    "apple":"りんご",
    "book" :"本",
    "school":"学校",
    "friend":"友達",
    "teacher":"先生",
    "study":"勉強",
    "play":"遊ぶ",
    "eat":"食べる",
    "happy":"幸せ",
    "beautiful":"美しい"}