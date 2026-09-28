import streamlit as st
from src.services.sales_service import SalesService
from src.services.bike_service import BikeService

st.set_page_config(page_title="Bike Purchase & Billing", page_icon="🧾", layout="wide")

st.title("5 & 6. Bike Purchase & Billing")
sales_service = SalesService()
bike_service = BikeService()

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Purchase Details")
    with st.form("purchase_form"):
        p_cid = st.text_input("Customer ID")
        models = bike_service.get_bike_models()
        p_model = st.selectbox("Bike Model", options=models)
        p_color = st.text_input("Color Selected")
        p_qty = st.number_input("Quantity", min_value=1, step=1, value=1)
        p_acc = st.number_input("Accessories Cost (INR)", min_value=0.0, value=0.0)
        p_ins = st.number_input("Insurance Cost (INR)", min_value=0.0, value=0.0)
        p_reg = st.number_input("Registration Charges (INR)", min_value=0.0, value=0.0)
        p_pay = st.selectbox("Payment Method", options=["Cash", "UPI", "Debit Card", "Credit Card", "Bank Transfer", "Loan / EMI"])
        
        submit = st.form_submit_button("Confirm Purchase & Generate Bill")

with col2:
    st.markdown("### Generated Bill")
    if submit:
        result_msg, bill_text = sales_service.generate_bill(p_cid, p_model, p_color, p_qty, p_acc, p_ins, p_reg, p_pay)
        if "✅" in result_msg:
            st.success(result_msg)
            st.code(bill_text, language="text")
        else:
            st.error(result_msg)
            st.info("No bill generated.")
