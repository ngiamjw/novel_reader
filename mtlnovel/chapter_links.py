from selenium import webdriver
from bs4 import BeautifulSoup
import time


def json_links(url):
    # Initialize Chrome WebDriver
    driver = webdriver.Chrome()
    json_links = []
    try:
        # Open the webpage
        driver.get(url)
        
        # Wait for the element to be clickable
        chapter_tab = driver.find_element("id", "tabchapterlist")
        chapter_tab.click()
        
        # Give some time for the page to load or for any animations to finish
        time.sleep(2)  # Adjust this time according to your website's loading time
        
        # Get the page source after clicking the tab
        page_source = driver.page_source
        
        # Parse the HTML using Beautiful Soup
        soup = BeautifulSoup(page_source, 'html.parser')
        
        # Find all <section> tags containing <amp-list> tags
        sections = soup.find_all('section')
        
        # Iterate through the <section> tags
        for section in sections:
            amp_list_tag = soup.find('amp-list')
        
        # Extracting the src attribute value
            src_attribute = ""

            if amp_list_tag:
                src_attribute = amp_list_tag.get('src')
                json_links.append(src_attribute)
                print("Source URL of JSON file:", src_attribute)
            
    except Exception as e:
        print("An error occurred:", e)

    finally:
        # Close the browser
        driver.quit()
    return json_links

print(json_links('https://www.mtlnovel.com/bulgarian-empire/'))