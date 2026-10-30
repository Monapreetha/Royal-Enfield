import streamlit as st

@st.dialog("🏍️ Motoverse (Rider Mania) - Goa")
def show_motoverse_dialog():
    st.markdown("### Motoverse: The Pure Motorcycling Festival")
    st.markdown("""
    Held every November on the sun-kissed beaches of Vagator, Goa, **Motoverse** is the biggest annual gathering of Royal Enfield riders in the world.
    
    ---
    
    #### 🎪 Highlights of Motoverse
    - **Hilltop Dirt Track Racing:** High-adrenaline competition across scramble and dirt tracks.
    - **Custom Build Showcase:** Hand-crafted factory and custom motorcycles from celebrated builders worldwide.
    - **Global Live Music:** Multiple stages featuring indie rock, reggae, electronica, and hip-hop.
    - **Art & Moto Culture:** Rider art galleries, apparel pop-ups, and interactive film screenings.
    
    ---
    
    **Location:** Vagator, North Goa, India  
    **Season:** November Annual  
    **Who Can Join:** Open to all motorcycle riders and community enthusiasts.
    """)
    if st.button("Close", key="close_motoverse", type="primary"):
        st.rerun()

@st.dialog("🏔️ Himalayan Odyssey")
def show_himalayan_odyssey_dialog():
    st.markdown("### The Himalayan Odyssey")
    st.markdown("""
    The holy grail of adventure motorcycling. An epic 18-day expedition conquering the world's most treacherous terrain, high-altitude passes, and pristine Himalayan valleys.
    
    ---
    
    #### 🗺️ Route Overview
    - **Total Distance:** Over 2,200 km
    - **Key Passes:** Rohtang Pass, Baralacha La, Nakee La, Lachung La, Tanglang La, and Khardung La (18,380 ft).
    - **Stages:** New Delhi → Chandigarh → Manali → Jispa → Sarchu → Leh → Nubra Valley → Pangong Tso → Dras.
    
    ---
    
    #### 🛡️ Expedition Support
    - Factory support mechanics and technicians with genuine spare parts backup.
    - Accompanying emergency medical doctors and oxygen equipment.
    - Strict pre-ride altitude acclimatization protocols.
    """)
    if st.button("Close", key="close_himalayan", type="primary"):
        st.rerun()

@st.dialog("🌍 One Ride Global")
def show_one_ride_dialog():
    st.markdown("### One Ride: Celebrating Global Brotherhood")
    st.markdown("""
    On a single Sunday in September, Royal Enfield riders across 60+ countries and 500+ cities ride out together in unity.
    
    ---
    
    #### 🌟 The Spirit of One Ride
    - **One Cause:** Riding in support of responsible travel, helmet safety, and environmental conservation.
    - **Global Footprint:** Over 25,000 riders in India, Europe, Latin America, Southeast Asia, and North America.
    - **Community Breakfast Rides:** Scenic morning rides organized by authorized dealerships and rider clubs.
    
    ---
    
    *Join your local dealership club for the upcoming One Ride.*
    """)
    if st.button("Close", key="close_oneride", type="primary"):
        st.rerun()

def render_rides():
    """Renders the Rides & Community section."""
    header_html = """
<div id="rides-community"></div>
<div id="rides"></div>
<div style="text-align: center; margin-top: 25px; margin-bottom: 25px;">
<h2 class="hero-text" style="font-size: 32px; font-weight: 900; letter-spacing: 2px; color: #ffffff; margin-bottom: 8px;">
RIDES & COMMUNITY
</h2>
<p style="color: #a0a0a0; font-size: 16px; max-width: 750px; margin: 0 auto; line-height: 1.5;">
Pure motorcycling is not just about the destination—it is a global brotherhood of explorers, legendary high-altitude expeditions, and community rides.
</p>
</div>
"""
    st.markdown("\n".join(l.strip() for l in header_html.splitlines() if l.strip()), unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        card1_html = """
<div style="background: rgba(25, 25, 25, 0.85); border: 1px solid #333; border-radius: 8px; padding: 22px 20px; text-align: center; min-height: 255px; box-shadow: 0 4px 15px rgba(0,0,0,0.3);">
<div style="font-size: 40px; margin-bottom: 12px;">🎪</div>
<h4 style="color: #ffffff; font-weight: 700; margin-bottom: 8px; font-size: 18px;">Motoverse (Rider Mania)</h4>
<div style="color: #e53935; font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 10px;">Vagator, Goa • Annual November</div>
<p style="color: #bbbbbb; font-size: 13.5px; line-height: 1.45; margin-bottom: 15px;">
The biggest 3-day festival of motorcycling, dirt-track racing, music, custom bikes, and coastal rides.
</p>
</div>
"""
        st.markdown("\n".join(l.strip() for l in card1_html.splitlines() if l.strip()), unsafe_allow_html=True)
        if st.button("Explore Motoverse", key="btn_motoverse", use_container_width=True):
            show_motoverse_dialog()

    with col2:
        card2_html = """
<div style="background: rgba(25, 25, 25, 0.85); border: 1px solid #333; border-radius: 8px; padding: 22px 20px; text-align: center; min-height: 255px; box-shadow: 0 4px 15px rgba(0,0,0,0.3);">
<div style="font-size: 40px; margin-bottom: 12px;">🏔️</div>
<h4 style="color: #ffffff; font-weight: 700; margin-bottom: 8px; font-size: 18px;">Himalayan Odyssey</h4>
<div style="color: #e53935; font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 10px;">18 Days • Over 2,200 km</div>
<p style="color: #bbbbbb; font-size: 13.5px; line-height: 1.45; margin-bottom: 15px;">
The ultimate mountain pilgrimage traversing the highest motorable passes on earth into Ladakh and Spiti.
</p>
</div>
"""
        st.markdown("\n".join(l.strip() for l in card2_html.splitlines() if l.strip()), unsafe_allow_html=True)
        if st.button("View Odyssey Details", key="btn_himalayan", use_container_width=True):
            show_himalayan_odyssey_dialog()

    with col3:
        card3_html = """
<div style="background: rgba(25, 25, 25, 0.85); border: 1px solid #333; border-radius: 8px; padding: 22px 20px; text-align: center; min-height: 255px; box-shadow: 0 4px 15px rgba(0,0,0,0.3);">
<div style="font-size: 40px; margin-bottom: 12px;">🌍</div>
<h4 style="color: #ffffff; font-weight: 700; margin-bottom: 8px; font-size: 18px;">One Ride Global</h4>
<div style="color: #e53935; font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 10px;">60+ Countries • 500+ Cities</div>
<p style="color: #bbbbbb; font-size: 13.5px; line-height: 1.45; margin-bottom: 15px;">
On one Sunday every September, thousands of riders worldwide take to the streets simultaneously in celebration.
</p>
</div>
"""
        st.markdown("\n".join(l.strip() for l in card3_html.splitlines() if l.strip()), unsafe_allow_html=True)
        if st.button("Discover One Ride", key="btn_oneride", use_container_width=True):
            show_one_ride_dialog()

    st.markdown("<br><hr style='border-color: #333;'>", unsafe_allow_html=True)
