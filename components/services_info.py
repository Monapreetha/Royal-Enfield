import streamlit as st

@st.dialog("🔧 Book a Service Appointment")
def show_book_service():
    st.markdown("### Schedule Your Service")
    st.write("Schedule regular maintenance, periodic inspection, or repair with certified Royal Enfield technicians.")
    
    with st.form("dialog_book_service_form"):
        name = st.text_input("Full Name", placeholder="e.g. Rahul Sharma")
        contact = st.text_input("Contact Number", placeholder="e.g. +91 98765 43210")
        reg_number = st.text_input("Vehicle Registration / VIN Number", placeholder="e.g. TN 01 AB 1234")
        model = st.selectbox("Motorcycle Model", [
            "Classic 350", "Hunter 350", "Meteor 350", "Bullet 350",
            "Himalayan 450", "Interceptor 650", "Continental GT 650", 
            "Super Meteor 650", "Shotgun 650"
        ])
        service_type = st.selectbox("Service Type", [
            "1st Free Service (500 km / 45 days)",
            "Periodic Maintenance (Every 5,000 km / 6 months)",
            "General Service & Oil Change",
            "Express Lube Service (90 Mins)",
            "Brake & Suspension Overhaul",
            "Electrical & Diagnostic Scan"
        ])
        center = st.selectbox("Select Service Center", [
            "South Chennai Service Center (Adyar)",
            "Central Chennai Service Center (Nungambakkam)",
            "West Chennai Service Center (Porur)",
            "Bandra West Service Hub (Mumbai)",
            "Andheri East Center (Mumbai)",
            "South Extension Center (New Delhi)",
            "Indiranagar Service Center (Bengaluru)",
            "Jubilee Hills Service Hub (Hyderabad)"
        ])
        pref_date = st.date_input("Preferred Date")
        notes = st.text_area("Any specific issues or symptoms?")
        
        submitted = st.form_submit_button("Confirm Service Booking", type="primary", use_container_width=True)
        if submitted:
            if not name or not contact:
                st.error("Please provide both your Name and Contact Number.")
            else:
                st.success(f"Service appointment confirmed for {model} at {center} on {pref_date}. Our service advisor will call you shortly.")

@st.dialog("📖 Official Owner's Manuals")
def show_owners_manual():
    st.markdown("### Royal Enfield Digital Handbooks")
    st.write("Download complete factory owner's handbooks with service charts, tire pressure specs, and wiring diagrams.")
    
    selected_bike = st.selectbox("Select Your Motorcycle", [
        "Classic 350 (J-Series)", "Bullet 350 (2024)", "Hunter 350", "Meteor 350", 
        "Himalayan 452", "Interceptor 650 Twin", "Continental GT 650 Cafe Racer", 
        "Super Meteor 650 Cruiser", "Shotgun 650 Custom"
    ])
    
    edition = st.radio("Handbook Edition", ["English (Global)", "Hindi (Regional)", "Service & Warranty Schedule"], horizontal=True)
    
    st.markdown(f"""
    **Document Details:**
    - Model: **{selected_bike}**
    - Format: High-Resolution PDF
    - Includes: Maintenance Schedule, Fuse Diagram, Recommended Torque Specs, Warranty Guide.
    """)
    
    if st.button(f"📥 Download {selected_bike} Manual (PDF)", type="primary", use_container_width=True):
        st.success(f"Handbook download started for {selected_bike} ({edition}). Check your downloads folder!")

