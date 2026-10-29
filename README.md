# 🏍️ Royal Enfield Digital Showroom

An interactive, modern digital showroom prototype for **Royal Enfield**, built with Python and Streamlit. This application simulates the official Royal Enfield online experience with cinematic hero sliders, dynamic motorcycle showcases, interactive pan-India dealership locator, test ride booking, and official ownership resources.

---

## 🌟 Key Features

1. **Cinematic Multi-Scene Hero Slider:**
   - Overlaid navigation arrows directly inside the visual canvas.
   - 4 switchable scenic atmospheres:
     - 🏙️ **Urban Heritage** (*Classic 350*)
     - 🏔️ **Himalayan Expedition** (*All-New Himalayan 450*)
     - 🛣️ **Coastal Cruiser** (*Super Meteor 650*)
     - 🏁 **Cafe Racer Circuit** (*Continental GT 650*)
   - In-picture action buttons and instant motorcycle pre-selection.

2. **Complete Motorcycle Lineup:**
   - Categorized showcases across Cruisers, Roadsters, Adventure, and Custom & Cafe.
   - Comprehensive technical specs (displacement, power, torque, estimated ex-showroom pricing).

3. **Interactive Dealership Locator:**
   - Real-time interactive map and directory covering major metropolitan hubs and service centers across India (Chennai, Mumbai, Delhi, Bengaluru, Hyderabad).

4. **Experience The Ride (Test Ride Booking):**
   - Streamlined test ride reservation flow with instant confirmation and reference ID generation.

5. **Ownership & Legal Resource Modals:**
   - Interactive dialogs for *Book a Service*, *Owner's Manuals*, and *Make It Yours (MIY)* customization.
   - Dedicated dialog modals for *Privacy Policy*, *Terms & Conditions*, *Disclaimer*, and *Cookie Policy*.

---

## 🚀 Getting Started

### 1. Installation
Clone this repository and install the dependencies:

```bash
git clone https://github.com/Monapreetha/Royal-Enfield.git
cd Royal-Enfield
pip install -r requirements.txt
```

### 2. Run the Digital Showroom
Launch the Streamlit web application:

```bash
streamlit run app.py
```

The application will automatically open in your default browser at `http://localhost:8501`.

---

## 📂 Project Structure

```
├── assets/                 # High-definition motorcycle imagery & hero banners
├── components/             # Modular Streamlit UI components
│   ├── navbar.py           # Fixed top brand navigation bar
│   ├── hero.py             # In-picture interactive hero slider & brand history
│   ├── showcase.py         # Categorized motorcycle showcase gallery
│   ├── locations.py        # Dealership directory & map
│   ├── booking_form.py     # Test ride reservation form
│   ├── services_info.py    # Ownership services & benefits
│   └── footer.py           # Quick actions, contact details & legal modals
├── services/               # Backend business logic & booking handlers
├── .gitignore              # Git ignore rules for clean repository
├── app.py                  # Main Streamlit application entry point
├── requirements.txt        # Python library dependencies
└── README.md               # Project documentation
```

---

## 🛠️ Built With
- **Python 3.10+**
- **Streamlit** (Web framework)
- **Pandas & NumPy** (Data processing)
