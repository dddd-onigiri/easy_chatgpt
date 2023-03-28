import openai
import streamlit as st
from PIL import Image

st.set_page_config(page_title="メンタルサポートアシスタントAI", layout="wide")

st.title("メンタルサポートAI")
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
    st.write("こんにちは！悩みを相談してください。")
    st.write("質問は具体的なほうが的確にアドバイスをくれます。")
    input_prompt = '''役割：あなたはメンタルサポートアシスタントです。ユーザは高校生で、あなたに様々な悩みや相談を投げかけます。以下の######内の質問に返してください。
    条件：メンタルサポーターとして、ユーザーに寄り添いながら、可能であれば根拠をもとに具体的な解決策を提案してください。
    最初は高校生に共感してあげてください。しかし、「当たり前」という言葉は使わないでください。
    回答は長めに書いてください。また、母の様な優しさを忘れないでください。
    そして、高校生が前向きになれるよう、応援をしてください。'''
    input_apikey = st.text_input("取得したAPIキーを貼り付けてください")
    input_text = st.text_area("質問を入力してください")
    submitted = st.form_submit_button('質問する')

if submitted:
    with st.spinner("考え中…"):
        openai.api_key = input_apikey
        response = openai.Completion.create(
            # テスト
            engine="text-davinci-003",
            prompt=input_prompt+"###"+input_text+"###",
            temperature=0.5,
            max_tokens=2048,
            top_p=1.0,
            frequency_penalty=0,
            presence_penalty=0
        )

    st.write("返答:", response['choices'][0]['text'])

st.write('差し支えなければアンケートへのご協力をお願いします。→', 'https://forms.gle/ADcoMh1zQUnoZVub7', 'まで')
st.write('© 2022-2023 Daiki Ito. All Rights Reserved.')
