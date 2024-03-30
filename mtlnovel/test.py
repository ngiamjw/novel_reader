import requests
from random import randint
import chapter_links

SCRAPEOPS_API_KEY = 'bc82af52-ef9a-4ae9-937c-ed2b6d2e6929'

def get_user_agent_list():
  response = requests.get('http://headers.scrapeops.io/v1/user-agents?api_key=' + SCRAPEOPS_API_KEY)
  json_response = response.json()
  return json_response.get('result', [])

def get_random_user_agent(user_agent_list):
  random_index = randint(0, len(user_agent_list) - 1)
  return user_agent_list[random_index]

## Retrieve User-Agent List From ScrapeOps
user_agent_list = get_user_agent_list()

url_list = ['https://www.mtlnovel.com/json/95220-v-6-1.json']
for url in url_list:

  ## Add Random User-Agent To Headers
    headers = {'User-Agent': get_random_user_agent(user_agent_list)}

  ## Make Requests
    r = requests.get(url=url, headers=headers)
    with open(f"hi.json", 'wb') as f:
        f.write(r.content)