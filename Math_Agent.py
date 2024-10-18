import os
from crewai import Agent,Task,Crew,Process
from dotenv import load_dotenv
load_dotenv()
from Calculator_Tool import calculate


print("##Welcome to the Math Wiz..")
math_input = input("What's your math equation:")

math_agent = Agent(
    role = "Math Magician",
    goal = "You are able to evaluate any math expression",
    backstory= "YOU ARE A MATH WHIZ.",
    verbose=True,
    tools=[calculate]
)

writer_agent = Agent(
    role="Writer",
    goal = "Craft compelling explanations based on outputs of math equations",
    backstory = "You are a reknown Content Strategist, known for your insightful and engaging articles. you transform complex concepts into compelling naratives.",
    verbose=True
)

task1 = Task(
    description=f"{math_input}",
    expected_output="Give full details in bullet points",
    agent=math_agent
)

task2 = Task(
    description="Using the insights provided, explain in detail how the equation and result were formed",
    expected_output= "Explain in great detail and save in markdown. Do not add the triple tick marks at the ending or the beginning of the file. Also dont say what type it is in the first line.",
    output_file="math.md",
    agent=writer_agent
)

crew = Crew(
    agents=[math_agent,writer_agent],
    tasks=[task1,task2],
    verbose=True
)


result = crew.kickoff()
print(result)