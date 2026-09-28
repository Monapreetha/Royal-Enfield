import streamlit as st
from src.services.delivery_service import DeliveryService

st.set_page_config(page_title="Delivery Management", page_icon="🚚", layout="wide")

st.title("8. Delivery Management")
service = DeliveryService()

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Update Delivery Status")
    with st.form("update_delivery_form"):
        d_inv = st.text_input("Invoice Number")
        d_date = st.date_input("Delivery Date")
        d_status = st.selectbox("Status", options=["Pending", "Ready for Delivery", "Delivered"])
        
        submit = st.form_submit_button("Update Delivery")

    if submit:
        date_str = d_date.strftime("%Y-%m-%d")
        result = service.update_delivery(d_inv, date_str, d_status)
        if "✅" in result:
            st.success(result)
        else:
            st.error(result)

with col2:
    st.markdown("### Delivery Log")
    if st.button("Refresh Log"):
        st.rerun()
        
    df = service.get_all_deliveries()
    st.dataframe(df, use_container_width=True)
