import streamlit as st

def render_showcase():
    """Renders the complete motorcycle gallery showcase categorized by tabs."""
    st.markdown("<h2 class='hero-text'>THE MOTORCYCLES</h2>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    # Organized categories
    categories = {
        "Cruisers": [
            {
                "name": "METEOR 350",
                "desc": "The quintessential easy cruiser for the open road.",
                "img": "assets/meteor_350_1790442144202.jpg",
                "specs": """**Engine:** 349cc, Single Cylinder\n**Power:** 20.2 bhp\n**Torque:** 27 Nm\n**Price:** ₹2,05,000"""
            },
            {
                "name": "SUPER METEOR 650",
                "desc": "The ultimate highway cruiser. Authentic and majestic.",
                "img": "assets/super_meteor_650_1790442171925.jpg",
                "specs": """**Engine:** 648cc, Parallel Twin\n**Power:** 47 bhp\n**Torque:** 52.3 Nm\n**Price:** ₹3,63,000"""
            },
            {
                "name": "CLASSIC 350",
                "desc": "Timeless styling meets modern reliability. A true legend.",
                "img": "assets/classic_350_1789794223429.jpg",
                "specs": """**Engine:** 349cc, Single Cylinder\n**Power:** 20.2 bhp\n**Torque:** 27 Nm\n**Price:** ₹1,93,000"""
            }
        ],
        "Roadsters": [
            {
                "name": "HUNTER 350",
                "desc": "A shot of motorcycling pureness. Compact, agile, urban.",
                "img": "assets/hunter_350_1790442132376.jpg",
                "specs": """**Engine:** 349cc, Single Cylinder\n**Power:** 20.2 bhp\n**Torque:** 27 Nm\n**Price:** ₹1,49,000"""
            },
            {
                "name": "INTERCEPTOR 650",
                "desc": "A modern classic roadster, inspired by the 60s twin.",
                "img": "assets/interceptor_650_1790442156809.jpg",
                "specs": """**Engine:** 648cc, Parallel Twin\n**Power:** 47 bhp\n**Torque:** 52 Nm\n**Price:** ₹3,03,000"""
            },
            {
                "name": "BULLET 350",
                "desc": "The iconic thumper. A symbol of resilience since 1932.",
                "img": "assets/bullet_350_1790442119499.jpg",
                "specs": """**Engine:** 349cc, J-series\n**Power:** 20.2 bhp\n**Torque:** 27 Nm\n**Price:** ₹1,73,000"""
            }
        ],
        "Adventure": [
            {
                "name": "HIMALAYAN",
                "desc": "Built for all roads, and no roads. Your adventure awaits.",
                "img": "assets/himalayan_1789794268326.jpg",
                "specs": """**Engine:** 452cc, Liquid Cooled\n**Power:** 40 bhp\n**Torque:** 40 Nm\n**Price:** ₹2,85,000"""
            }
        ],
        "Custom & Cafe": [
            {
                "name": "CONTINENTAL GT 650",
                "desc": "The quintessential cafe racer. Pure rock 'n' roll.",
                "img": "assets/continental_gt_1789794244984.jpg",
                "specs": """**Engine:** 648cc, Parallel Twin\n**Power:** 47 bhp\n**Torque:** 52 Nm\n**Price:** ₹3,19,000"""
            },
            {
                "name": "SHOTGUN 650",
                "desc": "By custom, for custom. A stunning factory bobber.",
                "img": "assets/shotgun_650_1790442184939.jpg",
                "specs": """**Engine:** 648cc, Parallel Twin\n**Power:** 47 bhp\n**Torque:** 52.3 Nm\n**Price:** ₹3,59,000"""
            }
        ]
    }

    # Create the tabs
    tabs = st.tabs(list(categories.keys()))
    
    # Render content inside each tab
    for i, (cat_name, bikes) in enumerate(categories.items()):
        with tabs[i]:
            st.markdown("<br>", unsafe_allow_html=True)
            
            # Determine column layout based on number of bikes in category
            # We use a fixed 3-column grid to prevent single items from becoming massive
            cols = st.columns(3)
            
            for idx, bike in enumerate(bikes):
                with cols[idx]:
                    st.image(bike["img"], use_container_width=True)
                    st.markdown(f"<div class='model-title'>{bike['name']}</div>", unsafe_allow_html=True)
                    st.markdown(f"<div class='model-desc'>{bike['desc']}</div>", unsafe_allow_html=True)
                    
                    with st.expander(f"Explore Specs"):
                        st.markdown(bike["specs"])
            
            st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("---")
