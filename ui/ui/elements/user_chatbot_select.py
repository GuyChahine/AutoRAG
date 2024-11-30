import streamlit as st
from dataclasses import dataclass
import requests


@dataclass
class UserChatbotSelectData:
    set_user_choice: str = None
    set_chatbot_choice: str = None
    user_chatbot_choices: dict = None
    is_set: bool = False


class UserChatbotSelect:

    def __init__(self, data: UserChatbotSelectData):
        self.data = data

        res = requests.get(
            "http://chromadb:8000/api/v1/collections",
            params={
                "tenant": "default_tenant",
                "database": "default_database",
            },
        )
        self.data.user_chatbot_choices = {
            user: [
                collection["name"].split("_")[1]
                for collection in res.json()
                if collection["name"].split("_")[0] == user
            ]
            for user in {collection["name"].split("_")[0] for collection in res.json()}
        }

    def on_click_set_button(self):
        if not self.user_choice or not self.chatbot_choice:
            return
        self.data.set_user_choice = self.user_choice
        self.data.set_chatbot_choice = self.chatbot_choice
        self.data.is_set = True

    def on_click_reset_button(self):
        if not self.data.is_set:
            return
        self.data.set_user_choice = None
        self.data.set_chatbot_choice = None
        self.data.is_set = False

    def user_selectbox(self):
        self.user_choice = st.sidebar.selectbox(
            "User",
            list(self.data.user_chatbot_choices.keys()),
            (
                list(self.data.user_chatbot_choices.keys()).index(
                    self.data.set_user_choice
                )
                if self.data.set_user_choice != None
                else None
            ),
            disabled=self.data.is_set,
        )

    def chatbot_selectbox(self):
        self.chatbot_choice = st.sidebar.selectbox(
            "Chatbot",
            (
                self.data.user_chatbot_choices[self.user_choice]
                if self.user_choice
                else []
            ),
            (
                self.data.user_chatbot_choices[self.user_choice].index(
                    self.data.set_chatbot_choice
                )
                if self.data.set_chatbot_choice != None
                else None
            ),
            disabled=self.data.is_set or self.user_choice == None,
        )

    def __call__(self):
        self.user_selectbox()
        self.chatbot_selectbox()
        col1, col2 = st.sidebar.columns(2)
        col1.button(
            "Set",
            on_click=self.on_click_set_button,
            use_container_width=True,
            disabled=self.data.is_set,
        )
        col2.button(
            "Reset",
            on_click=self.on_click_reset_button,
            use_container_width=True,
            disabled=not self.data.is_set,
        )
        st.sidebar.divider()
