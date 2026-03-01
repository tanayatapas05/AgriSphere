import os
from crewai import Agent, Task, Crew, LLM
from dotenv import load_dotenv
from datetime import date

# ------------------------
# Load environment variables
# ------------------------
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
# Define Farmer Scheme Specialist Agent
# ------------------------
scheme_agent = Agent(
    role="Farmer Scheme Specialist",
    goal=(
        "Provide farmers with the most relevant central and state government schemes "
        "based on their location (state)."
    ),
    backstory=(
        "You are an agricultural policy expert who tracks the latest government schemes "
        "for farmers. You specialize in identifying eligibility, benefits, application "
        "steps, and deadlines. You always focus on schemes active or updated in the "
        "last 12 months and adapt the response to the requested language."
    ),
    allow_delegation=False,
    verbose=True,
    llm=llm
)

# ------------------------
# Define the task
# ------------------------
scheme_task = Task(
    description=(
        "Based on the farmer’s location {state}, list central and state-level "
        "government schemes available within the last 12 months. "
        "Provide eligibility, benefits, and how to apply. Answer in {language}."
    ),
    expected_output=(
        "A structured markdown list of:\n"
        "- Scheme name\n"
        "- Type (subsidy/insurance/credit/etc.)\n"
        "- Eligibility\n"
        "- Benefits\n"
        "- Application process\n"
        "- Deadlines (if any)\n"
        "- Official portal/helpline\n\n"
        f"Last updated: {date.today().isoformat()}"
    ),
    agent=scheme_agent,
    llm=llm
)

# ------------------------
# Create the crew
# ------------------------
scheme_crew = Crew(
    agents=[scheme_agent],
    tasks=[scheme_task],
    llm=llm,
    verbose=True
)

# ------------------------
# Function to get scheme recommendations
# ------------------------
def get_farmer_schemes(state, language):
    inputs = {"state": state, "language": language}
    result = scheme_crew.kickoff(inputs=inputs)
    return result
