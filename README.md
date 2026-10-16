# OpenAI Streamlit 챗봇

`gpt-4o-mini`를 사용하는 간단한 Streamlit 챗봇입니다. 대화 내용은 브라우저 세션 동안만 유지됩니다.

## 로컬 실행

1. 패키지를 설치합니다.

   ```bash
   pip install -r requirements.txt
   ```

2. `.streamlit/secrets.toml.example` 파일을 복사해 `.streamlit/secrets.toml`로 만들고, `OPENAI_API_KEY` 값을 채웁니다.
3. 앱을 실행합니다.

   ```bash
   streamlit run app.py
   ```

## Streamlit Community Cloud 배포

1. 이 폴더를 GitHub 저장소에 올립니다.
2. Streamlit Community Cloud에서 저장소와 `app.py`를 선택해 배포합니다.
3. 앱의 **Settings → Secrets**에 아래 내용을 저장합니다.

   ```toml
   OPENAI_API_KEY = "sk-..."
   ```

키는 저장소에 커밋하지 마세요. `.streamlit/secrets.toml`은 `.gitignore`에 포함되어 있습니다.
