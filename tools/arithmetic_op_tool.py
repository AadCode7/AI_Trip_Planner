import os
from dotenv import load_dotenv
load_dotenv()

from langchain.tools import tool
from langchain_community.utilities.alpha_vantage import AlphaVantageAPIWrapper

@tool
def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b    

@tool
def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b

@tool
def subtract(a: float, b: float) -> float:
    """Subtract two numbers."""
    return a - b

@tool
def divide(a: float, b: float) -> float:
    """Divide two numbers."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

@tool
def convert_currency(from_curr: str, to_curr: str, value: float) -> float:
    os.environ["ALPHA_VANTAGE_API_KEY"] = os.getenv("ALPHA_VANTAGE_API_KEY")
    alpha_vantage = AlphaVantageAPIWrapper()
    response = alpha_vantage.get_currency_exchange_rate(from_currency=from_curr, to_currency=to_curr)
    exchange_rate = response['Realtime Currency Exchange Rate']['5. Exchange Rate']

    return value * float(exchange_rate)
