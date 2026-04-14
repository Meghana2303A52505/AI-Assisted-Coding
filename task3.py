import requests

def fetch_github_repo_details(owner, repo_name):
    """
    Fetch repository details from GitHub API.
    
    Args:
        owner (str): GitHub username/organization
        repo_name (str): Repository name
    
    Returns:
        dict: Repository details or error message
    """
    
    # Validate input
    if not owner or not repo_name:
        return {"error": "Owner and repository name are required"}
    
    url = f"https://api.github.com/repos/{owner}/{repo_name}"
    
    try:
        response = requests.get(url, timeout=5)
        
        # Handle rate limit error
        if response.status_code == 403:
            return {"error": "API rate limit exceeded. Please try again later."}
        
        # Handle repo not found
        if response.status_code == 404:
            return {"error": "Repository not found"}
        
        # Handle other HTTP errors
        if response.status_code != 200:
            return {"error": f"HTTP Error {response.status_code}"}
        
        data = response.json()
        
        # Extract relevant details
        repo_details = {
            "repository": data.get("name"),
            "description": data.get("description"),
            "stars": data.get("stargazers_count"),
            "forks": data.get("forks_count"),
            "open_issues": data.get("open_issues_count")
        }
        
        return repo_details
    
    except requests.exceptions.Timeout:
        return {"error": "Request timeout"}
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}


# Example usage
if __name__ == "__main__":
    owner = input("Enter GitHub owner/organization: ").strip()
    repo = input("Enter repository name: ").strip()
    
    result = fetch_github_repo_details(owner, repo)
    
    if "error" in result:
        print(f"Error: {result['error']}")
    else:
        print(f"\n📊 Repository Details:")
        print(f"Name: {result['repository']}")
        print(f"Description: {result['description']}")
        print(f"⭐ Stars: {result['stars']}")
        print(f"🔀 Forks: {result['forks']}")
        print(f"📋 Open Issues: {result['open_issues']}")