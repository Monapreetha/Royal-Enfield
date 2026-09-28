import streamlit as st

def render_hero_section():
    """Renders the main hero banner, headline, and brand history."""
    
    # 1. Hero Banner Image
    st.image("assets/appealing_loft_hero_silver_text_1790475974062.jpg", use_container_width=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # 2. History & Quotes Section
    col1, spacer, col2 = st.columns([1.2, 0.2, 1])
    
    with col1:
        st.markdown("<h1 style='color: #cc0000; font-family: \"Arial Black\", Impact, sans-serif; margin-bottom: 20px;'>MADE LIKE A GUN</h1>", unsafe_allow_html=True)
        st.markdown("""
        <div style='font-size: 18px; line-height: 1.8; color: #ddd; font-family: \"Helvetica Neue\", sans-serif;'>
            <p>As the oldest global motorcycle brand in continuous production, Royal Enfield crafted its very first motorcycle in 1901. For over a century, we have been crafting timeless machines that have forged their own path.</p>
            <p>From serving on the battlefields of two World Wars to conquering the rugged, unforgiving terrains of the Himalayas, our motorcycles have stood the test of time—proving their mettle through unwavering mechanical resilience and enduring character.</p>
            <p>Today, Royal Enfield continues to preserve the legacy of simple, mechanical, and accessible motorcycles. We build machines that evoke the purest joy of motorcycling, fostering a community of riders bound by their love for the open road.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        # Quotes presented in stylish dark cards
        st.markdown("""
        <div style='background-color: #111; padding: 25px; border-left: 4px solid #cc0000; border-radius: 4px; margin-top: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.3);'>
            <h4 style='font-style: italic; font-weight: 400; color: #fff; line-height: 1.5; font-size: 19px;'>
            "We don't build motorcycles for people to just look at. We build them to be ridden. To create stories. To find new horizons."
            </h4>
            <p style='text-align: right; color: #888; font-size: 14px; margin-bottom: 0; margin-top: 15px;'>- Siddhartha Lal, Managing Director</p>
        </div>
        
        <br>
        
        <div style='background-color: #111; padding: 25px; border-left: 4px solid #c4d600; border-radius: 4px; box-shadow: 0 4px 6px rgba(0,0,0,0.3);'>
            <h4 style='font-style: italic; font-weight: 400; color: #fff; line-height: 1.5; font-size: 19px;'>
            "It is not just a machine, it is an emotion. It is the rhythmic thud-thud of the engine that echoes the heartbeat of millions."
            </h4>
            <p style='text-align: right; color: #888; font-size: 14px; margin-bottom: 0; margin-top: 15px;'>- The Royal Enfield Community</p>
        </div>
        """, unsafe_allow_html=True)
        
    st.markdown("<br><hr>", unsafe_allow_html=True)
