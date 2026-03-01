# import streamlit as st

# # Import your pages
# import image_detect
# import mixed_cropping
# import crop_adviser

# # Sidebar navigation
# st.sidebar.title("📂 Navigation")
# page = st.sidebar.radio(
#     "Go to",
#     ["🏠 Home", "📊 Disease Detection", "📈 Mixed Cropping", "📝 Crop Advisor"]
# )

# # Home page
# def home():
#     st.title("🌱 Welcome to AgriSphere")
#     st.markdown(
#         """
#         ### 🚀 Smart Farming Assistant  
#         This application helps farmers with:
#         - 🌾 **Crop Disease Diagnosis** - upload an image and get treatment suggestions  
#         - 📍 **Location-based Crop Recommendations** - profitable crops based on soil & climate  
#         - ♻️ **Mixed Farming Guidance** - increase yield with sustainable practices  

#         ---
#         **Use the sidebar** 👉 to navigate between different sections.
#         """
#     )

#     st.info("Tip: Start by exploring the **Analysis Page** to see sample insights!")

#     # Quick link buttons (like shortcuts)
#     col1, col2, col3 = st.columns(3)
#     with col1:
#         if st.button("📊 Go to Analysis"):
#             st.session_state["page"] = "📊 Disease Detection"
#     with col2:
#         if st.button("📈 Go to Dashboard"):
#             st.session_state["page"] = "📈 Mixed Cropping"
#     with col3:
#         if st.button("📝 Go to Reports"):
#             st.session_state["page"] = "📝 Crop Advisor"


# # Routing logic
# if "page" in st.session_state:
#     page = st.session_state["page"]

# if page == "🏠 Home":
#     home()
# elif page == "📊 Disease Detection":
#     image_detect.app1()
# elif page == "📈 Mixed Cropping":
#     mixed_cropping.app()
# elif page == "📝 Crop Advisor":
#     crop_adviser.app()





import streamlit as st
# Import your pages
import image_detect
import mixed_cropping
import crop_adviser
import govt

