import streamlit as st
import math
from services.public_booking_service import PublicBookingService

BIKE_PRICES = {
    "Hunter 350": 149000,
    "Bullet 350": 173000,
    "Classic 350": 193000,
    "Meteor 350": 205000,
    "Himalayan": 285000,
    "Interceptor 650": 303000,
    "Continental GT 650": 319000,
    "Shotgun 650": 359000,
    "Super Meteor 650": 363000
}

def calculate_emi(principal: float, annual_rate: float, months: int) -> tuple[int, int, int]:
    """Calculates monthly EMI, total interest, and total payable amount."""
    if principal <= 0:
        return 0, 0, 0
    if annual_rate <= 0:
        emi = principal / months
        return int(round(emi)), 0, int(round(principal))
    
    monthly_rate = (annual_rate / 100) / 12
    emi = principal * monthly_rate * ((1 + monthly_rate) ** months) / (((1 + monthly_rate) ** months) - 1)
    total_payment = emi * months
    total_interest = total_payment - principal
    return int(round(emi)), int(round(total_interest)), int(round(total_payment))

def render_booking_form():
    """Renders Experience the Ride alongside Calculate Finance with side-by-side headings."""
    col_ride, col_calc = st.columns([1, 1], gap="large")

    models_list = list(BIKE_PRICES.keys())
    preselected = st.session_state.get("selected_test_ride_model", "Classic 350")
    default_index = models_list.index(preselected) if preselected in models_list else 2

    # --- LEFT COLUMN: EXPERIENCE THE RIDE ---
    with col_ride:
        ride_header_html = """
<div id="experience-the-ride"></div>
<div id="book-test-ride"></div>
<div style="margin-top: 15px; margin-bottom: 20px;">
<h2 class="hero-text" style="font-size: 28px; font-weight: 900; letter-spacing: 2px; color: #ffffff; margin-bottom: 6px;">
EXPERIENCE THE RIDE
</h2>
<p style="color: #a0a0a0; font-size: 14.5px; line-height: 1.5; margin: 0;">
Reserve a complimentary priority test ride at your nearest authorized dealership.
</p>
</div>
"""
        st.markdown("\n".join(l.strip() for l in ride_header_html.splitlines() if l.strip()), unsafe_allow_html=True)

        with st.form("public_test_ride_form"):
            c_n, c_p = st.columns(2)
            with c_n:
                name = st.text_input("Full Name *", placeholder="e.g. Vikramaditya")
            with c_p:
                contact = st.text_input("Contact Number *", placeholder="e.g. +91 98765 43210")
            
            c_m, c_c = st.columns(2)
            with c_m:
                model = st.selectbox("Select Motorcycle", models_list, index=default_index, key="form_model_select")
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

    # --- RIGHT COLUMN: CALCULATE FINANCE ---
    with col_calc:
        calc_header_html = """
<div id="calculate-finance"></div>
<div id="finance-calculator"></div>
<div style="margin-top: 15px; margin-bottom: 20px;">
<h2 class="hero-text" style="font-size: 28px; font-weight: 900; letter-spacing: 2px; color: #ffffff; margin-bottom: 6px;">
CALCULATE FINANCE
</h2>
<p style="color: #a0a0a0; font-size: 14.5px; line-height: 1.5; margin: 0;">
Customize your down payment and monthly EMI plan with partner banks.
</p>
</div>
"""
        st.markdown("\n".join(l.strip() for l in calc_header_html.splitlines() if l.strip()), unsafe_allow_html=True)

        calc_default_idx = models_list.index(model) if model in models_list else default_index
        calc_model = st.selectbox("Motorcycle Model", models_list, index=calc_default_idx, key="calc_model_select")
        base_price = BIKE_PRICES.get(calc_model, 193000)
        
        st.markdown(f"<div style='color: #bbb; font-size: 13px; margin-top: -8px; margin-bottom: 12px;'>Ex-Showroom Price: <strong style='color:#ffffff; font-size: 15px;'>₹{base_price:,.0f}</strong></div>", unsafe_allow_html=True)

        min_dp = int(round(base_price * 0.10, -3))
        max_dp = int(round(base_price * 0.70, -3))
        default_dp = int(round(base_price * 0.20, -3))

        c_dp, c_rate = st.columns(2)
        with c_dp:
            down_payment = st.slider(
                "Down Payment (₹)",
                min_value=min_dp,
                max_value=max_dp,
                value=default_dp,
                step=5000,
                format="₹%d"
            )
        with c_rate:
            annual_rate = st.slider(
                "Interest Rate (% p.a.)",
                min_value=7.5,
                max_value=13.5,
                value=8.9,
                step=0.1
            )

        tenure_months = st.radio(
            "Loan Tenure",
            options=[12, 24, 36, 48, 60],
            index=2,
            horizontal=True,
            format_func=lambda m: f"{m} Months ({m//12} Yr{'s' if m//12>1 else ''})"
        )

        principal = max(0, base_price - down_payment)
        monthly_emi, total_interest, total_payable = calculate_emi(principal, annual_rate, tenure_months)

        # Output EMI Card
        emi_card_html = f"""
<div style="background: linear-gradient(135deg, #1e1e1e 0%, #151515 100%); border: 1px solid #3d3d3d; border-radius: 8px; padding: 18px 20px; margin-top: 15px; box-shadow: 0 4px 14px rgba(0,0,0,0.5);">
<div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 12px;">
<span style="color: #aaaaaa; font-size: 13px; text-transform: uppercase; letter-spacing: 1px; font-weight: 600;">Estimated Monthly EMI</span>
<span style="color: #ffffff; font-size: 26px; font-weight: 900; font-family: 'Helvetica Neue', sans-serif;"><span style="color: #e53935;">₹{monthly_emi:,.0f}</span> <span style="font-size: 14px; font-weight: 500; color: #888;">/ mo</span></span>
</div>
<div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 8px; padding-top: 10px; border-top: 1px solid #2a2a2a; text-align: center;">
<div>
<div style="color: #777; font-size: 11px; text-transform: uppercase;">Loan Principal</div>
<div style="color: #eee; font-size: 13.5px; font-weight: 700;">₹{principal:,.0f}</div>
</div>
<div>
<div style="color: #777; font-size: 11px; text-transform: uppercase;">Total Interest</div>
<div style="color: #e57373; font-size: 13.5px; font-weight: 700;">₹{total_interest:,.0f}</div>
</div>
<div>
<div style="color: #777; font-size: 11px; text-transform: uppercase;">Total Payable</div>
<div style="color: #eee; font-size: 13.5px; font-weight: 700;">₹{total_payable:,.0f}</div>
</div>
</div>
</div>
<div style="display: flex; align-items: center; gap: 8px; margin-top: 10px; color: #888; font-size: 11.5px;">
<span>🏛️</span>
<span>Partner Banks: HDFC, ICICI, SBI, Axis Bank • Instant Approval at Dealership</span>
</div>
"""
        st.markdown("\n".join(l.strip() for l in emi_card_html.splitlines() if l.strip()), unsafe_allow_html=True)

    st.markdown("<br><hr style='border-color: #333;'>", unsafe_allow_html=True)


