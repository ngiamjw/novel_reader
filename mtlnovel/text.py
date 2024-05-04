import requests
from bs4 import BeautifulSoup

def extract_content(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all <p> tags and extract their text
        paragraphs = soup.find_all('p')
        
        # Extract the text from each <p> tag and join them together
        content = '\n'.join(paragraph.get_text() for paragraph in paragraphs)
        
        return content
    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)
        return None

url = "https://www.mtlnovel.com/bulgarian-empire/chapter-1-through/"
content = extract_content(url)
if content:
    print(content)