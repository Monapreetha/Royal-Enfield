import streamlit as st
from src.services.test_ride_service import TestRideService
from src.services.bike_service import BikeService

st.set_page_config(page_title="Test Ride Booking", page_icon="📅", layout="wide")

st.title("4. Test Ride Booking")
tr_service = TestRideService()
bike_service = BikeService()

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Book a Slot")
    with st.form("book_test_ride_form"):
        tr_cid = st.text_input("Customer ID")
        models = bike_service.get_bike_models()
        tr_model = st.selectbox("Bike Model", options=models)
        tr_date = st.date_input("Date")
        tr_time = st.selectbox("Time Slot", options=["10:00 AM", "11:00 AM", "12:00 PM", "02:00 PM", "04:00 PM"])
        tr_contact = st.text_input("Contact Number")
        
        submit = st.form_submit_button("Book Test Ride")

    if submit:
        # Format date as YYYY-MM-DD
        date_str = tr_date.strftime("%Y-%m-%d")
        result = tr_service.book_test_ride(tr_cid, tr_model, date_str, tr_time, tr_contact)
        if "✅" in result:
            st.success(result)
        else:
            st.error(result)

with col2:
    st.markdown("### Scheduled Test Rides")
    if st.button("Refresh"):
        st.rerun()
        
    df = tr_service.get_all_test_rides()
    st.dataframe(df, use_container_width=True)
