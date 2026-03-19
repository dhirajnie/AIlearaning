from dotenv import load_dotenv
from langchain.messages import SystemMessage

load_dotenv()
from typing import List
from langchain.agents import create_agent

from pydantic import BaseModel, Field
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama
from tavily import TavilyClient

tavily = TavilyClient()

class Source(BaseModel):
    """Schema for source used by Model"""
    url:str=Field(description="The URL of the source")

class Answers(BaseModel):
    """ Schema for agent response with answers and source """
    answer:str=Field(description="The agent answer for the query")
    sources:List[Source]=Field(default_factory=list, description="The sources used by the agent to answer the query")


@tool
def search(query: str) -> str:
    """
    Tool that searches over internet
    Args:
        query: The query to search for
    Returns:
        The search result
    """
    print(f"Searching for {query}")
    return tavily.search(query=query)


@tool
def searchRelevantCompanies(query: str) -> str:
    """
    Tool that searches over internet for relevant companies based on the current company as query
    Args:
        query: The query to search for
    Returns:
        The search result
    """
    print(f"Relevant companies for {query}")
    return tavily.search(query=query)

llm = ChatOllama(model="qwen3:1.7b")
tools = [search, searchRelevantCompanies]
agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt="You are an assistant that uses tools to answer questions and cites sources.",
    response_format=Answers,
)


def main():
    print("Hello from langchain-course!")
    messages=[SystemMessage(content="You are a job search assistant that helps users find relevant companies and job openings based on their experience and skills. STRICT RULE : 1. Find the relevant companies based on the user's experience and skills. 2. After fetching the companies, find out the job openings in those companies. 3. Find all the jobs relevant to the user."),
              HumanMessage(content="1.I am full stack developer and 10 years of experience Find the releavant comapanies i can apply in as i am full stack developer 2. after fetching the company find out the opening in that companies  3. Find all the jobs relevant to me" )
              ]
    result = agent.invoke({"messages":messages})
    print(result)

if __name__ == "__main__":
    main()