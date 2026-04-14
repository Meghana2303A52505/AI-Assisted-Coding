import requests
import time
from typing import Dict, Optional

# Using disease.sh API (free, no authentication required)
BASE_URL = "https://disease.sh/v3/covid-19/countries"

def fetch_covid_data(country_name: str, max_retries: int = 3) -> Optional[Dict]:
    """
    Fetch COVID-19 statistics for a specific country.
    
    Args:
        country_name: Name of the country
        max_retries: Maximum number of retry attempts
    
    Returns:
        Dictionary with COVID statistics or None if failed
    """
    
    for attempt in range(max_retries):
        try:
            # Make API request
            response = requests.get(f"{BASE_URL}/{country_name}", timeout=10)
            
            # Handle rate limiting
            if response.status_code == 429:
                wait_time = int(response.headers.get('Retry-After', 60))
                print(f"Rate limit exceeded. Waiting {wait_time} seconds...")
                time.sleep(wait_time)
                continue
            
            # Handle not found
            if response.status_code == 404:
                print(f"Error: Country '{country_name}' not found.")
                return None
            
            # Handle other HTTP errors
            response.raise_for_status()
            
            data = response.json()
            return data
        
        except requests.exceptions.Timeout:
            print(f"Timeout error (attempt {attempt + 1}/{max_retries}). Retrying...")
            time.sleep(2 ** attempt)  # Exponential backoff
        
        except requests.exceptions.ConnectionError:
            print(f"Connection error (attempt {attempt + 1}/{max_retries}). Retrying...")
            time.sleep(2 ** attempt)
        
        except requests.exceptions.HTTPError as e:
            print(f"HTTP Error: {e}")
            return None
        
        except requests.exceptions.RequestException as e:
            print(f"Request error: {e}")
            return None
    
    print("Failed after maximum retries.")
    return None


def display_covid_stats(data: Dict) -> None:
    """Display COVID-19 statistics in a readable format."""
    
    print("\n" + "="*50)
    print(f"COVID-19 Statistics for {data['country']}")
    print("="*50)
    print(f"Total Confirmed Cases: {data['cases']:,}")
    print(f"Total Deaths: {data['deaths']:,}")
    print(f"Total Recovered: {data['recovered']:,}")
    print(f"Active Cases: {data['active']:,}")
    print(f"Cases per Million: {data['casesPerOneMillion']:,}")
    print(f"Deaths per Million: {data['deathsPerOneMillion']:,}")
    print("="*50 + "\n")


def main():
    """Main function to run the COVID-19 data fetcher."""
    
    print("COVID-19 Statistics Fetcher")
    print("-" * 50)
    
    while True:
        country = input("Enter country name (or 'exit' to quit): ").strip()
        
        if country.lower() == 'exit':
            print("Goodbye!")
            break
        
        if not country:
            print("Please enter a valid country name.\n")
            continue
        
        print("Fetching data...")
        data = fetch_covid_data(country)
        
        if data:
            display_covid_stats(data)
        else:
            print("Could not fetch data. Please try again.\n")


if __name__ == "__main__":
    main()