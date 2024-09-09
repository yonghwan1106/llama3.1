import streamlit as st
import requests

# API 엔드포인트
endpoint = "https://api.llama.ai/v1/models/3.1-405b"

# API 키 인증
api_key = "LA-372b2dec00874a9b8197263d16aeeef317465303cac244888ac2e2175cc5b458"  # YOUR_API_KEY를 실제 API 키로 대체하세요.

# Streamlit 앱 생성
st.title("LLaMA API 테스트")

# 사용자 입력 받기
prompt = st.text_input("prompt를 입력하세요.")

# API 호출 버튼 생성
option = st.selectbox("엔드포인트를 선택하세요.", ["generate", "completions"])

if st.button("API 호출"):
    # API 키 인증
    headers = {"Authorization": f"Bearer {api_key}"}

    # 요청 데이터 준비
    data = {"prompt": prompt}

    # API 호출
    if option == "generate":
        response = requests.post(endpoint + "/generate", headers=headers, json=data)
    elif option == "completions":
        response = requests.post(endpoint + "/completions", headers=headers, json=data)

    # 응답 처리
    if response.status_code == 200:
        result = response.json()
        st.write(result)
    else:
        st.write(f"Error: {response.status_code}")
