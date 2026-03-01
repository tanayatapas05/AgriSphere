import os
from crewai import Crew, Agent, Task, LLM
from dotenv import load_dotenv
from crewai.project import CrewBase, agent, task

# Load API key from .env
load_dotenv()

# LLM setup
llm = LLM(
    model="gemini/gemini-1.5-flash",
    api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.0
)

@CrewBase
class DiseaseCrew:
    # Define agent
    @agent
    def crop_disease_agent(self) -> Agent:
        return Agent(
            role="Disease Analyst",
            goal="Analyze crop disease and provide detailed diagnosis + treatment",
            backstory=(
                "You are a crop disease specialist with 40+ years of experience. "
                "You can identify diseases, classify stages, and suggest both "
                "short-term and long-term treatments.You can also provide answer in any language."
            ),
            llm=llm
        )

    # Define task
    @task
    def describe_disease(self) -> Task:
        return Task(
            description=(
                "Analyze the crop disease based on {inputs}. "
                "Provide disease name, stage, and both short-term and long-term treatments in {language}."
            ),
            expected_output=(
                "A structured markdown output with:\n"
                "- Disease name\n"
                "- Stage (early/mid/advanced)\n"
                "- Short-term treatment\n"
                "- Long-term treatment\n"
                "- Preventive measures"
            ),
            agent=self.crop_disease_agent()
        )

    # Define crew
    def crew(self) -> Crew:
        return Crew(
            agents=[self.crop_disease_agent()],
            tasks=[self.describe_disease()],
            llm=llm
        )
    



