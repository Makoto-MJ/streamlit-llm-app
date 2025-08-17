from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage

# ...existing code...
# LLM応答関数
def get_llm_response(user_input: str, expert_type: str) -> str:
    # 専門家タイプごとのシステムメッセージ
    system_messages = {
        "野生動物": "あなたは野生動物の領域の専門家です。専門的な知識を活かして回答してください。",
        "マーケティング": "あなたはマーケティングの領域の専門家です。専門的な知識を活かして回答してください。"
    }
    system_message = system_messages.get(expert_type, "あなたは一般的な知識を持つAIです。")
    # LLM呼び出し
    chat = ChatOpenAI()
    messages = [
        SystemMessage(content=system_message),
        HumanMessage(content=user_input)
    ]
    response = chat(messages)
    return response.content

# アプリ概要・操作説明
st.title("専門家LLMアプリ")
st.markdown("""
このアプリは、選択した専門家（野生動物／マーケティング）の視点でLLMが質問に回答します。  
1. 専門家タイプを選択  
2. 質問を入力して送信  
3. 回答が画面に表示されます
""")

# ラジオボタンで専門家選択
expert_type = st.radio("専門家タイプを選択してください", ("野生動物", "マーケティング"))

# 入力フォーム
user_input = st.text_input("質問を入力してください")

# 送信ボタン
if st.button("送信") and user_input:
    answer = get_llm_response(user_input, expert_type)
    st.markdown("### 回答")
    st.write(answer)
    
    