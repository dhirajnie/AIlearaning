from dotenv import load_dotenv
from langgraph.graph import MessagesState
from langgraph.prebuilt import ToolNode
from react_langraph import llm, tools

SYSTEM_MESSAGE="""
YOU ARE A HELPFUL ASSISTANT THAT USES TOOLS TO ANSWER QUESTIONS AND CITES SOURCES.
STRICT RULES:
1. Never guess or assume product prices, always use the get_product_price tool first to fetch the price.
2. Call apply_discount to apply discount only when you get product price, pass the exact price and tier to discount tool.
3. Always cite the tools you used in your answer.
4. If user don't provide discount tier ask user for the discount tier and don't assume anything.
"""

def run_agent_reasoning(state:MessagesState)->MessagesState:
    """
    Run the agent reasoning node.
    """
    response = llm.invoke([{"role":"system", "content":SYSTEM_MESSAGE}, *state["messages"]])
    return {"messages": state["messages"] + [response]}


tool_node = ToolNode(tools)

