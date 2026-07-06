from utils.expense_calculator import Calculator
from typing import List, Any
from langchain.tools import tool
import re


def _to_number(value: Any) -> float:
    """Sanitize and convert a value to float.

    - Accepts numbers, numeric strings (with commas/currency symbols), and returns 0.0 for invalid input.
    """
    if value is None:
        return 0.0
    if isinstance(value, (int, float)):
        return float(value)
    if isinstance(value, str):
        # remove anything that's not a digit, dot or minus
        clean = re.sub(r"[^0-9.\-]", "", value)
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


class CalculatorTool:
    def __init__(self):
        self.calculator = Calculator()
        self.calculator_tool_list = self._setup_tools()

    def _setup_tools(self) -> List:
        """Set up the tools for the calculator."""

        @tool
        def estimate_total_hotel_cost(price_per_night: Any, total_days: Any) -> float:
            """Calculate total hotel cost. Inputs may be strings (with commas/currency) or numbers."""
            p = _to_number(price_per_night)
            d = _to_number(total_days)
            return self.calculator.multiply(p, d)

        @tool
        def estimate_total_expense(*costs: Any) -> float:
            """Calculate the total expense based on a list of expenses."""
            nums = [_to_number(c) for c in costs]
            return self.calculator.calculate_total(*nums)

        @tool
        def calculate_daily_expense_budget(total_cost: Any, days: Any) -> float:
            """Calculate the daily budget based on total expense and number of days."""
            t = _to_number(total_cost)
            d = int(_to_number(days)) if _to_number(days) is not None else 0
            return self.calculator.calculate_daily_budget(t, d)

        return [estimate_total_hotel_cost, estimate_total_expense, calculate_daily_expense_budget]
