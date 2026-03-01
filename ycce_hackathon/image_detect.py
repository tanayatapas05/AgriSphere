import streamlit as st
from PIL import Image
import google.generativeai as genai
from dotenv import load_dotenv
from mycrew import DiseaseCrew
from io import BytesIO
import os
import json

def app1():
    load_dotenv()
    
    # Page configuration
    st.set_page_config(
        page_title="🔬 Disease Detection",
        page_icon="🌿",
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
        
        /* Upload container styling */
        .upload-container {
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
        
        /* File uploader styling */
        .stFileUploader > div > div > button {
            background: linear-gradient(45deg, #4a7c59, #2d5016) !important;
            color: white !important;
            border: none !important;
            border-radius: 10px !important;
            padding: 0.8rem 2rem !important;
            font-weight: 600 !important;
            font-size: 1rem !important;
            transition: all 0.3s ease !important;
            box-shadow: 0 4px 15px rgba(74, 124, 89, 0.3) !important;
        }
        
        .stFileUploader > div > div > button:hover {
            transform: translateY(-2px) !important;
            box-shadow: 0 6px 20px rgba(74, 124, 89, 0.4) !important;
        }
        
        /* Image container */
        .image-container {
            background: white;
            padding: 1.5rem;
            border-radius: 15px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.1);
            border: 2px solid #e8f5e8;
            margin: 1rem 0;
        }
        
        /* Language selection */
        .stSelectbox > div > div > select {
            border: 2px solid #d4edda !important;
            border-radius: 8px !important;
            padding: 0.5rem !important;
            font-family: 'Poppins', sans-serif !important;
            transition: all 0.3s ease !important;
        }
        
        .stSelectbox > div > div > select:focus {
            border-color: #4a7c59 !important;
            box-shadow: 0 0 0 2px rgba(74, 124, 89, 0.2) !important;
        }
        
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
        
        /* Results containers */
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
        
        /* JSON output styling */
        .json-container {
            background: #f8f9fa;
            border: 1px solid #d4edda;
            border-radius: 8px;
            padding: 1rem;
            margin: 1rem 0;
            font-family: 'Monaco', 'Consolas', monospace;
        }
        
        /* Analysis result styling */
        .analysis-result {
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
        
        /* Raw output styling */
        .raw-output {
            background: #f8f9fa;
            border: 1px solid #d4edda;
            padding: 1rem;
            border-radius: 8px;
            font-family: 'Monaco', 'Consolas', monospace;
            font-size: 0.9rem;
            color: #2d5016;
            margin: 1rem 0;
        }
        
        /* Sidebar styling */
        .css-1d391kg {
            background-color: #f8fdf8 !important;
        }
    </style>
    """, unsafe_allow_html=True)
    
    api_key = os.getenv("GEMINI_API_KEY")
    genai.configure(api_key=api_key)
    gemini_model = genai.GenerativeModel("gemini-1.5-flash")
    
    # Main header
    st.markdown("""
    <div class="main-header">
        <h1>🔬 Plant Disease Detection & Treatment</h1>
        <p>AI-powered diagnosis for healthier crops</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Create layout columns
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Upload section
        st.markdown('<div class="upload-container">', unsafe_allow_html=True)
        st.markdown('<div class="section-header">📸 Upload Plant Image</div>', unsafe_allow_html=True)
        
        uploaded_file = st.file_uploader(
            "Choose an image of the affected plant",
            type=["jpg", "jpeg", "png"],
            help="Upload a clear image showing the plant disease symptoms"
        )
        
        if uploaded_file:
            # Show the uploaded image
            st.markdown('<div class="image-container">', unsafe_allow_html=True)
            img = Image.open(uploaded_file)
            st.image(img, caption="🌿 Uploaded Plant Image", use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
            
            st.markdown("---")
            
            # Language selection
            st.markdown('<div class="section-header">🌍 Language Preference</div>', unsafe_allow_html=True)
            language = st.selectbox(
                "Select your preferred language for diagnosis",
                ["English", "Hindi", "Marathi", "Telugu", "Bengali", "Tamil", "Gujarati", "Kannada", "Odia", "Punjabi"],
                help="Choose the language you're most comfortable with"
            )
            
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Analysis button
            st.markdown("<br>", unsafe_allow_html=True)
            analyze_button = st.button("🔍 Analyze Plant Disease", use_container_width=True)
            
            if analyze_button:
                with st.spinner("🔬 Analyzing plant image with AI..."):
                    try:
                        response = gemini_model.generate_content([
                            {"role": "user", "parts": [
                                "You are a strict JSON generator. Return only valid JSON, no text outside JSON. \
                                Example format: {\"disease\": \"<name>\", \"stage\": \"<stage>\", \"treatment\": {\"short_term\": \"...\", \"long_term\": \"...\"}}",
                                img
                            ]}
                        ])
                        
                        raw_text = response.text.strip()
                        
                        # Remove code fences if present
                        if raw_text.startswith("```"):
                            raw_text = raw_text.strip("`")
                            raw_text = raw_text.replace("json", "", 1).strip()
                        
                        # Show raw output in styled container
                        st.markdown('<div class="results-container">', unsafe_allow_html=True)
                        st.markdown('<div class="results-header">🔍 AI Analysis Results</div>', unsafe_allow_html=True)
                        
                        st.markdown("*🔬 Raw Gemini Output:*")
                        st.markdown(f'<div class="raw-output">{raw_text}</div>', unsafe_allow_html=True)
                        
                        try:
                            data = json.loads(raw_text)
                            parsed = {
                                "disease": data.get("disease", ""),
                                "stage": data.get("stage", ""),
                                "short_term_treatment": data.get("treatment", {}).get("short_term", ""),
                                "long_term_treatment": data.get("treatment", {}).get("long_term", "")
                            }
                            
                            # Success message
                            st.markdown("""
                            <div class="success-message">
                                ✅ <strong>Analysis Complete!</strong> Disease detection successful.
                            </div>
                            """, unsafe_allow_html=True)
                            
                        except Exception as e:
                            parsed = {
                                "disease": "Error parsing",
                                "stage": "",
                                "short_term_treatment": "",
                                "long_term_treatment": ""
                            }
                            st.error(f"❌ Error parsing JSON: {str(e)}")
                        
                        # Get detailed analysis from crew
                        st.markdown("---")
                        st.markdown("*🤖 Getting Detailed Treatment Recommendations...*")
                        
                        with st.spinner("🌱 Consulting agricultural experts..."):
                            crew = DiseaseCrew().crew()
                            result = crew.kickoff(inputs={
                                "inputs": parsed["disease"],
                                "language": language
                            })
                        
                        # Display parsed JSON in styled format
                        st.markdown("*📊 Structured Analysis:*")
                        st.json(parsed)
                        
                        # Display crew result
                        st.markdown('<div class="analysis-result">', unsafe_allow_html=True)
                        st.markdown("*🌟 Expert Treatment Recommendations:*")
                        st.markdown(result)
                        st.markdown('</div>', unsafe_allow_html=True)
                        
                        st.markdown('</div>', unsafe_allow_html=True)
                        
                    except Exception as e:
                        st.error(f"❌ An error occurred during analysis: {str(e)}")
                        st.info("💡 Please check your API key and internet connection.")
    
    with col2:
        # Feature highlight cards
        st.markdown("""
        <div class="feature-card">
            <div class="feature-title">🔬 AI-Powered Detection</div>
            <div class="feature-desc">Advanced computer vision analyzes plant images to identify diseases accurately.</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card">
            <div class="feature-title">💊 Treatment Suggestions</div>
            <div class="feature-desc">Get both short-term and long-term treatment plans for identified diseases.</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card">
            <div class="feature-title">🎯 Disease Staging</div>
            <div class="feature-desc">Understand the severity and stage of the detected plant disease.</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card">
            <div class="feature-title">🗣️ Multi-language Support</div>
            <div class="feature-desc">Receive diagnosis and treatment advice in your preferred regional language.</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card">
            <div class="feature-title">⚡ Quick Analysis</div>
            <div class="feature-desc">Get instant results with detailed explanations and actionable recommendations.</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666; padding: 1rem;">
        <p>🔬 <strong>Plant Disease Detection</strong> - Protecting crops with AI technology</p>
        <p style="font-size: 0.9rem;">Early detection saves harvests 🌾</p>
    </div>
    """, unsafe_allow_html=True)