import streamlit as st
from streamlit_option_menu import option_menu
from pages.estimation import show as show_estimation
from pages.about import show as show_about
import streamlit-option-menu

# ===== REMOVE SIDEBAR =====
st.markdown("""
    <style>
        section[data-testid="stSidebar"] {
            display: none !important;
        }
        .stApp {
            margin-left: 0 !important;
        }
    </style>
""", unsafe_allow_html=True)

# App Header
st.markdown("<h1 class='header'>🚗 Smart Car Price Estimator</h1>", unsafe_allow_html=True)

# Navigation
selected = option_menu(
    menu_title=None,
    options=["Price Estimation", "About"],
    icons=["calculator", "info-circle"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
)

if selected == "Price Estimation":
    show_estimation()
elif selected == "About":
    show_about() 