# Page configuration
st.set_page_config(
    page_title="🌱 AgriSphere - Smart Farming Platform",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for agricultural homepage
st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&family=Inter:wght@300;400;500;600&display=swap');
    
    /* Main background and font */
    .stApp {
        background: linear-gradient(135deg, #e8f5e8 0%, #f0f9f0 30%, #ffffff 70%, #e8f5e8 100%);
        font-family: 'Poppins', sans-serif;
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background: linear-gradient(180deg, #f8fdf8 0%, #e8f5e8 100%) !important;
    }
    
    .css-1d391kg .stSelectbox label,
    .css-1d391kg .stRadio label {
        color: #2d5016 !important;
        font-weight: 600 !important;
    }
    
    /* Radio button styling in sidebar */
    .stRadio > div > label > div:first-child {
        background-color: #4a7c59 !important;
    }
    
    /* Hero Section */
    .hero-section {
        background: linear-gradient(135deg, #1a3a0f 0%, #2d5016 30%, #4a7c59 100%);
        padding: 4rem 2rem;
        border-radius: 20px;
        color: white;
        text-align: center;
        margin-bottom: 3rem;
        box-shadow: 0 20px 60px rgba(45, 80, 22, 0.3);
        position: relative;
        overflow: hidden;
    }
    
    .hero-section::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><circle cx="25" cy="25" r="2" fill="rgba(255,255,255,0.1)"/><circle cx="75" cy="75" r="3" fill="rgba(255,255,255,0.05)"/><circle cx="80" cy="20" r="1.5" fill="rgba(255,255,255,0.08)"/><circle cx="20" cy="80" r="2.5" fill="rgba(255,255,255,0.06)"/></svg>') repeat;
        pointer-events: none;
    }
    
    .hero-content {
        position: relative;
        z-index: 2;
    }
    
    .hero-section h1 {
        font-size: 3.5rem;
        font-weight: 800;
        margin: 0 0 1rem 0;
        text-shadow: 3px 3px 6px rgba(0,0,0,0.3);
    }
    
    .hero-subtitle {
        font-size: 1.4rem;
        margin: 1rem 0 2rem 0;
        opacity: 0.95;
        font-weight: 400;
        line-height: 1.6;
    }
    
    .hero-stats {
        display: flex;
        justify-content: center;
        gap: 3rem;
        margin-top: 2rem;
        flex-wrap: wrap;
    }
    
    .stat-item {
        text-align: center;
    }
    
    .stat-number {
        font-size: 2.5rem;
        font-weight: 700;
        color: #a8d8a8;
        display: block;
    }
    
    .stat-label {
        font-size: 0.9rem;
        opacity: 0.8;
        margin-top: 0.5rem;
    }
    
    /* Feature description section */
    .features-section {
        background: rgba(255, 255, 255, 0.9);
        padding: 2.5rem;
        border-radius: 15px;
        box-shadow: 0 8px 30px rgba(0,0,0,0.1);
        border: 2px solid #e8f5e8;
        margin: 2rem 0;
        backdrop-filter: blur(10px);
    }
    
    .section-header {
        color: #2d5016;
        font-weight: 700;
        font-size: 1.8rem;
        margin-bottom: 1.5rem;
        text-align: center;
        border-bottom: 3px solid #4a7c59;
        padding-bottom: 0.5rem;
    }
    
    .feature-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 2rem;
        margin: 2rem 0;
    }
    
    .feature-card {
        background: white;
        border-radius: 15px;
        padding: 2rem;
        box-shadow: 0 8px 25px rgba(0,0,0,0.1);
        border-left: 5px solid #4a7c59;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    
    .feature-card::before {
        content: '';
        position: absolute;
        top: 0;
        right: 0;
        width: 60px;
        height: 60px;
        background: linear-gradient(135deg, #4a7c59, #2d5016);
        transform: rotate(45deg) translate(30px, -30px);
        opacity: 0.1;
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 35px rgba(45, 80, 22, 0.2);
    }
    
    .feature-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
        display: block;
    }
    
    .feature-title {
        font-size: 1.3rem;
        font-weight: 600;
        color: #2d5016;
        margin-bottom: 1rem;
    }
    
    .feature-description {
        color: #666;
        line-height: 1.6;
        margin-bottom: 1rem;
    }
    
    .feature-benefits {
        list-style: none;
        padding: 0;
        margin: 0;
    }
    
    .feature-benefits li {
        padding: 0.3rem 0;
        color: #4a7c59;
        font-size: 0.9rem;
    }
    
    .feature-benefits li::before {
        content: '✓';
        color: #28a745;
        font-weight: bold;
        margin-right: 0.5rem;
    }
    
    /* Quick action buttons */
    .quick-actions {
        margin: 2rem 0;
    }
    
    .stButton > button {
        background: linear-gradient(45deg, #4a7c59, #2d5016) !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 1rem 2rem !important;
        font-weight: 600 !important;
        font-size: 1.1rem !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 6px 20px rgba(74, 124, 89, 0.3) !important;
        width: 100% !important;
        height: 60px !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-3px) !important;
        box-shadow: 0 8px 25px rgba(74, 124, 89, 0.4) !important;
    }
    
    /* Info box styling */
    .info-box {
        background: linear-gradient(45deg, #d4edda, #c3e6cb);
        color: #155724;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #28a745;
        margin: 2rem 0;
        font-size: 1.1rem;
    }
    
    /* About section */
    .about-section {
        background: linear-gradient(135deg, #f8fdf8, #e8f5e8);
        padding: 3rem 2rem;
        border-radius: 15px;
        margin: 3rem 0;
        text-align: center;
    }
    
    .about-title {
        font-size: 2rem;
        font-weight: 700;
        color: #2d5016;
        margin-bottom: 1rem;
    }
    
    .about-text {
        font-size: 1.1rem;
        color: #666;
        line-height: 1.8;
        max-width: 800px;
        margin: 0 auto;
    }
    
    /* Navigation tips */
    .nav-tip {
        background: rgba(74, 124, 89, 0.1);
        border: 2px solid rgba(74, 124, 89, 0.2);
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
        color: #2d5016;
        font-weight: 500;
    }
    
    /* Responsive adjustments */
    @media (max-width: 768px) {
        .hero-section h1 {
            font-size: 2.5rem;
        }
        
        .hero-subtitle {
            font-size: 1.2rem;
        }
        
        .hero-stats {
            gap: 2rem;
        }
        
        .feature-grid {
            grid-template-columns: 1fr;
        }
    }
</style>
""", unsafe_allow_html=True)

# Sidebar navigation with enhanced styling
st.sidebar.markdown("""
<div style="text-align: center; padding: 1rem; background: linear-gradient(45deg, #4a7c59, #2d5016); border-radius: 10px; margin-bottom: 2rem;">
    <h2 style="color: white; margin: 0; font-size: 1.5rem;">🌾 AgriSphere</h2>
    <p style="color: rgba(255,255,255,0.8); margin: 0.5rem 0 0 0; font-size: 0.9rem;">Smart Farming Platform</p>
</div>
""", unsafe_allow_html=True)

st.sidebar.title("📂 Navigation")
page = st.sidebar.radio(
    "Choose your farming tool:",
    ["🏠 Home", "📊 Disease Detection", "📈 Mixed Cropping", "📝 Crop Advisor","📝 Government Schemes"],
    help="Select a tool to get started with smart farming"
)

# Add sidebar info
st.sidebar.markdown("""
---
### 💡 Quick Tips
- *Disease Detection*: Upload plant images for instant diagnosis
- *Mixed Cropping*: Get companion planting suggestions  
- *Crop Advisor*: Receive location-based recommendations

### 📞 Support
Need help? Our AI-powered tools are designed to be intuitive and user-friendly.
""")

# Home page function with enhanced design
def home():
    # Hero Section
    st.markdown("""
    <div class="hero-section">
        <div class="hero-content">
            <h1>🌱 Welcome to AgriSphere</h1>
            <div class="hero-subtitle">
                Empowering farmers with AI-driven insights for smarter, more profitable agriculture
            </div>
            <div class="hero-stats">
                <div class="stat-item">
                    <span class="stat-number">90%</span>
                    <div class="stat-label">Accuracy Rate</div>
                </div>
                <div class="stat-item">
                    <span class="stat-number">--</span>
                    <div class="stat-label">Farmers Helped</div>
                </div>
                <div class="stat-item">
                    <span class="stat-number">24/7</span>
                    <div class="stat-label">AI Support</div>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Features Overview Section
    st.markdown("---")
    
    # Section Header
    st.markdown("""
    <div style="text-align: center; color: #2d5016; font-weight: 700; font-size: 1.8rem; margin: 2rem 0; border-bottom: 3px solid #4a7c59; padding-bottom: 0.5rem;">
        🚀 Smart Farming Solutions
    </div>
    """, unsafe_allow_html=True)
    
    # Create three columns for features
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div style="background: white; border-radius: 15px; padding: 2rem; box-shadow: 0 8px 25px rgba(0,0,0,0.1); border-left: 5px solid #4a7c59; margin: 1rem 0; text-align: center;">
            <div style="font-size: 3rem; margin-bottom: 1rem;">🔬</div>
            <h3 style="color: #2d5016; margin-bottom: 1rem;">Disease Detection & Treatment</h3>
            <p style="color: #666; line-height: 1.6; margin-bottom: 1rem;">
                Upload plant images and get instant AI-powered disease diagnosis with personalized treatment plans.
            </p>
            <ul style="list-style: none; padding: 0; color: #4a7c59; font-size: 0.9rem;">
                <li>✓ Instant image analysis</li>
                <li>✓ Treatment recommendations</li>
                <li>✓ Multi-language support</li>
                <li>✓ Disease stage identification</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="background: white; border-radius: 15px; padding: 2rem; box-shadow: 0 8px 25px rgba(0,0,0,0.1); border-left: 5px solid #4a7c59; margin: 1rem 0; text-align: center;">
            <div style="font-size: 3rem; margin-bottom: 1rem;">🌾</div>
            <h3 style="color: #2d5016; margin-bottom: 1rem;">Mixed Cropping Advisor</h3>
            <p style="color: #666; line-height: 1.6; margin-bottom: 1rem;">
                Discover the best companion plants and sustainable farming practices to maximize your harvest yield.
            </p>
            <ul style="list-style: none; padding: 0; color: #4a7c59; font-size: 0.9rem;">
                <li>✓ Companion planting guide</li>
                <li>✓ Soil optimization tips</li>
                <li>✓ Sustainable practices</li>
                <li>✓ Yield improvement strategies</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style="background: white; border-radius: 15px; padding: 2rem; box-shadow: 0 8px 25px rgba(0,0,0,0.1); border-left: 5px solid #4a7c59; margin: 1rem 0; text-align: center;">
            <div style="font-size: 3rem; margin-bottom: 1rem;">💰</div>
            <h3 style="color: #2d5016; margin-bottom: 1rem;">Profitable Crop Recommendations</h3>
            <p style="color: #666; line-height: 1.6; margin-bottom: 1rem;">
                Get location-specific crop suggestions based on soil conditions, climate data, and market profitability.
            </p>
            <ul style="list-style: none; padding: 0; color: #4a7c59; font-size: 0.9rem;">
                <li>✓ Location-based analysis</li>
                <li>✓ Profitability forecasting</li>
                <li>✓ Weather integration</li>
                <li>✓ Soil compatibility check</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div style="background: white; border-radius: 15px; padding: 2rem; box-shadow: 0 8px 25px rgba(0,0,0,0.1); border-left: 5px solid #4a7c59; margin: 1rem 0; text-align: center;">
            <div style="font-size: 3rem; margin-bottom: 1rem;">💰</div>
            <h3 style="color: #2d5016; margin-bottom: 1rem;">Government Schemes Recommendations</h3>
            <p style="color: #666; line-height: 1.6; margin-bottom: 1rem;">
                Get location-specific government scheme suggestions.
            </p>
            <ul style="list-style: none; padding: 0; color: #4a7c59; font-size: 0.9rem;">
                <li>✓ Location-based analysis</li>
                <li>✓ Government Scheme Name</li>
                <li>✓ Benefits </li>
                <li>✓ Official Website Links</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)    
    
    # Navigation tip
    st.markdown("""
    <div class="nav-tip">
        💡 <strong>Getting Started:</strong> Use the sidebar navigation to explore our farming tools. 
        Each tool is designed to provide instant, actionable insights for your agricultural needs.
    </div>
    """, unsafe_allow_html=True)
    
    # Quick action buttons
    st.markdown('<div class="section-header">⚡ Quick Access</div>', unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("🔬 Disease Detection", help="Upload plant images for instant diagnosis"):
            st.session_state["page"] = "📊 Disease Detection"
            st.experimental_rerun()
    
    with col2:
        if st.button("🌾 Mixed Cropping", help="Get companion planting recommendations"):
            st.session_state["page"] = "📈 Mixed Cropping"
            st.experimental_rerun()
    
    with col3:
        if st.button("💰 Crop Advisor", help="Find profitable crops for your area"):
            st.session_state["page"] = "📝 Crop Advisor"
            st.experimental_rerun()

    with col4:
        if st.button("💰 Government Schemes", help="Find government schemes according to state"):
            st.session_state["page"] = "📝 Government Schemes"
            st.experimental_rerun()        
    
    # Info box
    st.markdown("""
    <div class="info-box">
        🌟 <strong>Pro Tip:</strong> Start by exploring the Disease Detection tool to see how our AI can help identify and treat plant diseases instantly. 
        Our advanced computer vision technology provides accurate results in seconds!
    </div>
    """, unsafe_allow_html=True)
    
    # About section
    st.markdown("""
    <div class="about-section">
        <div class="about-title">🌍 Revolutionizing Agriculture with AI</div>
        <div class="about-text">
            AgriSphere combines cutting-edge artificial intelligence with decades of agricultural expertise to provide 
            farmers with instant, actionable insights. From disease detection to crop recommendations, our platform 
            empowers you to make data-driven decisions that increase yield, reduce costs, and promote sustainable farming practices.
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Footer stats
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666; padding: 2rem;">
        <div style="display: flex; justify-content: center; gap: 3rem; flex-wrap: wrap; margin-bottom: 1rem;">
            <div><strong>🎯 90% Accuracy</strong><br><small>Disease Detection</small></div>
            <div><strong>⚡ Instant Results</strong><br><small>Real-time Analysis</small></div>
            <div><strong>🌐 Multi-language</strong><br><small>10+ Languages</small></div>
            <div><strong>📱 Easy to Use</strong><br><small>No Training Required</small></div>
        </div>
        <p><strong>🌱 AgriSphere</strong> - Where Technology Meets Agriculture</p>
    </div>
    """, unsafe_allow_html=True)

# Routing logic with session state handling
if "page" in st.session_state:
    page = st.session_state["page"]

# Page routing
if page == "🏠 Home":
    home()
elif page == "📊 Disease Detection":
    image_detect.app1()
elif page == "📈 Mixed Cropping":
    mixed_cropping.app()
elif page == "📝 Crop Advisor":
    crop_adviser.app()
elif page == "📝 Government Schemes":
    govt.app()
