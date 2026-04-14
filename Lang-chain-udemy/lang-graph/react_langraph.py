from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_ollama import ChatOllama
from langchain_tavily import TavilySearch

load_dotenv()

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
def apply_discount(price: str, discount_tier: str) -> str:
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


@tool
def triple(num: int) -> int:
    """Tool that triples a number"""
    print(f"Tripling {num}")
    return num * 3


tools = [TavilySearch(max_results=3), get_product_price, apply_discount, triple]

llm = ChatOllama(model="qwen3:1.7b", temperature=0).bind_tools(tools)