@st.dialog("⚙️ Make It Yours (MIY) Accessories")
def show_make_it_yours():
    st.markdown("### Make It Yours (MIY) Customizer")
    st.write("Customize your Royal Enfield with 100% factory-homologated, warranty-approved genuine accessories.")
    
    model = st.selectbox("Choose Motorcycle to Customize", [
        "Classic 350", "Hunter 350", "Meteor 350", "Himalayan", "Interceptor 650", "Super Meteor 650"
    ])
    
    st.markdown(f"**Official Accessories for {model}:**")
    col_a, col_b = st.columns(2)
    with col_a:
        st.checkbox("Touring Dual Rider Seat (+₹3,450)")
        st.checkbox("Black Compact Engine Guard (+₹2,800)")
        st.checkbox("Aero Flyscreen Windshield (+₹1,950)")
    with col_b:
        st.checkbox("Machined Bar End Mirrors (+₹4,200)")
        st.checkbox("Heavy-Duty Aluminum Sump Guard (+₹3,100)")
        st.checkbox("Waterproof Pannier Pair (+₹6,500)")
        
    st.selectbox("Dealership for Fitment", [
        "South Chennai Showroom (Adyar)",
        "Connaught Place Showroom (New Delhi)",
        "Indiranagar Showroom (Bengaluru)",
        "Bandra Showroom (Mumbai)",
        "Jubilee Hills Showroom (Hyderabad)"
    ])
    
    if st.button("Save Configuration & Get Dealership Quote", type="primary", use_container_width=True):
        st.success("Configuration saved! A copy with accessories pricing has been reserved for you at your chosen showroom.")

@st.dialog("🆘 24/7 Roadside Assistance (RSA)")
def show_roadside_assistance():
    st.markdown("### Royal Enfield 24/7 Roadside Assistance")
    st.markdown("""
    Ride with ultimate peace of mind. Our nationwide roadside emergency network is standing by 24 hours a day, 365 days a year.
    
    ---
    
    #### 📞 Toll-Free Emergency Dispatch Lines
    - **Emergency RSA Hotline:** `1800 210 0008` (Toll-Free, 24/7)
    - **WhatsApp Assistance:** `+91 91520 22222`
    
    ---
    
    #### 🛠️ Services Covered Under RSA
    - **Towing Support:** Free towing up to 100 km to the nearest authorized Royal Enfield workshop.
    - **Puncture / Flat Tyre Support:** On-site puncture assistance or tube replacement.
    - **Emergency Fuel Dispatch:** Immediate delivery of up to 5 liters of fuel.
    - **Battery Jumpstart:** Fast response jumpstart support.
    - **Key Lockout / Lost Key Assistance:** On-spot key retrieval or spare delivery.
    - **Urgent Message Relay:** Free notification service to your nominated emergency contacts.
    
    ---
    
    *Valid across all national & state highways and city routes across India.*
    """)
    if st.button("Close Helpline", type="primary", use_container_width=True):
        st.rerun()

