import streamlit as st
import streamlit.components.v1 as components
import base64
import os

@st.cache_data
def get_image_base64(filepath: str) -> str:
    """Reads and base64 encodes an image with caching for fast, smooth loading."""
    if not os.path.isabs(filepath):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        candidate = os.path.join(base_dir, filepath)
        if os.path.exists(candidate):
            filepath = candidate
    with open(filepath, "rb") as f:
        encoded = base64.b64encode(f.read()).decode("utf-8")
    return f"data:image/jpeg;base64,{encoded}"

def render_hero_section():
    """Renders the cinematic in-picture hero slider and brand history."""

    # 1. Load base64 encoded images
    urban_img = get_image_base64("assets/appealing_loft_hero_silver_text_1790475974062.jpg")
    himalayan_img = get_image_base64("assets/hero_himalayan_pass_1793285980006.jpg")
    cruiser_img = get_image_base64("assets/hero_coastal_cruiser_1793286002785.jpg")
    cafe_img = get_image_base64("assets/hero_cafe_racer_1793286026679.jpg")

    # 2. In-Picture Interactive Slider HTML/CSS/JS
    slider_html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <style>
        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}
        body {{
            background: transparent;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            overflow: hidden;
            user-select: none;
        }}
        .hero-slider {{
            position: relative;
            width: 100%;
            height: 560px;
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 15px 35px rgba(0,0,0,0.6);
            background-color: #0d0d0d;
        }}
        .slides-wrapper {{
            position: relative;
            width: 100%;
            height: 100%;
        }}
        .slide {{
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            opacity: 0;
            visibility: hidden;
            transition: opacity 0.65s cubic-bezier(0.4, 0, 0.2, 1), transform 0.65s cubic-bezier(0.4, 0, 0.2, 1);
            transform: scale(1.02);
        }}
        .slide.active {{
            opacity: 1;
            visibility: visible;
            transform: scale(1);
        }}
        .slide img {{
            width: 100%;
            height: 100%;
            object-fit: cover;
            object-position: center;
            display: block;
        }}
        .slide-overlay {{
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: linear-gradient(180deg, rgba(0,0,0,0.1) 0%, rgba(0,0,0,0.3) 45%, rgba(0,0,0,0.85) 100%),
                        linear-gradient(90deg, rgba(0,0,0,0.7) 0%, rgba(0,0,0,0.2) 55%, transparent 100%);
            pointer-events: none;
        }}
        .slide-content {{
            position: absolute;
            bottom: 45px;
            left: 55px;
            max-width: 650px;
            z-index: 10;
            color: #ffffff;
        }}
        .slide-badge {{
            display: inline-block;
            background: rgba(204, 0, 0, 0.9);
            color: #ffffff;
            padding: 5px 12px;
            border-radius: 4px;
            font-size: 11px;
            font-weight: 800;
            letter-spacing: 2px;
            text-transform: uppercase;
            margin-bottom: 10px;
            box-shadow: 0 2px 10px rgba(204,0,0,0.4);
            backdrop-filter: blur(4px);
        }}
        .slide-title {{
            font-family: 'Arial Black', Impact, sans-serif;
            font-size: 42px;
            font-weight: 900;
            letter-spacing: 1.5px;
            line-height: 1.1;
            margin-bottom: 10px;
            color: #ffffff;
            text-transform: uppercase;
            text-shadow: 0 3px 14px rgba(0,0,0,0.9);
        }}
        .slide-subtitle {{
            font-size: 16px;
            line-height: 1.5;
            color: #e0e0e0;
            margin-bottom: 20px;
            text-shadow: 0 2px 8px rgba(0,0,0,0.9);
            font-weight: 400;
        }}
        .slide-cta {{
            display: flex;
            gap: 12px;
            align-items: center;
        }}
        .btn-primary {{
            background: #cc0000;
            color: #ffffff;
            padding: 11px 22px;
            border-radius: 4px;
            font-size: 12px;
            font-weight: 700;
            letter-spacing: 1.5px;
            text-transform: uppercase;
            text-decoration: none;
            transition: all 0.25s ease;
            box-shadow: 0 4px 15px rgba(204,0,0,0.4);
            display: inline-block;
        }}
        .btn-primary:hover {{
            background: #e60000;
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(204,0,0,0.6);
        }}
        .btn-secondary {{
            background: rgba(255,255,255,0.14);
            color: #ffffff;
            border: 1px solid rgba(255,255,255,0.35);
            padding: 11px 20px;
            border-radius: 4px;
            font-size: 12px;
            font-weight: 600;
            letter-spacing: 1px;
            text-transform: uppercase;
            text-decoration: none;
            backdrop-filter: blur(8px);
            transition: all 0.25s ease;
            display: inline-block;
        }}
        .btn-secondary:hover {{
            background: rgba(255,255,255,0.25);
            border-color: #ffffff;
            transform: translateY(-2px);
        }}
        /* Overlaid navigation arrows inside picture */
        .slider-arrow {{
            position: absolute;
            top: 50%;
            transform: translateY(-50%);
            width: 52px;
            height: 52px;
            border-radius: 50%;
            background: rgba(18, 18, 18, 0.45);
            border: 1px solid rgba(255, 255, 255, 0.25);
            color: #ffffff;
            font-size: 26px;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            backdrop-filter: blur(8px);
            transition: all 0.25s ease;
            z-index: 30;
            outline: none;
        }}
        .arrow-prev {{
            left: 20px;
        }}
        .arrow-next {{
            right: 20px;
        }}
        .slider-arrow:hover {{
            background: rgba(204, 0, 0, 0.9);
            border-color: #cc0000;
            transform: translateY(-50%) scale(1.1);
            box-shadow: 0 0 20px rgba(204,0,0,0.6);
        }}
        /* Dots indicator at the bottom right inside picture */
        .slider-dots {{
            position: absolute;
            bottom: 25px;
            right: 40px;
            display: flex;
            gap: 8px;
            z-index: 30;
        }}
        .dot {{
            width: 24px;
            height: 4px;
            border-radius: 2px;
            background: rgba(255,255,255,0.35);
            cursor: pointer;
            transition: all 0.3s ease;
        }}
        .dot.active {{
            width: 44px;
            background: #cc0000;
            box-shadow: 0 0 10px rgba(204,0,0,0.8);
        }}
    </style>
    </head>
    <body>

    <div class="hero-slider">
        <div class="slides-wrapper">
            <!-- Slide 1: Urban Heritage -->
            <div class="slide active">
                <img src="{urban_img}" alt="Urban Heritage">
                <div class="slide-overlay"></div>
                <div class="slide-content">
                    <div class="slide-badge">ESTD. 1901 • CLASSIC 350</div>
                    <h1 class="slide-title">URBAN HERITAGE</h1>
                    <p class="slide-subtitle">Timeless craftsmanship and unwavering character rooted in over a century of pure mechanical pedigree.</p>
                    <div class="slide-cta">
                        <a href="#experience-the-ride" target="_parent" class="btn-primary">Book Test Ride</a>
                        <a href="#the-motorcycles" target="_parent" class="btn-secondary">Explore Lineup</a>
                    </div>
                </div>
            </div>

            <!-- Slide 2: Himalayan Expedition -->
            <div class="slide">
                <img src="{himalayan_img}" alt="Himalayan Expedition">
                <div class="slide-overlay"></div>
                <div class="slide-content">
                    <div class="slide-badge">EXPEDITION READY • ALL-NEW HIMALAYAN</div>
                    <h1 class="slide-title">HIMALAYAN EXPEDITION</h1>
                    <p class="slide-subtitle">Built for all roads, and no roads. Conquer extreme altitudes, rugged gravel passes, and uncharted terrain.</p>
                    <div class="slide-cta">
                        <a href="#experience-the-ride" target="_parent" class="btn-primary">Book Test Ride</a>
                        <a href="#the-motorcycles" target="_parent" class="btn-secondary">Explore Lineup</a>
                    </div>
                </div>
            </div>

            <!-- Slide 3: Coastal Cruiser -->
            <div class="slide">
                <img src="{cruiser_img}" alt="Coastal Cruiser">
                <div class="slide-overlay"></div>
                <div class="slide-content">
                    <div class="slide-badge">HIGHWAY CRUISER • SUPER METEOR 650</div>
                    <h1 class="slide-title">COASTAL CRUISER</h1>
                    <p class="slide-subtitle">Effortless open highway cruising, relaxed ergonomics, and majestic low-slung cruiser stance at golden hour.</p>
                    <div class="slide-cta">
                        <a href="#experience-the-ride" target="_parent" class="btn-primary">Book Test Ride</a>
                        <a href="#the-motorcycles" target="_parent" class="btn-secondary">Explore Lineup</a>
                    </div>
                </div>
            </div>

            <!-- Slide 4: Cafe Racer Circuit -->
            <div class="slide">
                <img src="{cafe_img}" alt="Cafe Racer Circuit">
                <div class="slide-overlay"></div>
                <div class="slide-content">
                    <div class="slide-badge">AUTHENTIC CAFE RACER • CONTINENTAL GT 650</div>
                    <h1 class="slide-title">CAFE RACER CIRCUIT</h1>
                    <p class="slide-subtitle">Clip-on handlebars, sculpted cafe racer fuel tank, and raw British twin-cylinder racing character.</p>
                    <div class="slide-cta">
                        <a href="#experience-the-ride" target="_parent" class="btn-primary">Book Test Ride</a>
                        <a href="#the-motorcycles" target="_parent" class="btn-secondary">Explore Lineup</a>
                    </div>
                </div>
            </div>
        </div>

        <!-- Overlaid Left & Right Arrows in the Picture -->
        <button class="slider-arrow arrow-prev" onclick="changeSlide(-1)" aria-label="Previous slide">&#10094;</button>
        <button class="slider-arrow arrow-next" onclick="changeSlide(1)" aria-label="Next slide">&#10095;</button>

        <!-- Overlaid Slide Indicators -->
        <div class="slider-dots">
            <span class="dot active" onclick="goToSlide(0)"></span>
            <span class="dot" onclick="goToSlide(1)"></span>
            <span class="dot" onclick="goToSlide(2)"></span>
            <span class="dot" onclick="goToSlide(3)"></span>
        </div>
    </div>

    <script>
        let current = 0;
        const slides = document.querySelectorAll('.slide');
        const dots = document.querySelectorAll('.dot');
        const total = slides.length;

        function showSlide(index) {{
            if (index >= total) current = 0;
            else if (index < 0) current = total - 1;
            else current = index;

            slides.forEach((s, i) => s.classList.toggle('active', i === current));
            dots.forEach((d, i) => d.classList.toggle('active', i === current));
        }}

        function changeSlide(direction) {{
            showSlide(current + direction);
        }}

        function goToSlide(index) {{
            showSlide(index);
        }}

        // Keyboard arrow navigation
        window.addEventListener('keydown', (e) => {{
            if (e.key === 'ArrowLeft') changeSlide(-1);
            if (e.key === 'ArrowRight') changeSlide(1);
        }});
    </script>
    </body>
    </html>
    """

    components.html(slider_html, height=575)

    st.markdown("<br><br>", unsafe_allow_html=True)

    # 3. History & Quotes Section
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
