import streamlit as st
from PIL import Image
import google.generativeai as genai
from dotenv import load_dotenv
from mycrew import DiseaseCrew
import base64
from io import BytesIO
import os
import json

def app():
        load_dotenv()

        api_key = os.getenv("GEMINI_API_KEY")

        genai.configure(api_key=api_key)

        gemini_model = genai.GenerativeModel("gemini-1.5-flash")

        st.title("Disease Detection and Treatment Suggestion")

        uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

        if uploaded_file:
            # Show the uploaded image
            img = Image.open(uploaded_file)
            st.image(img, caption="Uploaded Image", use_container_width=True)

            language = st.selectbox(
            "🌍 Select Output Language",
            ["English", "Hindi", "Marathi", "Telugu", "Bengali", "Tamil", "Gujarati", "Kannada", "Odia", "Punjabi"]
        )


            if st.button("Analyze Image"):
                # # Convert image to base64 string
                # img_base64 = pil_to_base64(img)

                # # Pass base64 string into CrewAI
                # result = ImageCrew().crew().kickoff(
                #     inputs={"image": img_base64}
                # )

                # st.subheader("Description")
                # st.write(result.tasks_output[0].raw)

                response = gemini_model.generate_content(
                    [
                            {"role": "user", "parts": [
                        "You are a strict JSON generator. Return only valid JSON, no text outside JSON. \
                        Example format: {\"disease\": \"<name>\", \"stage\": \"<stage>\", \"treatment\": {\"short_term\": \"...\", \"long_term\": \"...\"}}",
                        img  # your image input
                    ]}
                    ]
                )

                raw_text = response.text.strip()

                # Remove code fences if present
                if raw_text.startswith("```"):
                    raw_text = raw_text.strip("`")        # remove all backticks
                    raw_text = raw_text.replace("json", "", 1).strip()  # remove optional 'json' label

                st.write("🔍 Raw Gemini Output:", raw_text)

                try:
                    data = json.loads(raw_text)

                    parsed = {
                        "disease": data.get("disease", ""),
                        "stage": data.get("stage", ""),
                        "short_term_treatment": data.get("treatment", {}).get("short_term", ""),
                        "long_term_treatment": data.get("treatment", {}).get("long_term", "")
                    }
                except Exception as e:
                    parsed = {
                        "disease": "Error parsing",
                        "stage": "",
                        "short_term_treatment": "",
                        "long_term_treatment": ""
                    }
                st.subheader("🔍 Gemini Analysis Result")

                crew = DiseaseCrew().crew()
                result = crew.kickoff(inputs={"inputs": parsed["disease"],
                                            "language": language})
                st.json(parsed)

                st.markdown(result)
