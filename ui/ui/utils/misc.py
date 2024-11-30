import streamlit as st
from typing import Any


def add_to_session_state_if_not_in(key: str, default_value: Any):
    if key not in st.session_state:
        st.session_state[key] = default_value
