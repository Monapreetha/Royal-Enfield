import streamlit as st

def render_navbar():
    """Renders a functional, modern fixed navigation bar with smooth section links and action CTA."""
    
    # Helper for smooth scrolling inside Streamlit's virtual scroll container
    def scroll_js(target_id: str) -> str:
        return (
            f"var el=document.getElementById('{target_id}');"
            "if(el){"
            "var m=document.querySelector('[data-testid=\"stMain\"]')||document.querySelector('section.main')||window;"
            "var mTop=m.getBoundingClientRect?m.getBoundingClientRect().top:0;"
            "var cur=(m.scrollTop!==undefined)?m.scrollTop:(window.pageYOffset||0);"
            "var dest=el.getBoundingClientRect().top-mTop+cur-85;"
            "if(m.scrollTo){m.scrollTo({top:Math.max(0,dest),behavior:'smooth'});}"
            "else{el.scrollIntoView({behavior:'smooth',block:'start'});}"
            "}"
            "return false;"
        )

    scroll_top_js = (
        "var m=document.querySelector('[data-testid=\"stMain\"]')||document.querySelector('section.main')||window;"
        "if(m.scrollTo){m.scrollTo({top:0,behavior:'smooth'});}"
        "else{window.scrollTo({top:0,behavior:'smooth'});}"
        "return false;"
    )

    navbar_html = f"""
<style>
html {{
    scroll-behavior: smooth;
}}
[id] {{
    scroll-margin-top: 85px;
}}
.custom-navbar {{
    background: rgba(18, 18, 18, 0.96);
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    height: 70px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 40px;
    z-index: 999999;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    border-bottom: 1px solid #333;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);
}}

/* Official Royal Enfield Wordmark Logo */
.nav-logo {{
    color: #cc0000;
    font-size: 26px;
    font-weight: 900;
    letter-spacing: 1px;
    font-family: 'Arial Black', Impact, sans-serif;
    cursor: pointer;
    text-decoration: none !important;
    border: none !important;
    border-bottom: none !important;
    outline: none !important;
    box-shadow: none !important;
    user-select: none;
    transition: color 0.2s ease;
}}
.nav-logo:hover {{
    color: #e60000;
}}

/* Navigation Links */
.nav-menu {{
    display: flex;
    align-items: center;
    gap: 28px;
    list-style: none;
    margin: 0;
    padding: 0;
}}
.nav-link {{
    color: #c7c7c7;
    text-decoration: none !important;
    font-size: 13px;
    font-weight: 600;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    position: relative;
    padding: 6px 0;
    border: none !important;
    outline: none !important;
    cursor: pointer;
    transition: color 0.25s ease;
}}
.nav-link:hover {{
    color: #ffffff;
}}
.nav-link::after {{
    content: '';
    position: absolute;
    width: 0%;
    height: 2px;
    bottom: 0;
    left: 0;
    background-color: #cc0000;
    transition: width 0.25s cubic-bezier(0.4, 0, 0.2, 1);
    border-radius: 2px;
}}
.nav-link:hover::after {{
    width: 100%;
}}

/* Action Button */
.nav-actions {{
    display: flex;
    align-items: center;
    gap: 15px;
}}
.nav-cta-btn {{
    background: linear-gradient(135deg, #cc0000 0%, #a80000 100%);
    color: #ffffff !important;
    text-decoration: none !important;
    padding: 9px 20px;
    border-radius: 4px;
    font-size: 12px;
    font-weight: 800;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    border: 1px solid rgba(255, 60, 60, 0.3) !important;
    box-shadow: 0 4px 14px rgba(204, 0, 0, 0.4);
    transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
    display: inline-flex;
    align-items: center;
    gap: 6px;
    cursor: pointer;
}}
.nav-cta-btn:hover {{
    background: linear-gradient(135deg, #e60000 0%, #cc0000 100%);
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(204, 0, 0, 0.65);
    border-color: rgba(255, 255, 255, 0.4) !important;
}}

/* Main container spacing so nothing is hidden behind fixed navbar */
.block-container {{
    padding-top: 85px !important; 
}}

/* Responsive */
@media (max-width: 960px) {{
    .nav-menu {{
        display: none;
    }}
    .custom-navbar {{
        padding: 0 20px;
    }}
}}
</style>

<div class="custom-navbar">
<div class="nav-logo" onclick="{scroll_top_js}">ROYAL ENFIELD</div>
<ul class="nav-menu">
<li><a href="#the-motorcycles" class="nav-link" onclick="{scroll_js('the-motorcycles')}">Motorcycles</a></li>
<li><a href="#find-a-dealership" class="nav-link" onclick="{scroll_js('find-a-dealership')}">Dealerships</a></li>
<li><a href="#ownership-services" class="nav-link" onclick="{scroll_js('ownership-services')}">Services</a></li>
<li><a href="#contact-us" class="nav-link" onclick="{scroll_js('contact-us')}">Contact</a></li>
</ul>
<div class="nav-actions">
<a href="#experience-the-ride" class="nav-cta-btn" onclick="{scroll_js('experience-the-ride')}"><span>🏍️ Book Test Ride</span></a>
</div>
</div>

"""
    clean_html = "\n".join(line.strip() for line in navbar_html.splitlines() if line.strip())
    st.markdown(clean_html, unsafe_allow_html=True)
