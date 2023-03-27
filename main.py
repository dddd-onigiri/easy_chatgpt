import openai
import streamlit as st
from PIL import Image

st.set_page_config(page_title="AI自然言語処理", layout="wide")

st.title("ChatGPT（AI自然言語処理システム）")
st.caption("Created by Daiki Ito")

st.write('初めての方は右のリンクから「Sign up」をしてAPIキーを取得してください',
         'https://beta.openai.com'
         '/account/api-keys')

# マニュアル
if st.checkbox('マニュアルの表示（クリックするとマニュアルが表示されます）'):
    image = Image.open('easy_chatgpt_openai登録手順（割付）-1.png')
    st.image(image)
    image = Image.open('easy_chatgpt_openai登録手順（割付）-2.png')
    st.image(image)
    image = Image.open('easy_chatgpt_openai登録手順（割付）-3.png')
    st.image(image)

# 質問フォーム
with st.form(key='input_form'):
    st.write("こんにちは！何でも聞いてください（あくまで参考にね）")
    input_prompt = '''あなたは研究アシスタントです。ユーザは高校生で、あなたに研究に関する質問を投げかけます。
    アシスタントとして、論文執筆や研究の遂行に役立つ回答を、できる限り根拠を示した上で以下の「」内の質問に返してください。'''
    input_apikey = st.text_input("取得したAPIキーを貼り付けてください")
    input_text = st.text_area("質問を入力してください")
    submitted = st.form_submit_button('質問する')

if submitted:
    with st.spinner("考え中…"):
        openai.api_key = input_apikey
        response = openai.Completion.create(
            # テストa
            engine="text-davinci-003",
            prompt=input_prompt+"「"+input_text+"」",
            temperature=1.0,
            max_tokens=1024,
            top_p=1.0,
            frequency_penalty=0,
            presence_penalty=0
        )

    st.write("返答:", response['choices'][0]['text'])

st.write('ご意見・ご要望は→', 'https://forms.gle/ADcoMh1zQUnoZVub7', 'まで')
st.write('© 2022-2023 Daiki Ito. All Rights Reserved.')
