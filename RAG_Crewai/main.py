import os
from textwrap import dedent
from crewai import Crew, Process
from agents import CustomAgents
from tasks import CustomTasks
from dotenv import load_dotenv
load_dotenv()
import streamlit as st 

class CustomCrew:
    def __init__(self,var1):
        self.var1 = var1

    def run(self,path):
        agents = CustomAgents()
        tasks = CustomTasks()

        custom_agent1 = agents.pdf_agent(path)
        custom_agent2 = agents.writer_agent()

        custom_task1 = tasks.pdf_task(
            agent = custom_agent1,
            var1 = self.var1
        )

        custom_task2 = tasks.writer_task(
            agent = custom_agent2
        )

        crew = Crew(
            agents= [custom_agent1,custom_agent2],
            tasks = [custom_task1, custom_task2],
            verbose= True
        )

        result = crew.kickoff()
        return result
    
if __name__ == "__main__":
    st.title("Agentic RAG using CrewAI")
    pdf_file = st.file_uploader("Browse your file: ",type=["pdf"])
    if pdf_file is not None:
        st.write(f"Filename: {pdf_file.name}")
        st.write(f"File type: {pdf_file.type}")
        st.write(f"File size: {pdf_file.size} bytes")
        save_path = f"./{pdf_file.name}"
        with open(save_path, "wb") as file:
            file.write(pdf_file.getbuffer())
        var1 = st.text_input(dedent("Enter your query:"))
        if var1:

            st.subheader("Loading the result...")

            custom_crew = CustomCrew(var1)
            result = custom_crew.run(save_path)
            st.subheader("Your result:")
            st.write(result)
    else:
        st.write("Upload the file:")
        
