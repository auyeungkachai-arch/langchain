from dotenv import load_dotenv
import os
load_dotenv()
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage 
from langchain_ollama import ChatOllama
# from tavily import TavilyClient
# from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_tavily import TavilySearch

# @tool
# def get_weather(query: str) -> str:
#     """get results from tavily search
    
#     Args:
#         query: The query to search for
#     Returns:
#         The results of the search
#     """
#     print(f"Getting results for {query}")

#     return tavily_client.search(query=query)

llm = ChatOllama(model="llama3.2:latest")
tool = [TavilySearch()]
agent = create_agent(model=llm, tools=tool)

def main():
    print("Hello from langchain!")
    response = agent.invoke({"messages":[HumanMessage(content="search for 3 job postings for an ai engineer using langchain in the bay area on linkedin and list their details?")]})
    print(response)

if __name__ == "__main__":

    main()