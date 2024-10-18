import os
from crewai import Agent,Task,Crew
from dotenv import load_dotenv
load_dotenv()

os.environ["OPENAI_MODEL_NAME"] = "gpt-4o"

info_agent = Agent(
    role = "Information Agent",
    goal = "Give compelling information about a certain topic",
    backstory = "You love to know information. People Love and hate you for it. You win most of the quizzes at your local pub"

)

task1 = Task(
    description = "Tell me all about blue-ringed octopus",
    expected_output = "Give me a quick summary and a 7 bullet points describing it",
    agent = info_agent
)

crew = Crew(
    agents = [info_agent],
    tasks = [task1],
    verbose=True
)

result = crew.kickoff()

print(result)
