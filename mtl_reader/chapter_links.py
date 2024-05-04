from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time

url = "https://wtr-lab.com/en/serie-5290/the-rise-of-australia"

driver = webdriver.Chrome()

# Open the webpage
driver.get(url)

# Wait for the button to be clickable (adjust the time as needed)
button = driver.find_element("id", "contents-tab-toc")
button.click()

# Wait for some time to allow dynamic content to load (adjust the time as needed)
time.sleep(2)

# Get the updated page source after clicking the button
updated_html = driver.page_source

# Close the browser
driver.quit()


soup = BeautifulSoup(updated_html, 'html.parser')

# Fetch the HTML content of the page


# with open('text.txt', 'w', encoding='utf-8') as fn:

#     texts = soup.prettify()
#     for text in texts:
#         fn.write(text)

def novel_name():
    title = soup.find('title')
    text = title.get_text()
    return text

def chapter_list():
    tag_list = soup.find_all('a')

    # href_list = [tag['href'] for tag in tag_list if 'the-rise-of-australia/chapter' in tag['href'] and tag['href'] not in href_list]

    href_list = []

    for tag in tag_list:
        if 'the-rise-of-australia/chapter' in tag['href'] and tag['href'] not in href_list:
            href_list += ['https://wtr-lab.com/' + tag['href']]
    return href_list
        



# Find all 'a' tags and extract href attributes
# href_list = [a['href'] for span in soup.select('.chapter-item span') for a in span.find_all('a', href=True)]

# # Print the extracted href attributes
# for href in href_list:
#     print(href)