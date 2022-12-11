import openai
import streamlit as st

st.set_page_config(page_title="AI対話システム", layout="wide")

st.title("ChatGPT（AI対話システム）")
st.caption("Created by Daiki Ito")

st.write('初めての方は右のリンクから「Sign up」をしてAPIキーを取得してください',
         'https://beta.openai.com'
         '/account/api-keys')
# マニュアル
st.write('マニュアルは下記リンクをクリック')
st.write('https://oitauniv-my.sharepoint.com/:b:/g/personal'
         '/dddd_sailing470_oitauniv_onmicrosoft_com/EewMDMq5DF1IjGn5Exe'
         '-0eMBJrDfC1TVEJ3gUtN-Awy-zQ?e=X2onjf')

# 質問フォーム
with st.form(key='input_form'):
    st.write("こんにちは！何でも聞いてください（あくまで参考にね）")
    input_apikey = st.text_input("取得したAPIキーを貼り付けてください")
    input_text = st.text_input("質問を入力してください")
    submitted = st.form_submit_button('質問する')

if submitted:
    with st.spinner("考え中…"):
        openai.api_key = input_apikey
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=input_text,
            temperature=0.5,
            max_tokens=1024,
            top_p=1.0,
            frequency_penalty=0,
            presence_penalty=0
        )

    st.write("返答:", response['choices'][0]['text'])

st.write('ご意見・ご要望は→', 'https://forms.gle/ADcoMh1zQUnoZVub7', 'まで')
st.write('© 2022 Daiki Ito. All Rights Reserved.')
