import requests
import json
import os

def google_search(keyword, api_key, cx):
    base_url = "https://www.googleapis.com/customsearch/v1"
    params = {
        'q': keyword,
        'key': api_key,
        'cx': cx,
    }

    response = requests.get(base_url, params=params)
    data = json.loads(response.text)

    # Extract links from search results
    links = [item['link'] for item in data.get('items', [])]

    return links

def save_links_to_json(links, output_file):
    with open(output_file, 'w') as json_file:
        json.dump(links, json_file, indent=2)

if __name__ == "__main__":
    api_key = os.getenv("YOUR_GOOGLE_API_KEY")
    cx = os.getenv("YOUR_CUSTOM_SEARCH_ENGINE_ID")
    keyword = "honeybush"

    # Perform Google search and get links
    search_results = google_search(keyword, api_key, cx)

    # Save the links to a JSON file
    output_json_file = "google_search_links.json"
    save_links_to_json(search_results, output_json_file)

    print(f"Google search links for the keyword '{keyword}' saved to {output_json_file}")
