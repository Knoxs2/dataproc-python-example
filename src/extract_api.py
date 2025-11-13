import requests
import json
import os

def fetch_data(api_url: str, output_path: str):
    """Fetch data from a mock API and store it locally."""
    response = requests.get(api_url)
    response.raise_for_status()
    data = response.json()
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w') as f:
        json.dump(data, f)
    print(f"Data saved to {output_path}")
    return data

if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com/posts"
    output_path = "/data/raw/posts.json"
    fetch_data(api_url, output_path)