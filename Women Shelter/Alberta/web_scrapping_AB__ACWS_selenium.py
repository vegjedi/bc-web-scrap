# author: Minh
# date: Mar 01 2023

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import pandas as pd

options = Options()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options, executable_path="chromedriver")

name = []
region = []
link = []

type = []
crisis_line = []
business_line = []
email = []
website = []

driver.get("https://acws.ca/shelters/")
time.sleep(3)

for temp_name in driver.find_elements(By.CLASS_NAME, "font-purple"):
    # print(temp_name.text)
    name.append(temp_name.text)

name = name[2:] # remove first 2 unwanted name in the list

for temp_region in driver.find_elements(By.CLASS_NAME, "font-light-purple"):
    # print(temp_region.text)
    region.append(temp_region.text)

for temp_link in driver.find_elements(By.XPATH, '//*[@id="search-results"]/div/div/div/div/div[3]/div[1]/h4/a'):
    # print(temp_link.get_attribute("href"))
    link.append(temp_link.get_attribute("href"))

for acws_link in link:
    driver.get(acws_link)
    time.sleep(0.5)
    temp_type = driver.find_element(By.XPATH, '//*[@id="page"]/header/div/div/div/div/div[1]/div/h2/span[1]').text
    type.append(temp_type)

    result = driver.find_elements(By.XPATH, '//*[@id="main"]/div/div/div/section[1]/div/div/div[1]/div/div/a')
    print("result length is", len(result))

    crisis_line.append(result[0].text)
    print("crisis line", result[0].text)

    if len(result) == 2:
        business_line.append(result[1].text)
        print("business line", result[1].text)
        email.append("No email")
        website.append("No website")
    if len(result) == 3:
        business_line.append(result[1].text)
        print("business line", result[1].text)
        email.append(result[2].text)
        print("email", result[2].text)
        website.append("No website")
    if len(result) == 4:
        business_line.append(result[1].text)
        print("business line", result[1].text)
        email.append(result[2].text)
        print("email", result[2].text)
        website.append(result[3].text)
        print("website", result[3].text)     

print(len(name), len(region), len(link), len(type), len(crisis_line), len(business_line), len(email), len(website))

df = pd.DataFrame(list(zip(name, region, link, type, crisis_line, business_line, email, website)), columns=["name", "region", "link", "type", "crisis_line", "business_line", "email", "website"])
df.to_csv('/Users/jedi/Desktop/sample_data.csv')

driver.close()