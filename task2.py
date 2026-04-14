import requests
import sys
from datetime import datetime

class CurrencyConverter:
    def __init__(self):
        self.api_url = "https://api.exchangerate-api.com/v4/latest"
        self.target_currencies = ["USD", "EUR", "GBP"]
        self.timeout = 5
    
    def validate_amount(self, amount):
        """Validate user input for amount"""
        try:
            amount = float(amount)
            if amount <= 0:
                raise ValueError("Amount must be greater than 0")
            return amount
        except ValueError as e:
            raise ValueError(f"Invalid amount: {e}")
    
    def fetch_exchange_rates(self):
        """Fetch exchange rates from API"""
        try:
            response = requests.get(
                f"{self.api_url}/INR",
                timeout=self.timeout
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.Timeout:
            raise Exception("API request timed out. Please try again later.")
        except requests.exceptions.ConnectionError:
            raise Exception("Connection error. Check your internet connection.")
        except requests.exceptions.HTTPError as e:
            raise Exception(f"API error: {e.response.status_code}")
        except Exception as e:
            raise Exception(f"Failed to fetch rates: {str(e)}")
    
    def convert_currency(self, amount, rates):
        """Convert INR to target currencies"""
        conversions = []
        for currency in self.target_currencies:
            if currency in rates["rates"]:
                converted = amount * rates["rates"][currency]
                conversions.append({
                    "From": "INR",
                    "To": currency,
                    "Amount": f"₹{amount:.2f}",
                    "Converted": f"{converted:.2f}",
                    "Rate": f"1 INR = {rates['rates'][currency]:.4f} {currency}"
                })
        return conversions
    
    def display_results(self, conversions):
        """Display conversion results in tabular format"""
        if conversions:
            print(f"Currency Conversion Report - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')},amt: {conversions[0]['Amount']}")

        else:
            print("No conversions available.")
    
    def run(self):
        """Main execution method"""
        try:
            # Get user input
            amount_input = input("Enter amount in INR: ").strip()
            amount = self.validate_amount(amount_input)
            
            print("\nFetching exchange rates...")
            
            # Fetch rates
            rates = self.fetch_exchange_rates()
            
            # Convert and display
            conversions = self.convert_currency(amount, rates)
            self.display_results(conversions)
            
        except ValueError as ve:
            print(f"❌ Validation Error: {ve}")
            sys.exit(1)
        except Exception as e:
            print(f"❌ Error: {e}")
            sys.exit(1)

if __name__ == "__main__":
    converter = CurrencyConverter()
    converter.run()