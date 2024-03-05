import requests
import sys

def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    # Construct the URL for the subreddit
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    # Set a custom User-Agent header to avoid potential errors
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    
    # Send a GET request to the subreddit's API endpoint
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    # Check the response status code
    if response.status_code == 404:
        # If subreddit not found, return 0
        return 0
    elif response.status_code == 403:
        # If forbidden (e.g., due to rate limiting), inform the user and return 0
        print("Error: Forbidden. This may be due to rate limiting or other restrictions.")
        return 0
    elif response.status_code != 200:
        # If any other error occurs, inform the user and return 0
        print(f"Error: HTTP Status Code {response.status_code}")
        return 0
    
    # Attempt to parse the JSON response and extract the number of subscribers
    try:
        data = response.json()
        subscribers = data.get("data", {}).get("subscribers", 0)
        return subscribers
    except Exception as e:
        # If an error occurs while parsing JSON, inform the user and return 0
        print(f"Error parsing JSON: {e}")
        print(f"Response content: {response.content}")
        return 0

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-main.py <subreddit>")
        sys.exit(1)
    subreddit = sys.argv[1]
    print("{:d}".format(number_of_subscribers(subreddit)))
