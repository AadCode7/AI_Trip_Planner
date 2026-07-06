import os
from dotenv import load_dotenv
load_dotenv()

from langchain.tools import tool
from langchain_community.utilities.alpha_vantage import AlphaVantageAPIWrapper
import re


def _to_number(value):
    if value is None:
        return 0.0
    if isinstance(value, (int, float)):
        return float(value)
    if isinstance(value, str):
        clean = re.sub(r"[^0-9.\-\.]", "", value)
        if clean == "":
            return 0.0
        try:
            return float(clean)
        except ValueError:
            return 0.0
    try:
        return float(value)
    except Exception:
        return 0.0


@tool
def multiply(a, b) -> float:
    """Multiply two numbers (sanitized)."""
    return _to_number(a) * _to_number(b)

@tool
def add(a, b) -> float:
    """Add two numbers (sanitized)."""
    return _to_number(a) + _to_number(b)

@tool
def subtract(a, b) -> float:
    """Subtract two numbers (sanitized)."""
    return _to_number(a) - _to_number(b)

@tool
def divide(a, b) -> float:
    """Divide two numbers (sanitized)."""
    denom = _to_number(b)
    if denom == 0:
        raise ValueError("Cannot divide by zero.")
    return _to_number(a) / denom

@tool
def convert_currency_av(from_curr: str, to_curr: str, value) -> float:
    """Convert currency using AlphaVantage (sanitized)."""
    os.environ["ALPHA_VANTAGE_API_KEY"] = os.getenv("ALPHA_VANTAGE_API_KEY")
    alpha_vantage = AlphaVantageAPIWrapper()
    response = alpha_vantage.get_currency_exchange_rate(from_currency=from_curr, to_currency=to_curr)
    exchange_rate = response['Realtime Currency Exchange Rate']['5. Exchange Rate']

    return _to_number(value) * float(exchange_rate)
