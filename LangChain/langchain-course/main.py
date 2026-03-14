import warnings

from langchain.agents import create_openai_tools_agent, AgentExecutor
warnings.filterwarnings("ignore", message="urllib3 v2 only supports OpenSSL")
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI
from langchain.tools import tool
load_dotenv()  # Load environment variables from .env file



@tool
def search(query: str) -> str:
    """ 
    Tool that can searches over the internet 
    Args: 
        query: The query to search for 
    Returns:
        The search result
    
    """
    print(f"##search for {query}")
    return "Tokyo weather is sunny. "


llm = ChatOllama(
    model="tinyllama",
    temperature=0.7
)
tools = [search]

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("placeholder", "{chat_history}"),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}"),
])

agent = create_openai_tools_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools)

def main():
    print("Hello from lang-chain")
    result = agent_executor.invoke({"input": "What is the weather in Bihar - Siwan district"})
    print(result)
    

if __name__ == "__main__":
    main()
