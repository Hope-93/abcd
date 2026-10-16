import streamlit as st
from openai import OpenAI


MODEL = "gpt-4o-mini"
SYSTEM_PROMPT = """You are a helpful, friendly AI assistant. Answer in the user's language.
Use clear Markdown when it improves readability."""


st.set_page_config(page_title="OpenAI 챗봇", page_icon="💬", layout="centered")


def clear_messages() -> None:
    st.session_state.messages = []


with st.sidebar:
    st.header("설정")
    st.caption(f"모델: `{MODEL}`")
    st.divider()
    st.button("대화 초기화", on_click=clear_messages, use_container_width=True)
    st.caption("API 키는 Streamlit Community Cloud Secrets에서 안전하게 관리됩니다.")


st.title("💬 OpenAI 챗봇")
st.caption(f"{MODEL}로 답변합니다.")

if "messages" not in st.session_state:
    st.session_state.messages = []

try:
    api_key = st.secrets["OPENAI_API_KEY"]
except (KeyError, FileNotFoundError):
    st.error("API 키가 설정되지 않았습니다.")
    st.info(
        "Streamlit Community Cloud에서 앱의 Settings → Secrets에 "
        '`OPENAI_API_KEY = "..."` 를 추가한 뒤 다시 실행하세요.'
    )
    st.stop()

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if prompt := st.chat_input("메시지를 입력하세요"):
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("답변을 작성하고 있습니다..."):
            try:
                client = OpenAI(api_key=api_key)
                completion = client.chat.completions.create(
                    model=MODEL,
                    messages=[
                        {"role": "system", "content": SYSTEM_PROMPT},
                        *st.session_state.messages,
                    ],
                )
                answer = completion.choices[0].message.content or "응답을 생성하지 못했습니다."
                st.markdown(answer)
            except Exception as error:
                answer = "죄송합니다. 요청을 처리하지 못했습니다. 잠시 후 다시 시도해 주세요."
                st.error(answer)
                st.caption(f"오류 세부 정보: {error}")

    st.session_state.messages.append({"role": "assistant", "content": answer})
