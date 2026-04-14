import requests
from typing import List, Dict
import time

# Get a free API key from: https://newsapi.org/
API_KEY = "626ffaa3fbbb4003a199abfa159d9922"
BASE_URL = "https://newsapi.org/v2/top-headlines"
VALID_CATEGORIES = ["sports", "technology", "health"]
MAX_RETRIES = 3
RETRY_DELAY = 2  # seconds


def fetch_headlines(category: str, retries: int = 0) -> List[Dict]:
    """
    Fetch top 5 headlines for a given category with retry mechanism.
    
    Args:
        category: News category (sports, technology, health)
        retries: Current retry attempt count
    
    Returns:
        List of headline dictionaries
    """
    # Validate category
    if category.lower() not in VALID_CATEGORIES:
        raise ValueError(f"Invalid category. Choose from: {', '.join(VALID_CATEGORIES)}")
    
    # Validate API key
    if not API_KEY or API_KEY == "your_api_key_here":
        raise ValueError("Missing or invalid API key. Set API_KEY in the script.")
    
    params = {
        "category": category.lower(),
        "country": "us",
        "apiKey": API_KEY,
        "pageSize": 5
    }
    
    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        
        if data.get("status") != "ok":
            raise Exception(f"API Error: {data.get('message', 'Unknown error')}")
        
        return data.get("articles", [])
    
    except requests.exceptions.Timeout:
        error_msg = "Request timeout"
    except requests.exceptions.ConnectionError:
        error_msg = "Connection error"
    except requests.exceptions.HTTPError as e:
        error_msg = f"HTTP error: {e.response.status_code}"
    except Exception as e:
        error_msg = str(e)
    
    # Retry logic
    if retries < MAX_RETRIES:
        print(f"Error: {error_msg}. Retrying in {RETRY_DELAY}s... (Attempt {retries + 1}/{MAX_RETRIES})")
        time.sleep(RETRY_DELAY)
        return fetch_headlines(category, retries + 1)
    else:
        raise Exception(f"Failed after {MAX_RETRIES} attempts: {error_msg}")


def display_headlines(category: str) -> None:
    """
    Display top 5 headlines for a category in a formatted list.
    
    Args:
        category: News category
    """
    try:
        print(f"\n📰 Top 5 {category.upper()} Headlines:\n")
        articles = fetch_headlines(category)
        
        for i, article in enumerate(articles, 1):
            title = article.get("title", "N/A")
            source = article.get("source", {}).get("name", "N/A")
            url = article.get("url", "#")
            
            print(f"{i}. {title}")
            print(f"   Source: {source}")
            print(f"   Link: {url}\n")
    
    except ValueError as e:
        print(f"❌ Validation Error: {e}")
    except Exception as e:
        print(f"❌ Error: {e}")


def main() -> None:
    """Main function to run the news aggregator."""
    print("=" * 60)
    print("         NEWS AGGREGATOR")
    print("=" * 60)
    print(f"Available categories: {', '.join(VALID_CATEGORIES)}")
    
    while True:
        category = input("\nEnter a category (or 'quit' to exit): ").strip()
        
        if category.lower() == "quit":
            print("Goodbye! 👋")
            break
        
        if category:
            display_headlines(category)
        else:
            print("Please enter a valid category.")


if __name__ == "__main__":
    main()