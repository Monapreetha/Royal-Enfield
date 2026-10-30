import streamlit as st
from services.public_booking_service import PublicBookingService

def render_booking_form():
    """Renders the form to book a test ride."""
    header_html = """
<div id="experience-the-ride"></div>
<div id="book-test-ride"></div>
<div style="text-align: center; margin-top: 15px; margin-bottom: 25px;">
<h2 class="hero-text" style="font-size: 32px; font-weight: 900; letter-spacing: 2px; color: #ffffff; margin-bottom: 8px;">
EXPERIENCE THE RIDE
</h2>
<p style="color: #a0a0a0; font-size: 16px; max-width: 700px; margin: 0 auto; line-height: 1.5;">
Nothing compares to the roar of a Royal Enfield engine on the open road. Reserve your complimentary priority test ride at your preferred authorized dealership.
</p>
</div>
"""
    st.markdown("\n".join(l.strip() for l in header_html.splitlines() if l.strip()), unsafe_allow_html=True)


    col_form1, col_form2, col_form3 = st.columns([1, 2, 1])

    with col_form2:
        with st.form("public_test_ride_form"):
            st.markdown("##### 🏍️ Test Ride Reservation Form")
            
            c_n, c_p = st.columns(2)
            with c_n:
                name = st.text_input("Full Name *", placeholder="e.g. Vikramaditya")
            with c_p:
                contact = st.text_input("Contact Number *", placeholder="e.g. +91 98765 43210")
            
            models_list = [
                "Classic 350", "Bullet 350", "Hunter 350", "Meteor 350",
                "Himalayan", "Interceptor 650", "Continental GT 650",
                "Super Meteor 650", "Shotgun 650"
            ]
            preselected = st.session_state.get("selected_test_ride_model", "Classic 350")
            default_index = models_list.index(preselected) if preselected in models_list else 0
            
            c_m, c_c = st.columns(2)
            with c_m:
                model = st.selectbox("Select Motorcycle", models_list, index=default_index)
            with c_c:
                dealership = st.selectbox("Preferred Dealership", [
                    "South Chennai Showroom (Adyar)",
                    "Central Chennai Showroom (Nungambakkam)",
                    "West Chennai Showroom (Porur)",
                    "Bandra Showroom (Mumbai)",
                    "South Extension Showroom (Delhi)",
                    "Connaught Place Showroom (Delhi)",
                    "Indiranagar Showroom (Bengaluru)",
                    "Koramangala Showroom (Bengaluru)",
                    "Jubilee Hills Showroom (Hyderabad)"
                ])

            c_d, c_t = st.columns(2)
            with c_d:
                date = st.date_input("Preferred Date")
            with c_t:
                time = st.selectbox("Preferred Slot", [
                    "10:00 AM - 11:30 AM",
                    "11:30 AM - 01:00 PM",
                    "02:00 PM - 03:30 PM",
                    "03:30 PM - 05:00 PM",
                    "05:00 PM - 06:30 PM"
                ])
            
            submitted = st.form_submit_button("🏍️ Confirm Test Ride Booking", type="primary", use_container_width=True)
            
            if submitted:
                service = PublicBookingService()
                success, message = service.book_test_ride(name, contact, model, date, time)
                
                if success:
                    st.success(message)
                    confirm_box = f"""
<div style="background: rgba(30, 45, 30, 0.7); border: 1px solid #2e7d32; border-radius: 6px; padding: 14px 18px; margin-top: 10px;">
<strong style="color: #81c784;">✓ All set for your test ride!</strong>
<p style="color: #c8e6c9; font-size: 13px; margin: 4px 0 0 0;">
A confirmation SMS has been dispatched. Please remember to carry your <strong>Valid Two-Wheeler Driving License</strong> and a <strong>DOT/ISI-certified helmet</strong> to {dealership}.
</p>
</div>
"""
                    st.markdown("\n".join(l.strip() for l in confirm_box.splitlines() if l.strip()), unsafe_allow_html=True)
                else:
                    st.error(message)

    st.markdown("<br><hr style='border-color: #333;'>", unsafe_allow_html=True)

