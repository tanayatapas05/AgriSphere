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
# Define Farming Agent
# ------------------------
farming_agent = Agent(
    role="Agro Advisory Specialist",
    goal="Suggest best farming practices and suitable companion crops for mixed farming.",
    backstory=(
        "You are an experienced agronomist who advises smallholder farmers. "
        "You tailor advice to the crop, soil type, and location. "
        "Your answers are always structured, practical, and safe."
    ),
    allow_delegation=False,
    verbose=True,
    llm=llm
)

# ------------------------
# Define Task
# ------------------------
farming_task = Task(
    description=(
        "Farmer wants advice for growing {crop} in {location} with {soil} soil. "
        "Farmer query: {query}. "
        "Provide:\n"
        "- Step-by-step farming practices\n"
        "- Best practices (water, fertilizer, sowing, harvesting, etc.)\n"
        "- Suitable companion crops for mixed farming\n"
    ),
    expected_output=(
        "Structured markdown output: in {language}\n"
        "### Steps\n- ...\n- ...\n\n"
        "### Best Practices\n- ...\n- ...\n\n"
        "### Companion Crops\n- ...\n- ...\n"
    ),
    agent=farming_agent,
    llm=llm
)

# ------------------------
# Create Crew
# ------------------------
crew = Crew(
    agents=[farming_agent],
    tasks=[farming_task],
    llm=llm,
    verbose=True
)

# ------------------------
# Function to get farming practices
# ------------------------
def get_farming_practices(crop, location, soil, query, language):
    inputs = {
        "crop": crop,
        "location": location,
        "soil": soil,
        "query": query,
        "language": language
    }
    result = crew.kickoff(inputs=inputs)
    return result
