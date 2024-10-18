from crewai import Agent
from langchain_openai import ChatOpenAI
from crewai_tools import PDFSearchTool
from textwrap import dedent

class CustomAgents:

    def __init__(self):
        self.OPENAIGPT35= ChatOpenAI(model_name = "gpt-3.5-turbo",temperature=0.7)
        self.OPENAIGPT4 = ChatOpenAI(model_name = "gpt-4o",temperature=0.7)

    def pdf_agent(self,path):

        pdf_tool = PDFSearchTool(path)

        return Agent(
            role = "Senior PDF Analyst",
            goal = dedent(f"""Uncover any information from pdf files exceptionally well."""),
            backstory= dedent(f"""You can find anything in a pdf. The people need you."""),
            tools=[pdf_tool],
            verbose=True,
            llm = self.OPENAIGPT35,
        )
    
    def writer_agent(self):
        return Agent(
            role= "Writer",
            goal = dedent(f"""Take the information from the pdf agent and summarize it nicely."""),
            backstory= dedent(f"""All your life, you have loved writing summaries"""),
            verbose=True,
            llm = self.OPENAIGPT35
        )
    

