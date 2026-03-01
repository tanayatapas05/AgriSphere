import streamlit as st
from dotenv import load_dotenv
from crew import get_farming_practices
import os

# Load environment variables
load_dotenv()

def app():
    # Page configuration
    st.set_page_config(
        page_title="🌱 Farming Advisor",
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
        
        /* Input container styling */
        .input-container {
            background: rgba(255, 255, 255, 0.9);
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.1);
            border: 2px solid #e8f5e8;
            margin-bottom: 1.5rem;
            backdrop-filter: blur(10px);
        }
        
        /* Form section headers */
        .section-header {
            color: #2d5016;
            font-weight: 600;
            font-size: 1.3rem;
            margin-bottom: 1rem;
            border-left: 4px solid #4a7c59;
            padding-left: 1rem;
        }
        
        /* Input field styling */
        .stTextInput > div > div > input,
        .stTextArea > div > div > textarea,
        .stSelectbox > div > div > select {
            border: 2px solid #d4edda !important;
            border-radius: 8px !important;
            padding: 0.5rem !important;
            font-family: 'Poppins', sans-serif !important;
            transition: all 0.3s ease !important;
        }
        
        .stTextInput > div > div > input:focus,
        .stTextArea > div > div > textarea:focus,
        .stSelectbox > div > div > select:focus {
            border-color: #4a7c59 !important;
            box-shadow: 0 0 0 2px rgba(74, 124, 89, 0.2) !important;
        }
        
        /* Label styling */
        .stTextInput label,
        .stTextArea label,
        .stSelectbox label {
            color: #2d5016 !important;
            font-weight: 500 !important;
            font-size: 1rem !important;
        }
        
        /* Button styling */
        .stButton > button {
            background: linear-gradient(45deg, #4a7c59, #2d5016) !important;
            color: white !important;
            border: none !important;
            border-radius: 10px !important;
            padding: 0.8rem 2rem !important;
            font-weight: 600 !important;
            font-size: 1.1rem !important;
            transition: all 0.3s ease !important;
            box-shadow: 0 4px 15px rgba(74, 124, 89, 0.3) !important;
            width: 100% !important;
        }
        
        .stButton > button:hover {
            transform: translateY(-2px) !important;
            box-shadow: 0 6px 20px rgba(74, 124, 89, 0.4) !important;
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
        
        /* Sidebar styling */
        .css-1d391kg {
            background-color: #f8fdf8 !important;
        }
        
        /* Icons */
        .icon {
            font-size: 1.2em;
            margin-right: 0.5rem;
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
        
        /* Success message styling */
        .success-message {
            background: linear-gradient(45deg, #d4edda, #c3e6cb);
            color: #155724;
            padding: 1rem;
            border-radius: 8px;
            border-left: 4px solid #28a745;
            margin: 1rem 0;
        }
    </style>
    """, unsafe_allow_html=True)

    # Main header
    st.markdown("""
    <div class="main-header">
        <h1>🌾 Smart Farming Advisor</h1>
        <p>Get personalized agricultural guidance powered by AI</p>
    </div>
    """, unsafe_allow_html=True)

    # Create two columns for layout
    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown('<div class="input-container">', unsafe_allow_html=True)
        
        # Query section
        st.markdown('<div class="section-header">🔍 Your Farming Query</div>', unsafe_allow_html=True)
        query = st.text_area(
            "Describe your farming challenge or question",
            placeholder="e.g., How can I improve soil fertility? What crops grow best in sandy soil?",
            height=100,
            help="Optional: Provide specific details about your farming query"
        )
        
        st.markdown("---")
        
        # Crop and location details
        st.markdown('<div class="section-header">🌱 Crop & Location Details</div>', unsafe_allow_html=True)
        
        crop_col, soil_col = st.columns(2)
        with crop_col:
            crop = st.text_input(
                "🌾 Crop Name",
                placeholder="e.g., Rice, Wheat, Tomato",
                help="Enter the primary crop you're growing or planning to grow"
            )
        
        with soil_col:
            soil = st.text_input(
                "🏔️ Soil Type",
                placeholder="e.g., Clay, Sandy, Loamy",
                help="Specify your soil type for better recommendations"
            )
        
        location = st.text_input(
            "📍 Location",
            placeholder="e.g., Maharashtra, India or specific district",
            help="Your farming location helps provide climate-specific advice"
        )
        
        st.markdown("---")
        
        # Language selection
        st.markdown('<div class="section-header">🌍 Language Preference</div>', unsafe_allow_html=True)
        language = st.selectbox(
            "Select your preferred language for the advice",
            ["English", "Hindi", "Marathi", "Telugu", "Bengali", "Tamil", "Gujarati", "Kannada", "Odia", "Punjabi"],
            help="Choose the language you're most comfortable with"
        )
        
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Submit button
        st.markdown("<br>", unsafe_allow_html=True)
        submit_button = st.button("🚀 Get Smart Farming Advice", use_container_width=True)

    with col2:
        # Feature highlight cards
        st.markdown("""
        <div class="feature-card">
            <div class="feature-title">🎯 Personalized Advice</div>
            <div class="feature-desc">Get recommendations tailored to your specific crop, soil, and location conditions.</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card">
            <div class="feature-title">🤝 Mixed Cropping</div>
            <div class="feature-desc">Learn about companion planting and optimal crop combinations for your farm.</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card">
            <div class="feature-title">🌿 Best Practices</div>
            <div class="feature-desc">Discover proven farming techniques and sustainable agricultural methods.</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card">
            <div class="feature-title">🗣️ Multi-language</div>
            <div class="feature-desc">Get advice in your preferred regional language for better understanding.</div>
        </div>
        """, unsafe_allow_html=True)

    # Handle form submission
    if submit_button:
        if not crop and not soil and not location and not query:
            st.error("❌ Please provide at least one field (crop, soil, location, or query) to get advice.")
        else:
            # Show loading message
            with st.spinner("🔄 Our AI experts are analyzing your farming requirements..."):
                try:
                    result = get_farming_practices(crop, location, soil, query, language)
                    
                    # Display results
                    st.markdown('<div class="results-container">', unsafe_allow_html=True)
                    st.markdown('<div class="results-header">🌟 Your Personalized Farming Advice</div>', unsafe_allow_html=True)
                    
                    # Success message
                    st.markdown("""
                    <div class="success-message">
                        ✅ <strong>Success!</strong> Your farming advice has been generated based on your inputs.
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Display the advice
                    st.markdown(result.tasks_output[0].raw)
                    st.markdown('</div>', unsafe_allow_html=True)
                    
                except Exception as e:
                    st.error(f"❌ An error occurred while generating advice: {str(e)}")
                    st.info("💡 Please check your internet connection and try again.")

    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666; padding: 1rem;">
        <p>🌱 <strong>Smart Farming Advisor</strong> - Empowering farmers with AI-driven agricultural insights</p>
        <p style="font-size: 0.9rem;">Made with ❤️ for sustainable farming practices</p>
    </div>
    """, unsafe_allow_html=True)