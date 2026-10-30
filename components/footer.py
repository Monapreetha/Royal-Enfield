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

@st.dialog("🔒 Privacy Policy", width="large")
def show_privacy_policy():
    st.markdown("""
    ### Royal Enfield Customer Data Privacy Policy
    *Effective Date: October 2026 | Royal Enfield (A Unit of Eicher Motors Ltd.)*
    
    ---
    
    #### 1. Information We Collect
    When you explore our digital showroom, configure a motorcycle, or request a test ride, we collect:
    - **Contact Information:** Name, email address, primary phone number, and residential city/state.
    - **Showroom Preferences:** Motorcycle models explored (e.g., Classic 350, Himalayan, Interceptor 650), customized accessories (Make It Yours), and preferred dealership location.
    - **Telemetry & Technical Data:** Anonymized browser signatures, IP address, and interaction metrics to optimize portal responsiveness.
    
    #### 2. How We Utilize Your Information
    - Scheduling test rides and coordinating priority allocation queues with your chosen authorized dealership.
    - Sending order updates, delivery milestone alerts, and customer care responses.
    - Updating you regarding certified Royal Enfield rider community initiatives (e.g., Rider Mania, Himalayan Odyssey) and service campaigns (with explicit consent).
    
    #### 3. Data Protection Safeguards
    - **Strict Confidentiality:** We do not sell, rent, or lease personal customer data to any third-party marketing brokers.
    - **Authorized Network Only:** Information is exclusively shared with authorized Royal Enfield dealerships and verified logistics partners for fulfillment.
    - **Enterprise Encryption:** All data transfers are safeguarded by 256-bit TLS encryption protocols.
    
    #### 4. Contact Our Privacy Grievance Officer
    For questions, records verification, or data deletion requests:  
    📧 **Email:** `privacy@royalenfield.com`  
    🏢 **Address:** Royal Enfield (A Unit of Eicher Motors Ltd.), Tiruvottiyur High Road, Chennai - 600019, Tamil Nadu, India.
    """)
    if st.button("Close", key="close_privacy", type="primary"):
        st.rerun()

@st.dialog("📜 Terms & Conditions", width="large")
def show_terms_and_conditions():
    st.markdown("""
    ### Terms of Service & Showroom Reservation Conditions
    *Effective Date: October 2026 | Royal Enfield Digital Showroom*
    
    ---
    
    #### 1. Showroom Pricing & Quotations
    - All motorcycle prices shown on this platform are **Ex-Showroom** estimates in Indian Rupees (INR).
    - Statutory charges—including State Road Tax (RTO), Motor Vehicle Registration, and Comprehensive Insurance—vary by state and will be computed on the final dealership invoice.
    - Prices prevailing on the date of final vehicle invoicing apply.
    
    #### 2. Booking Priority & Vehicle Allocation
    - Online reservations establish your position in the priority allotment queue at the designated dealership.
    - Vehicle dispatch depends upon factory production batch schedules, shade/variant availability, and regional transit clearances.
    - Dealership representatives will verify statutory identity documents (Aadhaar / PAN and valid Driving License) prior to registration.
    
    #### 3. Cancellation & Full Refund Policy
    - You may cancel your reservation without any penalty prior to chassis (VIN) assignment.
    - 100% of the reservation deposit is refunded to the original payment method within **5 to 7 working days**.
    
    #### 4. Manufacturer Warranty & Care
    - Every Royal Enfield comes backed with a **3-Year / 30,000 km standard warranty** (extendable to 5 years under the Ride Sure program).
    - Unofficial ECU mapping, frame modifications, or installation of non-homologated exhausts void manufacturer warranty.
    
    #### 5. Legal Jurisdiction
    - These terms are governed by the laws of India. Any legal proceedings fall under the exclusive jurisdiction of the competent courts in Chennai, Tamil Nadu.
    """)
    if st.button("Close", key="close_terms", type="primary"):
        st.rerun()

