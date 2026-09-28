import streamlit as st

@st.dialog("🔧 Book a Service")
def show_book_service():
    st.write("Schedule a service appointment for your Royal Enfield.")
    st.text_input("Full Name")
    st.text_input("Vehicle Registration Number")
    st.date_input("Preferred Date")
    st.selectbox("Select Service Center", ["South Chennai Showroom", "Central Chennai Showroom", "West Chennai Showroom"])
    st.text_area("Any specific issues?")
    
    if st.button("Submit Request", type="primary"):
        st.success("Service request submitted successfully! Our team will contact you shortly.")

@st.dialog("📖 Owner's Manuals")
def show_owners_manual():
    st.write("Select your motorcycle to download the official owner's manual.")
    st.selectbox("Select Motorcycle", [
        "Classic 350", "Bullet 350", "Hunter 350", "Meteor 350", 
        "Himalayan", "Interceptor 650", "Continental GT 650", 
        "Super Meteor 650", "Shotgun 650"
    ])
    if st.button("Download PDF", type="primary"):
        st.success("Downloading manual...")
        
@st.dialog("⚙️ Make It Yours (MIY)")
def show_make_it_yours():
    st.write("Customize your Royal Enfield with genuine motorcycle accessories.")
    model = st.selectbox("Select Model to Customize", ["Classic 350", "Hunter 350", "Meteor 350", "Interceptor 650"])
    
    st.write(f"**Available Accessories for {model}:**")
    st.multiselect("Select Upgrades", [
        "Touring Rider Seat", 
        "Black Aero Visor", 
        "Compact Engine Guard", 
        "Bar End Mirrors", 
        "Aluminum Sump Guard"
    ])
    if st.button("Save Configuration", type="primary"):
        st.success("Configuration saved! Bring this to your nearest dealership.")

def render_footer():
    """Renders the website footer with contact info and interactive quick links."""
    st.markdown("---")
    
    # Optional CSS to make buttons in the footer look a bit more compact
    st.markdown("""
        <style>
        div[data-testid="stButton"] button {
            text-align: center !important;
        }
        </style>
    """, unsafe_allow_html=True)

    # --- QUICK LINKS ABOVE FOOTER ---
    st.markdown("<h3 style='text-align:center;'>QUICK ACTIONS</h3><br>", unsafe_allow_html=True)
    q1, q2, q3 = st.columns(3)
    
    with q1:
        if st.button("🔧 Book a Service", use_container_width=True):
            show_book_service()
    with q2:
        if st.button("📖 Owner's Manual", use_container_width=True):
            show_owners_manual()
    with q3:
        if st.button("⚙️ Make it Yours", use_container_width=True):
            show_make_it_yours()
            
    st.markdown("<br><hr>", unsafe_allow_html=True)

    # --- MAIN FOOTER ---
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("#### Ownership & Services")
        st.markdown("""
        - **Scheduled Maintenance:** Factory-trained technicians using genuine parts.
        - **Genuine Accessories:** Customize your ride with our official catalog.
        - **Roadside Assistance:** 24/7 support anywhere in the country.
        """)
        
    with col2:
        st.markdown("#### For Further Queries")
        st.markdown("""
        **Email:** support@royalenfield.com  
        **Toll-Free:** 1800 210 0007  
        **Hours:** 9:00 AM - 9:00 PM (All Days)
        """)
        
    with col3:
        st.markdown("#### Follow Us")
        st.markdown("""
        [📘 Facebook](https://www.facebook.com/RoyalEnfield)  
        [📸 Instagram](https://www.instagram.com/royalenfield/)  
        [🐦 Twitter](https://twitter.com/royalenfield)  
        [▶️ YouTube](https://www.youtube.com/user/RoyalEnfield)
        """)
        
    with col4:
        st.markdown("#### Legal")
        st.markdown("""
        - [Privacy Policy](#)
        - [Terms & Conditions](#)
        - [Disclaimer](#)
        - [Cookie Policy](#)
        """)
        
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: center; color: #666; font-size: 12px;'>© 2026 Royal Enfield. This is a digital showroom prototype built with Streamlit.</div>", unsafe_allow_html=True)
