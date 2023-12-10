import requests


def expand_link(short_url):
    try:
        response = requests.head(short_url, allow_redirects=True)
        return response.url
        
    except requests.RequestException as e:
        return f"Error during request: {e}"


if __name__ == "__main__":
    # Example usage
    shortened_url = "https://t.co/RFzX0LSCfD"
    expanded_url = expand_link(shortened_url)
    print(f"Original URL: {shortened_url}")
    print(f"Expanded URL: {expanded_url}")
