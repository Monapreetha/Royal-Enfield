import streamlit as st
from services.public_booking_service import PublicBookingService

def render_contact():
    """Renders the comprehensive Royal Enfield Contact & Customer Support section."""
    
    header_html = """
<div id="contact-us"></div>
<div style="text-align: center; margin-top: 25px; margin-bottom: 25px;">
<h2 class="hero-text" style="font-size: 32px; font-weight: 900; letter-spacing: 2px; color: #ffffff; margin-bottom: 8px;">
CONNECT & CUSTOMER SUPPORT
</h2>
<p style="color: #a0a0a0; font-size: 16px; max-width: 750px; margin: 0 auto; line-height: 1.5;">
Have questions about motorcycle models, test ride reservations, ownership service, or genuine accessories? Reach out to our dedicated concierge team.
</p>
</div>
"""
    clean_header = "\n".join(line.strip() for line in header_html.splitlines() if line.strip())
    st.markdown(clean_header, unsafe_allow_html=True)

    col_info, col_form = st.columns([1, 1], gap="large")

    with col_info:
        info_html = """
<div style="background: rgba(22, 22, 22, 0.9); border: 1px solid #333; border-radius: 8px; padding: 28px 24px; box-shadow: 0 4px 18px rgba(0,0,0,0.4); height: 100%;">
<h3 style="color: #ffffff; font-size: 20px; font-weight: 700; margin-bottom: 20px; border-bottom: 2px solid #cc0000; padding-bottom: 10px; display: inline-block;">
Official Helplines & Directory
</h3>

<div style="margin-bottom: 18px;">
<div style="font-size: 13px; color: #888; text-transform: uppercase; letter-spacing: 1px; font-weight: 600;">Customer Care (Toll-Free)</div>
<div style="font-size: 19px; color: #ffffff; font-weight: 800; margin-top: 3px;">
<a href="tel:18002100007" style="color: #ffffff; text-decoration: none;">📞 1800 210 0007</a>
</div>
<div style="color: #aaa; font-size: 12.5px; margin-top: 2px;">Available 9:00 AM – 9:00 PM IST (All 7 Days)</div>
</div>

<div style="margin-bottom: 18px;">
<div style="font-size: 13px; color: #888; text-transform: uppercase; letter-spacing: 1px; font-weight: 600;">24/7 Roadside Emergency (RSA)</div>
<div style="font-size: 19px; color: #ff4d4d; font-weight: 800; margin-top: 3px;">
<a href="tel:18002100008" style="color: #ff4d4d; text-decoration: none;">🚨 1800 210 0008</a>
</div>
<div style="color: #aaa; font-size: 12.5px; margin-top: 2px;">Pan-India Towing, Flat Tyre & Fuel Dispatch (24x7x365)</div>
</div>

<div style="margin-bottom: 18px;">
<div style="font-size: 13px; color: #888; text-transform: uppercase; letter-spacing: 1px; font-weight: 600;">Official Support Email</div>
<div style="font-size: 16px; color: #ffffff; font-weight: 700; margin-top: 3px;">
<a href="mailto:support@royalenfield.com" style="color: #ffcccc; text-decoration: none;">✉️ support@royalenfield.com</a>
</div>
<div style="color: #aaa; font-size: 12.5px; margin-top: 2px;">Average response time: within 24 business hours</div>
</div>

<div style="margin-bottom: 18px;">
<div style="font-size: 13px; color: #888; text-transform: uppercase; letter-spacing: 1px; font-weight: 600;">Corporate Headquarters</div>
<div style="color: #dddddd; font-size: 13.5px; margin-top: 3px; line-height: 1.4;">
🏢 <strong>Royal Enfield</strong> (A Unit of Eicher Motors Ltd.)<br>
Tiruvottiyur High Road, Tiruvottiyur, Chennai - 600019, Tamil Nadu, India.
</div>
</div>

<div>
<div style="font-size: 13px; color: #888; text-transform: uppercase; letter-spacing: 1px; font-weight: 600;">Showroom Timings</div>
<div style="color: #dddddd; font-size: 13.5px; margin-top: 3px;">
🕒 Monday – Saturday: 9:30 AM – 8:00 PM<br>
🕒 Sunday: 10:00 AM – 7:00 PM
</div>
</div>
</div>
"""
        clean_info = "\n".join(line.strip() for line in info_html.splitlines() if line.strip())
        st.markdown(clean_info, unsafe_allow_html=True)

    with col_form:
        form_title_html = """
<div style="background: rgba(22, 22, 22, 0.9); border: 1px solid #333; border-radius: 8px; padding: 24px; box-shadow: 0 4px 18px rgba(0,0,0,0.4);">
<h3 style="color: #ffffff; font-size: 20px; font-weight: 700; margin-bottom: 6px;">
Send Us a Message
</h3>
<p style="color: #999; font-size: 13px; margin-bottom: 15px;">
Leave your details below and our regional customer care executive will connect with you.
</p>
</div>
"""
        clean_form_title = "\n".join(line.strip() for line in form_title_html.splitlines() if line.strip())
        st.markdown(clean_form_title, unsafe_allow_html=True)

        with st.form("contact_inquiry_form"):
            inq_name = st.text_input("Full Name *", placeholder="Enter your full name")
            c_f1, c_f2 = st.columns(2)
            with c_f1:
                inq_email = st.text_input("Email Address *", placeholder="e.g. name@example.com")
            with c_f2:
                inq_phone = st.text_input("Contact Number *", placeholder="e.g. +91 98765 43210")
            
            inq_topic = st.selectbox("Topic of Inquiry", [
                "Test Ride & Showroom Visit Query",
                "New Motorcycle Booking & Delivery Status",
                "Service Appointment & Maintenance",
                "Genuine Accessories & Make It Yours (MIY)",
                "Dealership & Franchise Opportunity",
                "General Feedback & Customer Experience"
            ])
            inq_msg = st.text_area("Your Message / Details", placeholder="Tell us how we can assist you...", height=100)
            
            submitted = st.form_submit_button("📨 Submit Inquiry", type="primary", use_container_width=True)
            if submitted:
                service = PublicBookingService()
                success, message = service.submit_inquiry(inq_name, inq_email, inq_phone, inq_topic, inq_msg)
                if success:
                    st.success(message)
                else:
                    st.error(message)

    st.markdown("<div style='margin-bottom: 10px;'></div>", unsafe_allow_html=True)
