import requests

# Make a GET request
response = requests.get('https://api.example.com/data')

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")

    // Make a GET request
    async function fetchData() {
        try {
            const response = await fetch('https://api.example.com/data');
            
            // Check if the request was successful
            if (response.ok) {
                const data = await response.json();
                console.log(data);
            } else {
                console.log(`Error: ${response.status}`);
            }
        } catch (error) {
            console.log(`Error: ${error.message}`);
        }
    }

    fetchData();