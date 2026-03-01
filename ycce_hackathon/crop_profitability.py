import os
from crewai import Agent, Task, Crew, LLM
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# ------------------------
# Create the LLM (Gemini)
# ------------------------
llm = LLM(
    model="gemini/gemini-1.5-flash",         
    api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.0
)

# ------------------------
# Define Crop Advisor Agent
# ------------------------
advisor = Agent(
    role="Crop Advisor",
    goal="Suggest profitable crops based on soil and weather",
    backstory=(
        "You are an expert agronomist who analyzes soil and weather data to "
        "recommend the most profitable crops for a given location based on soil type,weather "
        "Provide expected yield and a profit score for each crop."
    ),
    allow_delegation=False,
    verbose=True,
    llm=llm
)

# ------------------------
# Define the task
# ------------------------
task = Task(
    description=(
        "Based on the following data, suggest the top 5 profitable crops which has higher profit_score and expected_yield.\n"
        "Soil data: {soil}\n"
        "Weather: {weather}\n"
        "Do not add extra notes, disclaimers, or any text outside the table."
        "Return a nicely formatted markdown with fields: crop, expected_yield (tons per acre), profit_score in percent out of 100%"
    ),
    expected_output="A nicely formatted markdown of crops with keys: crop, expected_yield [tons per acre], profit_score in percent out of 100% written in percent symbol." \
    " And the reasons why that crop was suggested in detail for each crop suggested and also tha basis on which the profitability was calculated below the table of suggested crops." \
    "Do not add extra notes, disclaimers, or any text outside the table." \
    "Example format:" \
    "Make the explanation clear, concise, and easy to understand, highlighting:" 
        "**Crop name**" 
        "- **Soil compatibility**"
        "- **Climate suitability**" 
        "- **Market demand & profitability**"  
        "- **Resource requirements (water, fertilizer, labor)**",
    agent=advisor,
    llm=llm
)

# ------------------------
# Create the crew
# ------------------------
crew = Crew(
    agents=[advisor],
    tasks=[task],
    llm=llm,
    verbose=True
)

# ------------------------
# Function to get crop recommendations
# ------------------------
def get_crop_recommendations(soil, weather, language):
    inputs = {"soil": soil, "weather": weather, "language":language}
    result = crew.kickoff(inputs=inputs)
    return result