@st.dialog("⚠️ Disclaimer & Legal Notices", width="large")
def show_disclaimer():
    st.markdown("""
    ### Official Disclaimer & Product Notices
    *Royal Enfield Digital Showroom Platform*
    
    ---
    
    #### 1. Imagery & Specifications Notice
    - Colors, finishes, technical attributes, and optional accessories displayed on this portal are for representational purposes.
    - Actual product appearances may vary slightly due to screen calibration and ongoing engineering refinements.
    - Royal Enfield reserves the right to modify specifications, parts, colorways, and prices without prior public notification.
    
    #### 2. Fuel Economy & Performance Data
    - Certified mileage, power, and emission numbers are tested under statutory ARAI / WMTC conditions.
    - Real-world performance varies depending on payload, road topography, weather conditions, tire pressure, and riding habits.
    
    #### 3. Genuine Accessories & Road Safety
    - Always wear an ISI/DOT/ECE-certified helmet and proper motorcycling protective gear.
    - Use only genuine Royal Enfield parts and accessories. Non-certified aftermarket modifications may breach regional Motor Vehicle Acts.
    
    #### 4. Prototype Digital Platform
    - This digital showroom is an interactive experience platform designed for digital showcase, booking simulation, and customer convenience.
    """)
    if st.button("Close", key="close_disclaimer", type="primary"):
        st.rerun()

@st.dialog("🍪 Cookie Policy", width="large")
def show_cookie_policy():
    st.markdown("""
    ### Cookie & Tracking Technologies Policy
    *Effective Date: October 2026*
    
    ---
    
    #### 1. What Are Cookies?
    Cookies are small, secure tokens stored on your browser to make your digital showroom experience smooth, personalized, and responsive.
    
    #### 2. How We Use Cookies
    - **Essential Cookies:** Maintain session state across pages, preserving your test ride reservation and booking details.
    - **Preference Cookies:** Remember your preferred dealership location (e.g., Chennai, Delhi, Bangalore) and custom bike configurations.
    - **Performance & Analytics:** Anonymized data on page load times and module navigation to help our engineering team improve showroom performance.
    
    #### 3. No Third-Party Ad Trackers
    We do not permit third-party advertising tracking networks to install surveillance cookies on your machine through our digital showroom.
    
    #### 4. Managing Cookie Preferences
    You can adjust or disable cookies at any time via your browser settings. Note that disabling essential cookies may require re-entering your preferences during your session.
    """)
    if st.button("Close", key="close_cookies", type="primary"):
        st.rerun()

def render_footer():
    """Renders the website footer with contact info and interactive quick links."""
    st.markdown("---")
    
    # CSS styling for footer buttons and interactive legal links
    st.markdown("""
        <style>
        /* Quick action centered buttons */
        div[data-testid="stButton"] button[kind="secondary"],
        div[data-testid="stButton"] button[kind="primary"] {
            text-align: center !important;
        }
        
        /* Sleek styling for footer tertiary links */
        button[data-testid="baseButton-tertiary"],
        div[data-testid="stButton"] button[kind="tertiary"] {
            text-align: left !important;
            justify-content: flex-start !important;
            padding: 3px 0px !important;
            margin: 0px !important;
            height: auto !important;
            min-height: unset !important;
            color: #b0b0b0 !important;
            font-size: 14px !important;
            font-weight: 400 !important;
            border: none !important;
            background: transparent !important;
            box-shadow: none !important;
            cursor: pointer;
            transition: color 0.2s ease, transform 0.2s ease;
        }
        button[data-testid="baseButton-tertiary"]:hover,
        div[data-testid="stButton"] button[kind="tertiary"]:hover {
            color: #e53935 !important;
            text-decoration: underline !important;
            background: transparent !important;
            transform: translateX(4px);
        }
        </style>
    """, unsafe_allow_html=True)

    # --- QUICK LINKS ABOVE FOOTER ---
    st.markdown("<h3 style='text-align:center;' id='ownership-services'>QUICK ACTIONS & SERVICES</h3><br>", unsafe_allow_html=True)
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
        st.markdown("<h4 id='contact-us'>For Further Queries</h4>", unsafe_allow_html=True)
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
        if st.button("🔒 Privacy Policy", key="legal_privacy_btn", type="tertiary"):
            show_privacy_policy()
        if st.button("📜 Terms & Conditions", key="legal_terms_btn", type="tertiary"):
            show_terms_and_conditions()
        if st.button("⚠️ Disclaimer", key="legal_disclaimer_btn", type="tertiary"):
            show_disclaimer()
        if st.button("🍪 Cookie Policy", key="legal_cookies_btn", type="tertiary"):
            show_cookie_policy()
        
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: center; color: #666; font-size: 12px;'>© 2026 Royal Enfield. This is a digital showroom prototype built with Streamlit.</div>", unsafe_allow_html=True)
