import streamlit as st
import requests
import os
from dotenv import load_dotenv
from gcrew import get_farmer_schemes

load_dotenv()

def app():

# Page configuration
    st.set_page_config(
        page_title="🌾 Farmer Government Scheme Finder",
        page_icon="🏛️",
        layout="wide"
    )

    # Custom CSS matching your main app style
    st.markdown("""
    <style>
        /* Import Google Fonts */
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&family=Inter:wght@300;400;500;600&display=swap');
        
        /* Main background and font */
        .stApp {
            background: linear-gradient(135deg, #e8f5e8 0%, #f0f9f0 30%, #ffffff 70%, #e8f5e8 100%);
            font-family: 'Poppins', sans-serif;
        }
        
        /* Hero Section */
        .hero-section {
            background: linear-gradient(135deg, #1a3a0f 0%, #2d5016 30%, #4a7c59 100%);
            padding: 3rem 2rem;
            border-radius: 20px;
            color: white;
            text-align: center;
            margin-bottom: 2rem;
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
            font-size: 2.8rem;
            font-weight: 800;
            margin: 0 0 1rem 0;
            text-shadow: 3px 3px 6px rgba(0,0,0,0.3);
        }
        
        .hero-subtitle {
            font-size: 1.2rem;
            margin: 1rem 0;
            opacity: 0.95;
            font-weight: 400;
            line-height: 1.6;
        }
        
        /* Main content card */
        .content-card {
            background: rgba(255, 255, 255, 0.95);
            padding: 2.5rem;
            border-radius: 15px;
            box-shadow: 0 8px 30px rgba(0,0,0,0.1);
            border: 2px solid #e8f5e8;
            margin: 2rem 0;
            backdrop-filter: blur(10px);
        }
        
        /* Form section styling */
        .form-section {
            background: white;
            padding: 2rem;
            border-radius: 12px;
            border-left: 5px solid #4a7c59;
            box-shadow: 0 4px 15px rgba(0,0,0,0.08);
            margin: 1.5rem 0;
        }
        
        .section-header {
            color: #2d5016;
            font-weight: 700;
            font-size: 1.5rem;
            margin-bottom: 1rem;
            border-bottom: 2px solid #4a7c59;
            padding-bottom: 0.5rem;
        }
        
        /* Location detection styling */
        .location-info {
            background: linear-gradient(45deg, #d4edda, #c3e6cb);
            color: #155724;
            padding: 1.5rem;
            border-radius: 10px;
            border-left: 5px solid #28a745;
            margin: 1.5rem 0;
            display: flex;
            align-items: center;
            gap: 1rem;
        }
        
        .location-icon {
            font-size: 2rem;
        }
        
        .location-text {
            flex: 1;
        }
        
        .location-state {
            font-size: 1.3rem;
            font-weight: 600;
            margin-top: 0.5rem;
        }
        
        /* Error styling */
        .error-box {
            background: linear-gradient(45deg, #f8d7da, #f5c6cb);
            color: #721c24;
            padding: 1.5rem;
            border-radius: 10px;
            border-left: 5px solid #dc3545;
            margin: 1.5rem 0;
            display: flex;
            align-items: center;
            gap: 1rem;
        }
        
        /* Button styling */
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
            background: linear-gradient(45deg, #2d5016, #1a3a0f) !important;
        }
        
        /* Selectbox styling */
        .stSelectbox > div > div {
            background: white;
            border: 2px solid #e8f5e8;
            border-radius: 8px;
        }
        
        .stSelectbox > div > div:focus-within {
            border-color: #4a7c59;
            box-shadow: 0 0 0 2px rgba(74, 124, 89, 0.2);
        }
        
        /* Results section */
        .results-section {
            background: linear-gradient(135deg, #f8fdf8, #e8f5e8);
            padding: 2rem;
            border-radius: 15px;
            margin: 2rem 0;
            border: 2px solid #4a7c59;
        }
        
        .results-header {
            color: #2d5016;
            font-size: 1.8rem;
            font-weight: 700;
            margin-bottom: 1.5rem;
            text-align: center;
            border-bottom: 3px solid #4a7c59;
            padding-bottom: 0.5rem;
        }
        
        /* Info cards */
        .info-card {
            background: white;
            padding: 1.5rem;
            border-radius: 10px;
            border-left: 4px solid #4a7c59;
            margin: 1rem 0;
            box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        }
        
        .info-card h4 {
            color: #2d5016;
            margin-bottom: 0.5rem;
            font-weight: 600;
        }
        
        .info-card p {
            color: #666;
            margin: 0;
            line-height: 1.5;
        }
        
        /* Features grid */
        .features-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 1.5rem;
            margin: 2rem 0;
        }
        
        .feature-item {
            background: white;
            padding: 1.5rem;
            border-radius: 10px;
            text-align: center;
            border: 1px solid #e8f5e8;
            transition: all 0.3s ease;
        }
        
        .feature-item:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 20px rgba(74, 124, 89, 0.15);
        }
        
        .feature-icon {
            font-size: 2.5rem;
            margin-bottom: 1rem;
            display: block;
        }
        
        .feature-title {
            font-weight: 600;
            color: #2d5016;
            margin-bottom: 0.5rem;
        }
        
        .feature-desc {
            color: #666;
            font-size: 0.9rem;
            line-height: 1.4;
        }
        
        /* Responsive adjustments */
        @media (max-width: 768px) {
            .hero-section h1 {
                font-size: 2.2rem;
            }
            
            .hero-subtitle {
                font-size: 1rem;
            }
            
            .features-grid {
                grid-template-columns: 1fr;
            }
        }
    </style>
    """, unsafe_allow_html=True)

    # Hero Section
    st.markdown("""
    <div class="hero-section">
        <div class="hero-content">
            <h1>🏛️ Government Scheme Finder</h1>
            <div class="hero-subtitle">
                Discover government schemes and subsidies available for farmers in your state
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Main content
    st.markdown('<div class="content-card">', unsafe_allow_html=True)

    # Features overview
    st.markdown("""
    <div class="features-grid">
        <div class="feature-item">
            <span class="feature-icon">📍</span>
            <div class="feature-title">Auto Location Detection</div>
            <div class="feature-desc">Automatically detects your state using IP location</div>
        </div>
        <div class="feature-item">
            <span class="feature-icon">🌍</span>
            <div class="feature-title">Multi-language Support</div>
            <div class="feature-desc">Available in 10+ Indian languages</div>
        </div>
        <div class="feature-item">
            <span class="feature-icon">🤖</span>
            <div class="feature-title">AI-Powered Analysis</div>
            <div class="feature-desc">Smart recommendations based on your location</div>
        </div>
        <div class="feature-item">
            <span class="feature-icon">⚡</span>
            <div class="feature-title">Real-time Updates</div>
            <div class="feature-desc">Latest government schemes and policies</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Form section
    st.markdown('<div class="form-section">', unsafe_allow_html=True)
    st.markdown('<div class="section-header">🔧 Configuration</div>', unsafe_allow_html=True)

    # Language selection
    language = st.selectbox(
        "🌍 Select Output Language",
        ["English", "Hindi", "Marathi", "Telugu", "Bengali", "Tamil", "Gujarati", "Kannada", "Odia", "Punjabi"],
        help="Choose your preferred language for scheme information"
    )

    st.markdown('</div>', unsafe_allow_html=True)

    # Detect state from IP function
    def get_state_from_ip():
        try:
            ip = requests.get('https://api64.ipify.org').text
            response = requests.get(f'https://ipinfo.io/{ip}/json').json()
            return response.get('region', '')  # 'region' gives state
        except:
            return None

    # Location detection
    st.markdown('<div class="section-header">📍 Location Detection</div>', unsafe_allow_html=True)

    with st.spinner("🔍 Detecting your location..."):
        state = get_state_from_ip()

    if not state:
        st.markdown("""
        <div class="error-box">
            <span style="font-size: 2rem;">❌</span>
            <div>
                <strong>Location Detection Failed</strong><br>
                Could not detect your location from IP address. Please check your internet connection and try again.
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="location-info">
            <span class="location-icon">📍</span>
            <div class="location-text">
                <strong>Location Successfully Detected!</strong>
                <div class="location-state">{state}</div>
                <small>We'll find schemes specific to your state</small>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Action button
    st.markdown('<div style="margin: 2rem 0;">', unsafe_allow_html=True)
    if st.button("🔍 Find Government Schemes", disabled=not state):
        if state:
            with st.spinner("🤖 AI is analyzing government schemes for your state..."):
                try:
                    # Create progress bar
                    progress_bar = st.progress(0)
                    progress_text = st.empty()
                    
                    progress_text.text("🔍 Initializing AI crew...")
                    progress_bar.progress(25)
                    
                    
                    
                    progress_text.text("📊 Analyzing state-specific schemes...")
                    progress_bar.progress(50)
                    
                    progress_text.text("🌾 Generating personalized recommendations...")
                    progress_bar.progress(75)
                    
                    result = get_farmer_schemes(state, language)
                    
                    progress_text.text("✅ Analysis complete!")
                    progress_bar.progress(100)
                    
                    # Clear progress indicators
                    progress_bar.empty()
                    progress_text.empty()
                    
                    # Display results
                    st.markdown("""
                    <div class="results-section">
                        <div class="results-header">✅ Recommended Government Schemes</div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    st.markdown(result)
                    
                    # Success message
                    st.success("🎉 Scheme analysis completed successfully!")
                    
                except Exception as e:
                    st.error(f"❌ Error occurred while fetching schemes: {str(e)}")
                    st.info("💡 Please try again or contact support if the issue persists.")

    st.markdown('</div>', unsafe_allow_html=True)

    # Information cards
    st.markdown('<div class="section-header">ℹ️ How It Works</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="info-card">
            <h4>🎯 Personalized Recommendations</h4>
            <p>Our AI analyzes your state's specific agricultural policies and suggests the most relevant schemes for farmers in your area.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="info-card">
            <h4>🔄 Real-time Updates</h4>
            <p>We continuously update our database with the latest government announcements and policy changes to ensure accuracy.</p>
        </div>
        """, unsafe_allow_html=True)

    # Help section
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; padding: 2rem; background: linear-gradient(45deg, #f8fdf8, #e8f5e8); border-radius: 10px; margin: 2rem 0;">
        <h3 style="color: #2d5016; margin-bottom: 1rem;">💡 Need Help?</h3>
        <p style="color: #666; margin: 0;">
            If you're having trouble detecting your location or finding relevant schemes, 
            our AI will provide general farming schemes that apply across India.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)