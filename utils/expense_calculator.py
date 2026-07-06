

class Calculator:
    @staticmethod
    def multiply(a: float, b: float) -> float:
        """Multiply two numbers."""
        return a * b
    
    @staticmethod
    def calculate_total(*x: float) -> float:
        """Calculate the total expense based on a list of expenses."""
        return sum(x)

    @staticmethod
    def calculate_daily_budget(total: float, days: int) -> float:
        """Calculate the daily budget based on total expense and number of days."""
        if days <= 0:
            raise ValueError("Number of days must be greater than zero.")
        
        return total / days

    