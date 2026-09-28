import streamlit as st
from src.services.customer_service import CustomerService

st.set_page_config(page_title="Customer Management", page_icon="👥", layout="wide")

st.title("2. Customer Management")
service = CustomerService()

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Register New Customer")
    with st.form("add_customer_form"):
        c_name = st.text_input("Full Name")
        c_phone = st.text_input("Phone Number")
        c_email = st.text_input("Email")
        c_address = st.text_input("Address")
        submit = st.form_submit_button("Register Customer")

    if submit:
        result = service.add_customer(c_name, c_phone, c_email, c_address)
        if "✅" in result:
            st.success(result)
        else:
            st.error(result)

with col2:
    st.markdown("### Search & View Customers")
    c_search = st.text_input("Search by ID or Name")
    
    df = service.search_customer(c_search)
    st.dataframe(df, use_container_width=True)
