import streamlit as st
from src.services.feedback_service import FeedbackService
from src.services.bike_service import BikeService

st.set_page_config(page_title="Customer Feedback", page_icon="⭐", layout="wide")

st.title("9. Customer Feedback")
fb_service = FeedbackService()
bike_service = BikeService()

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Submit Feedback")
    with st.form("submit_feedback_form"):
        fb_cid = st.text_input("Customer ID")
        fb_inv = st.text_input("Invoice Number")
        
        models = bike_service.get_bike_models()
        fb_model = st.selectbox("Bike Model", options=models)
        
        fb_tr = st.slider("Test Ride Experience (1-5)", 1, 5, 5)
        fb_sales = st.slider("Sales Service Rating (1-5)", 1, 5, 5)
        fb_del = st.slider("Delivery Experience (1-5)", 1, 5, 5)
        fb_overall = st.slider("Overall Satisfaction (1-5)", 1, 5, 5)
        
        fb_comments = st.text_area("Comments")
        
        submit = st.form_submit_button("Submit Feedback")

    if submit:
        result = fb_service.submit_feedback(fb_cid, fb_inv, fb_model, fb_tr, fb_sales, fb_del, fb_overall, fb_comments)
        st.success(result)

with col2:
    st.markdown("### Feedback Records")
    if st.button("Refresh Feedback"):
        st.rerun()
        
    df = fb_service.get_all_feedback()
    st.dataframe(df, use_container_width=True)
