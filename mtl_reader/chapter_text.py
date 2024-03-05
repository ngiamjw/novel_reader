import requests
from bs4 import BeautifulSoup
import json

# URL of the page
class chapter_texts:
    def __init__(self, url):
        self.url = url
        self.json_data = self.return_json_data()

    def return_json_data(self):
        # Fetch the HTML content of the page
        response = requests.get(self.url)
        html_content = response.content

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')

        # Find all 'p' tags and extract the text
        script_with_specific_id = soup.find('script', id='__NEXT_DATA__')

        if script_with_specific_id:
            try:
                script_content = script_with_specific_id.string
                json_data = json.loads(script_content)
                # number = json_data['props']['pageProps']['serie']
                # print(json.dumps(number, indent=2))
                
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")
        else:
            print("Script not found.")

        return json_data

    def novel_content(self):
        # json_data = self.return_json_data()
        body_content = self.json_data['props']['pageProps']['serie']['chapter_data']['data']['body']

        return body_content

    def chapter_number(self):
        # json_data = self.return_json_data()
        number = self.json_data['props']['pageProps']['serie']['chapter']['order']
        return number
