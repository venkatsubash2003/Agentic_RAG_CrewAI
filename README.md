# Agentic RAG using CrewAI

Agentic RAG (Retrieval-Augmented Generation) is an advanced document processing application built using CrewAI, LangChain, and OpenAI models. It leverages AI agents to retrieve, analyze, and summarize information from PDF documents based on user queries. The application utilizes two specialized agents—one for extracting information from PDFs and another for generating polished summaries.
<p align="center">
  <img src="https://raw.githubusercontent.com/venkatsubash2003/crewAI/main/docs/crewai_logo.png" width="200" alt="Ollama model Logo">
</p>

## Features

- **PDF Analysis**: Upload a PDF document and extract key information based on user queries.
- **Summarization**: Automatically summarize the extracted data into a clean, concise format, including title, brief summary, bullet points, and TL;DR.
- **AI Agents**: Two AI agents—`PDF Analyst` and `Writer`—work together to provide a seamless, automated experience.
- **Interactive UI**: A Streamlit interface allows users to easily upload documents and input queries.

## Tech Stack

- **Python**
- **CrewAI**: Used to manage the flow of tasks between agents.
- **LangChain**: For integrating OpenAI's language models.
- **OpenAI GPT-3.5 & GPT-4**: For natural language processing and text generation.
- **Streamlit**: To create the user interface.
- **FAISS**: (optional) For document retrieval in advanced use cases.

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/venkatsubash2003/Agentic_RAG_CrewAI
    cd RAG_Crewai
    ```

2. **Set Up a Virtual Environment** (Optional but recommended):
    ```bash
    python3 -m venv env
    source env/bin/activate
    ```

3. **Install Required Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set Up API Keys**:
    - Create a `.env` file in the root directory with your OpenAI API key.
    ```
    OPENAI_API_KEY=your_openai_key_here
    ```

## Usage

1. **Run the Streamlit Application**:
    ```bash
    streamlit run main.py
    ```

2. **Upload a PDF**: Use the UI to upload a PDF file that you want to analyze.

3. **Enter a Query**: Provide a query (e.g., “What are the key findings?”) to instruct the PDF agent.

4. **View Results**: After processing, the app will display a comprehensive summary of the PDF content based on your query.

## Agents and Tasks

- **PDF Analyst**: Extracts the requested information from the PDF using OpenAI’s `gpt-3.5-turbo`.
- **Writer Agent**: Takes the analyzed data from the PDF Analyst and crafts a well-structured summary.

### Agent Workflow
1. The **PDF Analyst** finds and extracts data from the uploaded PDF file.
2. The **Writer Agent** transforms the extracted data into a neatly formatted summary.

### Task Breakdown
- **Task 1**: Extract relevant information from the PDF based on the query.
- **Task 2**: Summarize the extracted data into a compelling narrative, including bullet points and a TL;DR.

## Example Use Case

1. Upload a research paper in PDF format.
2. Enter a query like “Summarize the key results of this paper.”
3. The application analyzes the paper and provides a detailed summary along with bullet points.



