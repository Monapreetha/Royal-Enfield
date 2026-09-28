import streamlit as st
from src.services.bike_service import BikeService

st.set_page_config(page_title="Bike Management", page_icon="🏍️", layout="wide")

st.title("3. Bike Management")
service = BikeService()

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Add New Bike Model")
    with st.form("add_bike_form"):
        b_model = st.text_input("Model Name")
        b_cc = st.text_input("Engine CC (e.g., 349cc)")
        b_color = st.text_input("Color")
        b_price = st.number_input("Price (INR)", min_value=0.0, step=1000.0)
        b_qty = st.number_input("Quantity", min_value=0, step=1)
        b_feat = st.text_input("Features")
        submit = st.form_submit_button("Add Bike")

    if submit:
        result = service.add_bike(b_model, b_cc, b_color, b_price, b_qty, b_feat)
        if "✅" in result:
            st.success(result)
        else:
            st.error(result)

with col2:
    st.markdown("### Inventory")
    if st.button("Refresh Inventory"):
        st.rerun()
        
    df = service.get_all_bikes()
    st.dataframe(df, use_container_width=True)
