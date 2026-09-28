import streamlit as st
from services.public_booking_service import PublicBookingService

def render_booking_form():
    """Renders the form to book a test ride."""
    st.markdown("<h2 class='hero-text'>EXPERIENCE THE RIDE</h2>", unsafe_allow_html=True)
    st.markdown("<h4 class='hero-text' style='color:#999;'>Book a test ride at your local dealership today.</h4>", unsafe_allow_html=True)

    col_form1, col_form2, col_form3 = st.columns([1, 2, 1])

    with col_form2:
        with st.form("public_test_ride_form"):
            name = st.text_input("Full Name")
            contact = st.text_input("Contact Number")
            model = st.selectbox("Select Model", ["Classic 350", "Continental GT 650", "Himalayan", "Meteor 350", "Hunter 350"])
            date = st.date_input("Preferred Date")
            time = st.selectbox("Preferred Time", ["10:00 AM", "11:00 AM", "12:00 PM", "02:00 PM", "04:00 PM"])
            
            submitted = st.form_submit_button("Book Test Ride", use_container_width=True)
            
            if submitted:
                service = PublicBookingService()
                success, message = service.book_test_ride(name, contact, model, date, time)
                
                if success:
                    st.success(message)
                    st.info("Our local dealership will contact you shortly to confirm details.")
                else:
                    st.error(message)

    st.markdown("<br><br>", unsafe_allow_html=True)
