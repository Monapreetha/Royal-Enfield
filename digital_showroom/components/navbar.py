import streamlit as st

def render_navbar():
    """Renders a custom HTML/CSS navigation bar mimicking the official website."""
    
    navbar_html = """
    <style>
        .custom-navbar {
            background-color: #1a1a1a;
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            height: 70px;
            display: flex;
            align-items: center;
            padding: 0 40px;
            z-index: 99999;
            font-family: 'Helvetica Neue', Arial, sans-serif;
            border-bottom: 1px solid #333;
        }
        
        .nav-logo {
            color: #cc0000;
            font-size: 26px;
            font-weight: 900;
            letter-spacing: 1px;
            font-family: 'Arial Black', Impact, sans-serif;
            cursor: pointer;
        }
        
        /* Add some padding to the main container so it's not hidden behind the fixed navbar */
        .block-container {
            padding-top: 80px !important; 
        }
    </style>

    <div class="custom-navbar">
        <div class="nav-logo">
            ROYAL ENFIELD
        </div>
    </div>
    """
    
    st.markdown(navbar_html, unsafe_allow_html=True)
