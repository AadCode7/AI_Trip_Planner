import requests

class CurrencyConverter:
    def __init__(self, api_key: str):
        self.base_url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/"

    def convert(self, amount:float, from_currency: str, to_currency: str):
        """Convert the amount from one currency to another using the ExchangeRate API."""
        url = f"{self.base_url}/{from_currency}"
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception(f"Error fetching exchange rates: {response.status_code} - {response.text}")
        rates = response.json().get("conversion_rates")
        if to_currency not in rates:
            raise Exception(f"Currency {to_currency} not found in exchange rates.")

        return amount * rates[to_currency]        
    
