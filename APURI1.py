import streamlit as st

st.title("English解読マシーン")

if 'English' not in st.session_state:
    st.session_state.English = ""
if 'English2' not in st.session_state:
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
     "beautiful":"ビューティフル",
     "car":"カア",
     "sleep":"スリープ",
     "soccer":"サッカー",
     "bed":"ベッド",
     "dog":"ドッグ",
     "doctor":"ドクター",
     "clock":"クロック",
     "color":"カラー",
     "fish":"フィッシュ",
     "Die":"ダーイ"
     }

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
    "beautiful":"美しい",
    "car":"車",
    "sleep":"寝る",
    "soccer":"サッカー",
    "bed":"ベッド",
    "dog":"犬",
    "doctor":"医者",
    "clock":"時計",
    "color":"色",
    "color":"色",
    "fish":"魚",
    "Die":"死ね"}
 
st.session_state.English= eitango[En]
st.session_state.English2= eitango2[En]