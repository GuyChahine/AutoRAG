import streamlit as st

from ui.utils.misc import add_to_session_state_if_not_in
from ui.elements.user_chatbot_select import UserChatbotSelect, UserChatbotSelectData
from ui.elements.chat import Chat, ChatData

st.title("💬 Chat")

add_to_session_state_if_not_in("UserChatbotSelectData", UserChatbotSelectData())
UserChatbotSelect(st.session_state["UserChatbotSelectData"])()

add_to_session_state_if_not_in("ChatData", ChatData())
Chat(st.session_state["ChatData"])()
