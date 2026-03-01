import streamlit as st
import requests
from fetch import get_weather, get_soil
from crop_profitability import get_crop_recommendations


def app():
    # ------------------------

    # Page configuration
    st.set_page_config(
        page_title="💰 Crop Profitability",
        page_icon="🌾",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # Custom CSS for agricultural theme
    st.markdown("""
    <style>
        /* Import Google Fonts */
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
        
        /* Main background and font */
        .stApp {
            background: linear-gradient(135deg, #e8f5e8 0%, #f0f9f0 50%, #ffffff 100%);
            font-family: 'Poppins', sans-serif;
        }
        
        /* Header styling */
        .main-header {
            background: linear-gradient(90deg, #2d5016 0%, #4a7c59 50%, #2d5016 100%);
            padding: 2rem;
            border-radius: 15px;
            color: white;
            text-align: center;
            margin-bottom: 2rem;
            box-shadow: 0 8px 32px rgba(45, 80, 22, 0.3);
        }
        
        .main-header h1 {
            font-size: 2.5rem;
            font-weight: 700;
            margin: 0;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }
        
        .main-header p {
            font-size: 1.2rem;
            margin: 0.5rem 0 0 0;
            opacity: 0.9;
        }
        
        /* Info container styling */
        .info-container {
            background: rgba(255, 255, 255, 0.9);
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.1);
            border: 2px solid #e8f5e8;
            margin-bottom: 1.5rem;
            backdrop-filter: blur(10px);
        }
        
        /* Section headers */
        .section-header {
            color: #2d5016;
            font-weight: 600;
            font-size: 1.3rem;
            margin-bottom: 1rem;
            border-left: 4px solid #4a7c59;
            padding-left: 1rem;
        }
        
        /* Location info styling */
        .location-info {
            background: linear-gradient(45deg, #e8f5e8, #d4edda);
            color: #2d5016;
            padding: 1rem;
            border-radius: 8px;
            border-left: 4px solid #4a7c59;
            margin: 1rem 0;
            font-weight: 500;
        }
        
        /* Error message styling */
        .error-message {
            background: linear-gradient(45deg, #f8d7da, #f5c6cb);
            color: #721c24;
            padding: 1rem;
            border-radius: 8px;
            border-left: 4px solid #dc3545;
            margin: 1rem 0;
        }
        
        /* Success message styling */
        .success-message {
            background: linear-gradient(45deg, #d4edda, #c3e6cb);
            color: #155724;
            padding: 1rem;
            border-radius: 8px;
            border-left: 4px solid #28a745;
            margin: 1rem 0;
        }
        
        /* Results container */
        .results-container {
            background: rgba(255, 255, 255, 0.95);
            border: 2px solid #d4edda;
            border-radius: 15px;
            padding: 2rem;
            margin-top: 2rem;
            box-shadow: 0 8px 25px rgba(0,0,0,0.1);
        }
        
        .results-header {
            color: #2d5016;
            font-weight: 700;
            font-size: 1.5rem;
            margin-bottom: 1rem;
            text-align: center;
            border-bottom: 3px solid #4a7c59;
            padding-bottom: 0.5rem;
        }
        
        /* Crop recommendations styling */
        .crop-recommendations {
            background: linear-gradient(45deg, #f0fff0, #e6f7ff);
            padding: 1.5rem;
            border-radius: 10px;
            border-left: 5px solid #4a7c59;
            margin: 1rem 0;
        }
        
        /* Feature cards */
        .feature-card {
            background: white;
            padding: 1.5rem;
            border-radius: 10px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.05);
            border-left: 5px solid #4a7c59;
            margin-bottom: 1rem;
        }
        
        .feature-title {
            color: #2d5016;
            font-weight: 600;
            font-size: 1.1rem;
            margin-bottom: 0.5rem;
        }
        
        .feature-desc {
            color: #666;
            line-height: 1.6;
        }
        
        /* Data cards */
        .data-card {
            background: white;
            padding: 1.5rem;
            border-radius: 10px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.05);
            border: 2px solid #e8f5e8;
            margin-bottom: 1rem;
            text-align: center;
        }
        
        .data-title {
            color: #2d5016;
            font-weight: 600;
            font-size: 1rem;
            margin-bottom: 0.5rem;
        }
        
        .data-value {
            color: #4a7c59;
            font-weight: 700;
            font-size: 1.2rem;
        }
        
        /* Loading animation */
        .loading-text {
            text-align: center;
            color: #4a7c59;
            font-weight: 500;
            animation: pulse 2s infinite;
        }
        
        @keyframes pulse {
            0% { opacity: 1; }
            50% { opacity: 0.5; }
            100% { opacity: 1; }
        }
        
        /* Auto-detection badge */
        .auto-badge {
            display: inline-block;
            background: linear-gradient(45deg, #4a7c59, #2d5016);
            color: white;
            padding: 0.3rem 0.8rem;
            border-radius: 20px;
            font-size: 0.9rem;
            font-weight: 500;
            margin-left: 1rem;
        }
        
        /* Progress styling */
        .stProgress > div > div {
            background-color: #4a7c59 !important;
        }
        
        /* Spinner customization */
        .stSpinner > div {
            border-top-color: #4a7c59 !important;
        }
        
        /* Sidebar styling */
        .css-1d391kg {
            background-color: #f8fdf8 !important;
        }
        
        /* Markdown content in results */
        .results-container h1, .results-container h2, .results-container h3 {
            color: #2d5016;
        }
        
        .results-container ul {
            margin-left: 1rem;
        }
        
        .results-container li {
            margin-bottom: 0.5rem;
            line-height: 1.6;
        }
    </style>
    """, unsafe_allow_html=True)

    # Main header
    st.markdown("""
    <div class="main-header">
        <h1>💰 Smart Crop Profitability Advisor</h1>
        <p>AI-powered crop suggestions based on your location, soil & weather data</p>
    </div>
    """, unsafe_allow_html=True)

    # Description with auto-detection info
    st.markdown("""
    <div class="info-container">
        <div class="section-header">🎯 How It Works</div>
        <p style="color: #666; font-size: 1.1rem; line-height: 1.6; margin-bottom: 0;">
            Our intelligent system automatically detects your location using your IP address, then analyzes local soil conditions and weather patterns to recommend the most profitable crops for your area.
        </p>
        <span class="auto-badge">🤖 Fully Automated</span>
    </div>
    """, unsafe_allow_html=True)

    # Detect city and coordinates from IP
    def get_location_from_ip():
        try:
            ip = requests.get('https://api64.ipify.org').text
            response = requests.get(f'https://ipinfo.io/{ip}/json').json()
            city = response.get('city', '')
            loc = response.get('loc', '')  # format "lat,lon"
            if loc:
                lat, lon = loc.split(',')
                return city, float(lat), float(lon)
            else:
                return city, None, None
        except:
            return None, None, None

    # Create layout columns
    col1, col2 = st.columns([2, 1])

    with col1:
        # Automatically detect location
        st.markdown('<div class="section-header">📍 Location Detection</div>', unsafe_allow_html=True)
        
        if st.button("🔍 Detect My Location and Recommend Crops"):
            with st.spinner("🌍 Detecting your location..."):
                city, lat, lon = get_location_from_ip()
            
            if not city or not lat or not lon:
                st.markdown("""
                <div class="error-message">
                    ❌ <strong>Location Detection Failed</strong><br>
                    Could not automatically detect your location from IP address. Please check your internet connection and try refreshing the page.
                </div>
                """, unsafe_allow_html=True)
            else:
                # Display detected location
                st.markdown(f"""
                <div class="location-info">
                    ✅ <strong>Location Successfully Detected!</strong><br>
                    📍 <strong>City:</strong> {city}<br>
                    🌐 <strong>Coordinates:</strong> {lat:.4f}°, {lon:.4f}°
                </div>
                """, unsafe_allow_html=True)
                
                # Start analysis
                st.markdown('<div class="section-header">🔄 Data Analysis in Progress</div>', unsafe_allow_html=True)
                
                # Progress bar for better UX
                progress_bar = st.progress(0)
                status_text = st.empty()
                
                try:
                    # Update progress: Fetching weather data
                    progress_bar.progress(25)
                    status_text.text("🌤️ Fetching weather data...")
                    weather = get_weather(lat=lat, lon=lon)
                    
                    # Update progress: Fetching soil data
                    progress_bar.progress(50)
                    status_text.text("🏔️ Analyzing soil conditions...")
                    soil = get_soil(lat=lat, lon=lon)
                    
                    # Update progress: Generating recommendations
                    progress_bar.progress(75)
                    status_text.text("🤖 Generating crop recommendations...")
                    md_crops = get_crop_recommendations(soil, weather, language="English")
                    
                    # Complete progress
                    progress_bar.progress(100)
                    status_text.text("✅ Analysis complete!")
                    
                    # Clear progress elements
                    progress_bar.empty()
                    status_text.empty()
                    
                    # Display results
                    st.markdown('<div class="results-container">', unsafe_allow_html=True)
                    st.markdown('<div class="results-header">🌾 Recommended Crops for Your Location</div>', unsafe_allow_html=True)
                    
                    # Success message
                    st.markdown("""
                    <div class="success-message">
                        🎉 <strong>Analysis Successful!</strong> Here are the most profitable crop recommendations for your area.
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Display crop recommendations in styled container
                    st.markdown('<div class="crop-recommendations">', unsafe_allow_html=True)
                    st.markdown(md_crops)
                    st.markdown('</div>', unsafe_allow_html=True)
                    
                    st.markdown('</div>', unsafe_allow_html=True)
                    
                except Exception as e:
                    # Clear progress elements on error
                    progress_bar.empty()
                    status_text.empty()
                    
                    st.markdown(f"""
                    <div class="error-message">
                        ❌ <strong>Data Fetch Error</strong><br>
                        Error fetching data for detected location '<strong>{city}</strong>': {str(e)}<br>
                        <small>Please try refreshing the page or check your internet connection.</small>
                    </div>
                    """, unsafe_allow_html=True)

    with col2:
        # Feature highlight cards
        st.markdown("""
        <div class="feature-card">
            <div class="feature-title">🎯 Auto-Location Detection</div>
            <div class="feature-desc">Automatically identifies your location using IP geolocation for precise recommendations.</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card">
            <div class="feature-title">🌤️ Real-time Weather Data</div>
            <div class="feature-desc">Analyzes current weather patterns and seasonal conditions for optimal crop timing.</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card">
            <div class="feature-title">🏔️ Soil Analysis</div>
            <div class="feature-desc">Evaluates soil composition, pH levels, and nutrient availability for crop compatibility.</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card">
            <div class="feature-title">💰 Profitability Focus</div>
            <div class="feature-desc">Recommendations prioritize crops with highest profit potential in your region.</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card">
            <div class="feature-title">⚡ Instant Results</div>
            <div class="feature-desc">Get comprehensive crop recommendations within seconds of loading the page.</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Data source info
        st.markdown("""
        <div class="data-card">
            <div class="data-title">📊 Data Sources</div>
            <div style="color: #666; font-size: 0.9rem; line-height: 1.5;">
                • Weather APIs<br>
                • Soil Database<br>
                • Market Analysis<br>
                • Regional Statistics
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666; padding: 1rem;">
        <p>💰 <strong>Smart Crop Profitability Advisor</strong> - Maximizing agricultural returns with data science</p>
        <p style="font-size: 0.9rem;">Powered by real-time weather and soil analytics 🌾</p>
    </div>
    """, unsafe_allow_html=True)