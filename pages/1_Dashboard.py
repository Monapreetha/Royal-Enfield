import streamlit as st
from src.services.dashboard_service import DashboardService

st.set_page_config(page_title="Dashboard", page_icon="📊")

st.title("1. Dashboard")
st.markdown("### 📊 Quick Overview")

service = DashboardService()
tot_cust, tot_bikes, tot_revenue = service.get_dashboard_stats()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Registered Customers", tot_cust)
with col2:
    st.metric("Total Bikes in Stock", tot_bikes)
with col3:
    st.metric("Total Revenue (INR)", f"₹{tot_revenue:,.2f}")

if st.button("Refresh Dashboard"):
    st.rerun()
