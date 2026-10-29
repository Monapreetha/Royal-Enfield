import streamlit as st
import pandas as pd

def render_locations():
    """Renders the Dealership Locations section with an interactive map."""
    st.markdown("<h2 class='hero-text'>FIND A DEALERSHIP</h2>", unsafe_allow_html=True)
    st.markdown("<h4 class='hero-text' style='color:#999;'>Locate your nearest authorized showroom and service center across India.</h4><br>", unsafe_allow_html=True)
    
    locations_data = {
        "Chennai": {
            "stores": [
                {"name": "South Chennai Showroom", "address": "123 Sardar Patel Road, Adyar, Chennai", "type": "Sales & Service", "lat": 13.0012, "lon": 80.2565},
                {"name": "Central Chennai Showroom", "address": "45 Nungambakkam High Road, Chennai", "type": "Sales & Merchandise", "lat": 13.0627, "lon": 80.2407},
                {"name": "West Chennai Showroom", "address": "78 Mount Poonamallee Road, Porur, Chennai", "type": "Service Center Only", "lat": 13.0373, "lon": 80.1606}
            ]
        },
        "Mumbai": {
            "stores": [
                {"name": "Bandra Showroom", "address": "Linking Road, Bandra West, Mumbai", "type": "Sales, Service & Merchandise", "lat": 19.0596, "lon": 72.8295},
                {"name": "Andheri Service Center", "address": "MIDC, Andheri East, Mumbai", "type": "Service Center Only", "lat": 19.1136, "lon": 72.8697}
            ]
        },
        "Delhi": {
            "stores": [
                {"name": "South Extension Showroom", "address": "South Ex Part 2, New Delhi", "type": "Sales & Service", "lat": 28.5684, "lon": 77.2205},
                {"name": "Connaught Place Showroom", "address": "Inner Circle, Connaught Place, New Delhi", "type": "Sales & Merchandise", "lat": 28.6315, "lon": 77.2167}
            ]
        },
        "Bengaluru": {
            "stores": [
                {"name": "Indiranagar Showroom", "address": "100ft Road, Indiranagar, Bengaluru", "type": "Sales, Service & Merchandise", "lat": 12.9784, "lon": 77.6408},
                {"name": "Koramangala Showroom", "address": "80ft Road, Koramangala, Bengaluru", "type": "Sales & Service", "lat": 12.9345, "lon": 77.6200}
            ]
        },
        "Hyderabad": {
            "stores": [
                {"name": "Jubilee Hills Showroom", "address": "Road No. 36, Jubilee Hills, Hyderabad", "type": "Sales, Service & Merchandise", "lat": 17.4326, "lon": 78.4071},
                {"name": "Banjara Hills Service Center", "address": "Road No. 1, Banjara Hills, Hyderabad", "type": "Sales & Service", "lat": 17.4156, "lon": 78.4347}
            ]
        }
    }

    # Use columns to make the selectbox smaller and centered
    col_l, col_m, col_r = st.columns([1, 2, 1])
    with col_m:
        selected_city = st.selectbox("Select your city", list(locations_data.keys()))
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    
    city_info = locations_data[selected_city]
    
    with col1:
        st.markdown(f"<h3 style='color: #cc0000;'>{selected_city} Flagship Stores</h3>", unsafe_allow_html=True)
        for store in city_info["stores"]:
            st.markdown(f"""
            <div style='background-color: #1a1a1a; padding: 15px; border-radius: 5px; margin-bottom: 15px; border-left: 3px solid #cc0000;'>
                <strong>📍 {store['name']}</strong><br>
                <span style='color: #aaa; font-size: 14px;'>{store['address']}</span><br>
                <span style='color: #888; font-style: italic; font-size: 13px;'>{store['type']}</span>
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        # Create a dataframe for the map based on the selected city
        df = pd.DataFrame(city_info["stores"])
        # Render the interactive map (st.map automatically reads 'lat' and 'lon' columns)
        st.map(df, zoom=11, use_container_width=True)
        
    st.markdown("<hr>", unsafe_allow_html=True)
