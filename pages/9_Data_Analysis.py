import streamlit as st
from src.utils.charts import (
    generate_sales_chart, 
    generate_revenue_chart, 
    generate_inventory_chart,
    generate_payment_method_chart,
    generate_test_ride_chart,
    generate_delivery_status_chart,
    generate_satisfaction_chart,
    generate_average_ratings_chart
)

st.set_page_config(page_title="Data Analysis & Insights", page_icon="📈", layout="wide")

st.title("10. Data Analysis & Insights")
st.markdown("### 📈 Comprehensive Dealership Analytics Dashboard")

if st.button("Refresh Charts"):
    st.rerun()

st.markdown("---")
st.header("Sales & Financials")
col1, col2 = st.columns(2)

with col1:
    st.markdown("#### Sales Volume by Model")
    fig1 = generate_sales_chart()
    if fig1:
        st.pyplot(fig1)
    else:
        st.info("No sales data available.")
        
with col2:
    st.markdown("#### Revenue Distribution")
    fig2 = generate_revenue_chart()
    if fig2:
        st.pyplot(fig2)
    else:
        st.info("No revenue data available.")

st.markdown("---")
st.header("Operations & Inventory")
col3, col4 = st.columns(2)

with col3:
    st.markdown("#### Current Bike Inventory")
    fig3 = generate_inventory_chart()
    if fig3:
        st.pyplot(fig3)
    else:
        st.info("No inventory data available.")

with col4:
    st.markdown("#### Delivery Status")
    fig4 = generate_delivery_status_chart()
    if fig4:
        st.pyplot(fig4)
    else:
        st.info("No delivery data available.")

st.markdown("---")
st.header("Customer Insights")
col5, col6 = st.columns(2)

with col5:
    st.markdown("#### Preferred Payment Methods")
    fig5 = generate_payment_method_chart()
    if fig5:
        st.pyplot(fig5)
    else:
        st.info("No payment data available.")

with col6:
    st.markdown("#### Test Rides Booked")
    fig6 = generate_test_ride_chart()
    if fig6:
        st.pyplot(fig6)
    else:
        st.info("No test ride data available.")

st.markdown("---")
st.header("Customer Feedback & Satisfaction")
col7, col8 = st.columns(2)

with col7:
    st.markdown("#### Overall Satisfaction Distribution")
    fig7 = generate_satisfaction_chart()
    if fig7:
        st.pyplot(fig7)
    else:
        st.info("No feedback data available.")

with col8:
    st.markdown("#### Average Ratings by Category")
    fig8 = generate_average_ratings_chart()
    if fig8:
        st.pyplot(fig8)
    else:
        st.info("No feedback data available.")
