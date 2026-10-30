import streamlit as st
import os
import sys

# Ensure current working directory is digital_showroom directory
SHOWROOM_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(SHOWROOM_DIR)
if SHOWROOM_DIR not in sys.path:
    sys.path.insert(0, SHOWROOM_DIR)

# Set page config for a premium, wide look
st.set_page_config(
    page_title="Royal Enfield | Official Website",
    page_icon="🏍️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- Custom CSS for Premium Look ---
# We inject minimal CSS to hide the Streamlit header and adjust padding for a website feel
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
        .block-container {
            padding-top: 0rem;
            padding-bottom: 0rem;
            max-width: 100%;
        }
        .hero-text {
            text-align: center;
            font-family: 'Helvetica Neue', sans-serif;
        }
        .model-title {
            text-align: center;
            font-size: 24px;
            font-weight: bold;
            margin-top: 10px;
        }
        .model-desc {
            text-align: center;
            color: #ccc;
            font-size: 16px;
        }
    </style>
""", unsafe_allow_html=True)

# Important: We import components after styling so they inherit the classes
from components.navbar import render_navbar
from components.hero import render_hero_section
from components.showcase import render_showcase
from components.rides_info import render_rides
from components.heritage_info import render_heritage
from components.locations import render_locations
from components.booking_form import render_booking_form
from components.services_info import render_services
from components.contact_info import render_contact
from components.footer import render_footer

# --- Build the Page ---
render_navbar()
render_hero_section()
render_showcase()
render_rides()
render_heritage()
render_locations()
render_booking_form()
render_services()
render_contact()
render_footer()

