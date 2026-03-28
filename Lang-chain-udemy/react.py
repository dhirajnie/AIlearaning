from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain.messages import SystemMessage
from langchain_core import messages
from langsmith import traceable

load_dotenv()
from typing import List
from langchain.agents import create_agent

from pydantic import BaseModel, Field
from langchain.tools import tool
from langchain_core.messages import HumanMessage, ToolMessage
from langchain_ollama import ChatOllama

MAX_ITERATIONS = 3
MODEL = "qwen3:1.7b"


@tool
def get_product_price(product_name: str) -> str:
    """
    Tool that gets the price of a product
    Args:
        product_name: The name of the product to get the price for
    Returns:
        The price of the product
    """
    # In a real implementation, this would query a database or an API
    prices = {
        "laptop": "$999",
        "phone": "$499",
        "headphones": "$199",
    }
    return prices.get(product_name.lower(), "Product not found")


@tool
def apply_discount(price:str,discount_tier:str) -> str:
    """
    Tool that applies a discount to a price
    Args:
        price: The original price of the product
        discount_tier: The discount tier to apply (e.g. "silver", "gold", "platinum")
    Returns:
        The discounted price
    """
    # In a real implementation, this would apply the discount based on the tier
    discounts = {
        "silver": 0.10,
        "gold": 0.20,
        "platinum": 0.30,
    }
    discount = discounts.get(discount_tier.lower(), 0)
    discounted_price = float(price.strip("$")) * (1 - discount)
    return f"${discounted_price:.2f}"


@traceable(name="LangChain Agent with Tools", project="LangChain Course")
def run_agent(query: str) -> str:
    llm = ChatOllama(model=MODEL)
    tools = [get_product_price, apply_discount]
    tools_dict = {t.name: t for t in tools}

    llm = init_chat_model(f"ollama:{MODEL}",temperature=0)
    llm_with_tools = llm.bind_tools(tools)
    messages=[
        SystemMessage(content="You are a helpful assistant that uses tools to answer questions. You" \
        " have access tp product catalog tool and discount tool." \
        "STRICT RULES: 1. Never guess or assume product prices, always use the get_product_price tool first to fetch the price. " \
        "2. Call apply_discount to apply discount only when you get product price , pass the exact price and tier  to discount tool " \
        "3. Always cite the tools you used in your answer." \
        "4. If user dont provide discount tier ask user for the discount tier and dont assume anything."),
     
        HumanMessage(content=query)
    ]
    for iteration in range(1, MAX_ITERATIONS+1):
        print(f"\n-----Iteration:{iteration}---------- ")
        ai_message = llm_with_tools.invoke(messages)
        tool_calls = ai_message.tool_calls
        # If it is not a tool call , then it is a final Answer, AI dont want to reason more
        if not tool_calls:
            print(f"\nFinal Answer:{ai_message.content}")
            break

        #Process only the FIRST tool call - force one tool per iteration as LLM can return multiple tools call in the response 
        tool_call= tool_calls[0]
        tool_name= tool_call.get("name")
        tool_args = tool_call.get("args",{})
        tool_call_id = tool_call.get("id")

        print(f"[ Tool Selected ] {tool_name}   with args {tool_args}")
        tool_to_use = tools_dict.get(tool_name)
        observation = tool_to_use.invoke(tool_args)
        print(f"[ Observation ] {observation}")
        messages.append(ai_message)
        messages.append(ToolMessage(content=str(observation), tool_call_id=tool_call_id))
        





    




if __name__ == "__main__":
    query = "What is the price of a laptop and what would be the price after applying a discount tier of gold?"
    result = run_agent(query)
    print(result)


