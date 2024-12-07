import streamlit as st
from dataclasses import dataclass
import requests


@dataclass
class ChatData:
    chat_history: list = None


class Chat:

    def __init__(self, data: ChatData):
        self.data = data
        if not self.data.chat_history:
            self.data.chat_history = []

    def ask_chatbot(self, prompt: str) -> str:
        user = st.session_state["UserChatbotSelectData"].set_user_choice
        chatbot = st.session_state["UserChatbotSelectData"].set_chatbot_choice
        res = requests.post(
            f"http://backend:8000/{user}/ask/{chatbot}",
            json={"query": prompt, "query_type": "ui"},
        )
        return res.json()

    def __call__(self):
        prompt = st.chat_input(
            disabled=not st.session_state["UserChatbotSelectData"].is_set
        )
        if prompt:
            answer = self.ask_chatbot(prompt)
            self.data.chat_history.append({"role": "user", "content": prompt})
            self.data.chat_history.append({"role": "assistant", "content": answer})
        for message in self.data.chat_history:
            st.chat_message(message["role"]).write(message["content"])
