import streamlit as st

@st.dialog("📜 The Royal Enfield Heritage Timeline", width="large")
def show_heritage_timeline_dialog():
    st.markdown("### 125 Years of Unbroken Motorcycling Lineage")
    st.markdown("""
    Royal Enfield is the oldest motorcycle brand in continuous production in the world.
    
    ---
    
    #### 🕰️ Key Historic Milestones
    
    - **1901 — The First Motorcycle:**  
      Albert Eadie and Robert Walker Smith design the first motorized bicycle in Redditch, Worcestershire, England.
      
    - **1914 — World War I Service:**  
      Royal Enfield builds 6hp and 8hp sidecar rigs for ambulance and dispatch service across European fronts. The motto *"Made Like a Gun"* is born.
      
    - **1932 — The Birth of the Bullet:**  
      The legendary 'Bullet' is unveiled at the Olympia Motorcycle Show in London with its distinctive inclined engine and exposed valve gear.
      
    - **1948 — The First Swingarm Suspension:**  
      Royal Enfield pioneers swinging arm rear suspension in the Colmore Cup trials, revolutionizing motorcycle chassis handling forever.
      
    - **1955 — The Indian Journey Begins:**  
      The Indian government orders 800 Bullets for Indian Army border patrols. Madras Motors partners with Enfield to assemble motorcycles at Tiruvottiyur, Chennai.
      
    - **2018 — Return of the Parallel Twins:**  
      The Interceptor 650 and Continental GT 650 twin-cylinder motorcycles launch globally, winning international Motorcycle of the Year honors.
      
    - **Present Day — The Global Era:**  
      State-of-the-art Technology Centers at Bruntingthorpe Proving Ground (UK) and Chennai (India), delivering world-class motorcycles to riders across 60+ nations.
    """)
    if st.button("Close Timeline", key="close_timeline", type="primary"):
        st.rerun()

def render_heritage():
    """Renders the 125 Years of Heritage section."""
    header_html = """
<div id="our-heritage"></div>
<div id="heritage"></div>
<div style="text-align: center; margin-top: 25px; margin-bottom: 25px;">
<h2 class="hero-text" style="font-size: 32px; font-weight: 900; letter-spacing: 2px; color: #ffffff; margin-bottom: 8px;">
HERITAGE & CRAFTSMANSHIP
</h2>
<p style="color: #a0a0a0; font-size: 16px; max-width: 750px; margin: 0 auto; line-height: 1.5;">
Since 1901 — the world's oldest motorcycle brand in continuous production. An authentic legacy of resilient British engineering and Indian soul.
</p>
</div>
"""
    st.markdown("\n".join(l.strip() for l in header_html.splitlines() if l.strip()), unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        card1_html = """
<div style="background: rgba(25, 25, 25, 0.85); border: 1px solid #333; border-radius: 8px; padding: 22px 20px; text-align: center; min-height: 255px; box-shadow: 0 4px 15px rgba(0,0,0,0.3);">
<div style="font-size: 40px; margin-bottom: 12px;">🇬🇧</div>
<h4 style="color: #ffffff; font-weight: 700; margin-bottom: 8px; font-size: 18px;">1901: Redditch, England</h4>
<div style="color: #e53935; font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 10px;">The Legend Begins</div>
<p style="color: #bbbbbb; font-size: 13.5px; line-height: 1.45; margin-bottom: 15px;">
The iconic motto 'Made Like a Gun, Goes Like a Bullet' is born with precision rifle-parts engineering and early cycleframes.
</p>
</div>
"""
        st.markdown("\n".join(l.strip() for l in card1_html.splitlines() if l.strip()), unsafe_allow_html=True)

    with col2:
        card2_html = """
<div style="background: rgba(25, 25, 25, 0.85); border: 1px solid #333; border-radius: 8px; padding: 22px 20px; text-align: center; min-height: 255px; box-shadow: 0 4px 15px rgba(0,0,0,0.3);">
<div style="font-size: 40px; margin-bottom: 12px;">🇮🇳</div>
<h4 style="color: #ffffff; font-weight: 700; margin-bottom: 8px; font-size: 18px;">1955: Madras, India</h4>
<div style="color: #e53935; font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 10px;">Frontier Guardian</div>
<p style="color: #bbbbbb; font-size: 13.5px; line-height: 1.45; margin-bottom: 15px;">
The 350cc Bullet arrives to guard the high frontiers of the Himalayas, beginning an enduring love affair with Indian roads.
</p>
</div>
"""
        st.markdown("\n".join(l.strip() for l in card2_html.splitlines() if l.strip()), unsafe_allow_html=True)

    with col3:
        card3_html = """
<div style="background: rgba(25, 25, 25, 0.85); border: 1px solid #333; border-radius: 8px; padding: 22px 20px; text-align: center; min-height: 255px; box-shadow: 0 4px 15px rgba(0,0,0,0.3);">
<div style="font-size: 40px; margin-bottom: 12px;">⚙️</div>
<h4 style="color: #ffffff; font-weight: 700; margin-bottom: 8px; font-size: 18px;">Global Innovation</h4>
<div style="color: #e53935; font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 10px;">Bruntingthorpe & Chennai</div>
<p style="color: #bbbbbb; font-size: 13.5px; line-height: 1.45; margin-bottom: 15px;">
Dual Technology Centers uniting British design pedigree with Indian manufacturing precision to engineer modern twins.
</p>
</div>
"""
        st.markdown("\n".join(l.strip() for l in card3_html.splitlines() if l.strip()), unsafe_allow_html=True)

    # Center Button for Full Timeline Dialog
    b_col1, b_col2, b_col3 = st.columns([1, 2, 1])
    with b_col2:
        if st.button("📖 Explore 125-Year Heritage Timeline", key="btn_heritage_timeline", use_container_width=True):
            show_heritage_timeline_dialog()

    st.markdown("<br><hr style='border-color: #333;'>", unsafe_allow_html=True)