def render_services():
    """Renders the comprehensive Royal Enfield Ownership & Services section."""
    st.markdown("""
    <div id="ownership-services"></div>
    <div style="text-align: center; margin-top: 20px; margin-bottom: 25px;">
        <h2 class="hero-text" style="font-size: 32px; font-weight: 900; letter-spacing: 2px; color: #ffffff; margin-bottom: 8px;">
            OWNERSHIP & SERVICES
        </h2>
        <p style="color: #a0a0a0; font-size: 16px; max-width: 750px; margin: 0 auto; line-height: 1.5;">
            Engineered for pure endurance. Keep your Royal Enfield running in showroom condition with factory-trained technicians, authentic spares, and round-the-clock support.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # 4 Service Cards Grid
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("""
        <div style="background: rgba(25, 25, 25, 0.85); border: 1px solid #333; border-radius: 8px; padding: 22px 18px; text-align: center; min-height: 250px; box-shadow: 0 4px 15px rgba(0,0,0,0.3); transition: transform 0.2s ease;">
            <div style="font-size: 42px; margin-bottom: 12px;">🛠️</div>
            <h4 style="color: #ffffff; font-weight: 700; margin-bottom: 10px; font-size: 18px;">Scheduled Maintenance</h4>
            <p style="color: #bbbbbb; font-size: 13.5px; line-height: 1.45; margin-bottom: 15px;">
                Factory-trained technicians utilizing genuine lubricants and computerized 30-point diagnostics to preserve performance.
            </p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("🔧 Book a Service", key="btn_svc_sched", use_container_width=True):
            show_book_service()

    with col2:
        st.markdown("""
        <div style="background: rgba(25, 25, 25, 0.85); border: 1px solid #333; border-radius: 8px; padding: 22px 18px; text-align: center; min-height: 250px; box-shadow: 0 4px 15px rgba(0,0,0,0.3); transition: transform 0.2s ease;">
            <div style="font-size: 42px; margin-bottom: 12px;">⚙️</div>
            <h4 style="color: #ffffff; font-weight: 700; margin-bottom: 10px; font-size: 18px;">Genuine Accessories</h4>
            <p style="color: #bbbbbb; font-size: 13.5px; line-height: 1.45; margin-bottom: 15px;">
                Personalize your motorcycle with official Make It Yours (MIY) homologated touring seats, guards, mirrors, and exhaust shields.
            </p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("⚙️ Make It Yours", key="btn_svc_miy", use_container_width=True):
            show_make_it_yours()

    with col3:
        st.markdown("""
        <div style="background: rgba(25, 25, 25, 0.85); border: 1px solid #333; border-radius: 8px; padding: 22px 18px; text-align: center; min-height: 250px; box-shadow: 0 4px 15px rgba(0,0,0,0.3); transition: transform 0.2s ease;">
            <div style="font-size: 42px; margin-bottom: 12px;">🆘</div>
            <h4 style="color: #ffffff; font-weight: 700; margin-bottom: 10px; font-size: 18px;">Roadside Assistance</h4>
            <p style="color: #bbbbbb; font-size: 13.5px; line-height: 1.45; margin-bottom: 15px;">
                24/7 nationwide emergency breakdown support, puncture care, fuel dispatch, and towing across all Indian highways.
            </p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("🆘 RSA Emergency", key="btn_svc_rsa", use_container_width=True):
            show_roadside_assistance()

    with col4:
        st.markdown("""
        <div style="background: rgba(25, 25, 25, 0.85); border: 1px solid #333; border-radius: 8px; padding: 22px 18px; text-align: center; min-height: 250px; box-shadow: 0 4px 15px rgba(0,0,0,0.3); transition: transform 0.2s ease;">
            <div style="font-size: 42px; margin-bottom: 12px;">📖</div>
            <h4 style="color: #ffffff; font-weight: 700; margin-bottom: 10px; font-size: 18px;">Owner's Manuals</h4>
            <p style="color: #bbbbbb; font-size: 13.5px; line-height: 1.45; margin-bottom: 15px;">
                Download factory rider handbooks, wiring schematics, maintenance schedules, and torque specs for any motorcycle model.
            </p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("📖 Owner's Manual", key="btn_svc_manual", use_container_width=True):
            show_owners_manual()

    # Three-Pillar Value Bar
    st.markdown("""
    <br>
    <div style="background: linear-gradient(90deg, #181818 0%, #202020 50%, #181818 100%); border: 1px solid #2e2e2e; border-radius: 6px; padding: 18px 24px; margin-top: 15px; display: flex; flex-wrap: wrap; justify-content: space-around; gap: 20px;">
        <div style="display: flex; align-items: center; gap: 12px;">
            <span style="font-size: 26px;">🛡️</span>
            <div>
                <strong style="color: #ffffff; font-size: 14px; text-transform: uppercase; letter-spacing: 1px;">Ride Sure Warranty</strong>
                <p style="color: #999; font-size: 12px; margin: 0;">Standard 3-Year / 30,000 km warranty extendable up to 5 Years.</p>
            </div>
        </div>
        <div style="display: flex; align-items: center; gap: 12px;">
            <span style="font-size: 26px;">⚡</span>
            <div>
                <strong style="color: #ffffff; font-size: 14px; text-transform: uppercase; letter-spacing: 1px;">Express Service</strong>
                <p style="color: #999; font-size: 12px; margin: 0;">Scheduled periodic lube servicing completed within 90 minutes.</p>
            </div>
        </div>
        <div style="display: flex; align-items: center; gap: 12px;">
            <span style="font-size: 26px;">💯</span>
            <div>
                <strong style="color: #ffffff; font-size: 14px; text-transform: uppercase; letter-spacing: 1px;">100% Genuine Spares</strong>
                <p style="color: #999; font-size: 12px; margin: 0;">Precision-engineered components backed by manufacturer warranty.</p>
            </div>
        </div>
    </div>
    <br><hr style="border-color: #333;">
    """, unsafe_allow_html=True)
