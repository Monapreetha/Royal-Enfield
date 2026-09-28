import streamlit as st
from src.services.sales_service import SalesService

st.set_page_config(page_title="Payment Management", page_icon="💳", layout="wide")

st.title("7. Payment Management")
st.markdown("### View All Transactions")

service = SalesService()

if st.button("Refresh Payments"):
    st.rerun()

df = service.get_all_payments()
st.dataframe(df, use_container_width=True)
