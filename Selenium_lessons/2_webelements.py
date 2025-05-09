from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://testautomationpractice.blogspot.com")

wikipedia_icon = driver.find_element("class name", "wikipedia-icon")
search_input = driver.find_element("id", "Wikipedia1_wikipedia-search-input")
search_button = driver.find_element("css selector", ".wikipedia-search-button")
all_buttons = driver.find_elements("tag name", "button")

print(wikipedia_icon)
print(search_input)
print(search_button)
for button in all_buttons:
    print(button)
