import streamlit as st

def render_services():
    """Renders the Ownership & Services section."""
    st.markdown("<h2 class='hero-text'>OWNERSHIP & SERVICES</h2>", unsafe_allow_html=True)
    st.markdown("<h4 class='hero-text' style='color:#999;'>Keep your Royal Enfield running like new.</h4><br>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("<div style='text-align: center; font-size: 40px;'>🛠️</div>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center;'>Scheduled Maintenance</h3>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #ccc;'>Factory-trained technicians using genuine parts to keep your motorcycle in perfect condition.</p>", unsafe_allow_html=True)
        
    with col2:
        st.markdown("<div style='text-align: center; font-size: 40px;'>⚙️</div>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center;'>Genuine Accessories</h3>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #ccc;'>Customize your ride with our extensive catalog of official Royal Enfield accessories.</p>", unsafe_allow_html=True)
        
    with col3:
        st.markdown("<div style='text-align: center; font-size: 40px;'>🆘</div>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center;'>Roadside Assistance</h3>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #ccc;'>24/7 support anywhere in the country. Ride with peace of mind knowing we've got your back.</p>", unsafe_allow_html=True)
        
    st.markdown("<br><hr>", unsafe_allow_html=True)
