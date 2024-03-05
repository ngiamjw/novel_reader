from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the web driver (make sure to install the appropriate driver for your browser)
driver = webdriver.Chrome()  # Or any other driver you prefer

# Navigate to the website
driver.get("https://example.com")

# Find all sections with a specific style attribute
sections = driver.find_elements(By.XPATH, "//section[@style]")

# Click on each section
for section in sections:
    section.click()

    # Wait for some time to ensure the content loads after clicking
    import time
    time.sleep(1)  # You can adjust the sleep time according to your needs

    # Find the section again to get the HTML content
    section_html = section.get_attribute('innerHTML')
    print(section_html)

# Don't forget to close the driver when you're done
driver.quit()