import streamlit as st

st.set_page_config(
    page_title="Royal Enfield Dealership Management",
    page_icon="🏍️",
    layout="wide",
)

st.title("🏍️ Royal Enfield Dealership Management System")
st.markdown("""
Welcome to the modernized Dealership Management System! 

Navigate through the pages on the left sidebar to manage:
- **Dashboard**: Quick overview of metrics
- **Customer Management**: Register and view customers
- **Bike Management**: Inventory and models
- **Test Ride Booking**: Schedule rides
- **Bike Purchase & Billing**: Generate bills
- **Payment & Delivery**: Track orders
- **Customer Feedback**: Gather ratings
- **Data Analysis**: Visual insights

*This system is built with modularity and SOLID principles in mind.*
""")
