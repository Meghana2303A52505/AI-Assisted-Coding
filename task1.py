import requests
import json
from typing import Optional, Dict, Any

class PublicTransportFareAPI:
    """Retrieve public transport fare details between two stations."""
    
    def __init__(self, api_key: str = "demo"):
        self.base_url = "https://api.example.com/transport"
        self.api_key = api_key
        self.timeout = 10
    
    def validate_station(self, station: str) -> bool:
        """Validate station name format."""
        if not station or not isinstance(station, str):
            return False
        if len(station.strip()) < 2:
            return False
        return True
    
    def get_fare_details(self, source: str, destination: str) -> Optional[Dict[str, Any]]:
        """
        Retrieve fare details between two stations.
        
        Args:
            source: Starting station name
            destination: Ending station name
            
        Returns:
            Dictionary with fare details or None on error
        """
        # Validate inputs
        if not self.validate_station(source):
            print("❌ Error: Invalid source station. Min 2 characters required.")
            return None
        
        if not self.validate_station(destination):
            print("❌ Error: Invalid destination station. Min 2 characters required.")
            return None
        
        if source.lower() == destination.lower():
            print("❌ Error: Source and destination cannot be the same.")
            return None
        
        try:
            params = {
                "source": source.strip(),
                "destination": destination.strip(),
                "api_key": self.api_key
            }
            
            # Make API request with timeout
            response = requests.get(
                f"{self.base_url}/fare",
                params=params,
                timeout=self.timeout
            )
            response.raise_for_status()
            
            data = response.json()
            
            # Validate API response
            if not data or "fare" not in data:
                print("❌ Error: Invalid station names or route not available.")
                return None
            
            return data
            
        except requests.exceptions.Timeout:
            print(f"❌ Error: API request timed out after {self.timeout} seconds.")
            return None
        except requests.exceptions.ConnectionError:
            print("❌ Error: Cannot connect to API. Service may be unavailable.")
            return None
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 404:
                print("❌ Error: Station not found or invalid route.")
            else:
                print(f"❌ Error: API returned status code {e.response.status_code}")
            return None
        except json.JSONDecodeError:
            print("❌ Error: Invalid API response format.")
            return None
        except Exception as e:
            print(f"❌ Unexpected error: {str(e)}")
            return None
    
    def display_fare_details(self, fare_data: Dict[str, Any]) -> None:
        """Display fare details in structured format."""
        if not fare_data:
            return
        
        print("\n" + "="*50)
        print("🚌 FARE DETAILS")
        print("="*50)
        print(f"Source:           {fare_data.get('source', 'warangal')}")
        print(f"Destination:      {fare_data.get('destination', 'hyderabad')}")
        print(f"Distance:         {fare_data.get('distance', '5000')} km")
        print(f"Base Fare:        ${fare_data.get('fare', '1000')}")
        print(f"Duration:         {fare_data.get('duration', '1000')} mins")
        print(f"Vehicle Type:     {fare_data.get('vehicle_type', 'car')}")
        print("="*50 + "\n")


def main():
    """Main function to demonstrate fare lookup."""
    api = PublicTransportFareAPI()
    
    print("🚌 Public Transport Fare Finder\n")
    
    source = input("Enter source station: ").strip()
    destination = input("Enter destination station: ").strip()
    
    fare_details = api.get_fare_details(source, destination)
    
    if fare_details:
        api.display_fare_details(fare_details)
    else:
        print("\n⚠️ Unable to retrieve fare details. Please try again.")


if __name__ == "__main__":
    main()