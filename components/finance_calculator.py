import streamlit as st

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

def render_finance_calculator():
    """Renders the dedicated Calculate Finance & EMI Estimator section."""
    header_html = """
<div id="calculate-finance"></div>
<div id="finance-calculator"></div>
<div style="text-align: center; margin-top: 25px; margin-bottom: 25px;">
<h2 class="hero-text" style="font-size: 32px; font-weight: 900; letter-spacing: 2px; color: #ffffff; margin-bottom: 8px;">
CALCULATE FINANCE
</h2>
<p style="color: #a0a0a0; font-size: 16px; max-width: 700px; margin: 0 auto; line-height: 1.5;">
Plan your motorcycle purchase with tailored down payments, flexible tenures, and competitive partner bank interest rates.
</p>
</div>
"""
    st.markdown("\n".join(l.strip() for l in header_html.splitlines() if l.strip()), unsafe_allow_html=True)

    col_l, col_m, col_r = st.columns([1, 2, 1])

    with col_m:
        models_list = list(BIKE_PRICES.keys())
        preselected = st.session_state.get("selected_test_ride_model", "Classic 350")
        default_index = models_list.index(preselected) if preselected in models_list else 2
        
        calc_model = st.selectbox("Select Motorcycle Model", models_list, index=default_index, key="dedicated_calc_model")
        base_price = BIKE_PRICES.get(calc_model, 193000)
        
        st.markdown(f"<div style='color: #bbb; font-size: 13.5px; margin-top: -6px; margin-bottom: 15px;'>Ex-Showroom Price: <strong style='color:#ffffff; font-size: 16px;'>₹{base_price:,.0f}</strong></div>", unsafe_allow_html=True)

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
<div style="background: linear-gradient(135deg, #1e1e1e 0%, #151515 100%); border: 1px solid #3d3d3d; border-radius: 8px; padding: 22px 24px; margin-top: 15px; box-shadow: 0 4px 18px rgba(0,0,0,0.5);">
<div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 14px;">
<span style="color: #aaaaaa; font-size: 13.5px; text-transform: uppercase; letter-spacing: 1px; font-weight: 600;">Estimated Monthly EMI</span>
<span style="color: #ffffff; font-size: 28px; font-weight: 900; font-family: 'Helvetica Neue', sans-serif;"><span style="color: #e53935;">₹{monthly_emi:,.0f}</span> <span style="font-size: 15px; font-weight: 500; color: #888;">/ mo</span></span>
</div>
<div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; padding-top: 12px; border-top: 1px solid #2a2a2a; text-align: center;">
<div>
<div style="color: #777; font-size: 11px; text-transform: uppercase;">Loan Principal</div>
<div style="color: #eee; font-size: 14px; font-weight: 700;">₹{principal:,.0f}</div>
</div>
<div>
<div style="color: #777; font-size: 11px; text-transform: uppercase;">Total Interest</div>
<div style="color: #e57373; font-size: 14px; font-weight: 700;">₹{total_interest:,.0f}</div>
</div>
<div>
<div style="color: #777; font-size: 11px; text-transform: uppercase;">Total Payable</div>
<div style="color: #eee; font-size: 14px; font-weight: 700;">₹{total_payable:,.0f}</div>
</div>
</div>
</div>
<div style="display: flex; align-items: center; gap: 8px; margin-top: 12px; color: #888; font-size: 12px; justify-content: center;">
<span>🏛️</span>
<span>Partner Banks: HDFC, ICICI, SBI, Axis Bank • Instant Approval at Dealership</span>
</div>
"""
        st.markdown("\n".join(l.strip() for l in emi_card_html.splitlines() if l.strip()), unsafe_allow_html=True)

    st.markdown("<br><hr style='border-color: #333;'>", unsafe_allow_html=True)
