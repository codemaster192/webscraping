from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# for holding the resultant list
element_list = []

# Set up ChromeDriver once before looping
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

for page in range(1, 3):
    page_url = f"https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page={page}"
    driver.get(page_url)

    # Extract elements
    title = driver.find_elements(By.CLASS_NAME, "title")
    price = driver.find_elements(By.CLASS_NAME, "price")
    description = driver.find_elements(By.CLASS_NAME, "description")
    rating = driver.find_elements(By.CLASS_NAME, "ratings")

    for i in range(len(title)):
        element_list.append([title[i].text, price[i].text, description[i].text, rating[i].text])

# Close the driver after the loop
driver.quit()

# Print the result
print(element_list)
