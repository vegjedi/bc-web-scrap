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
business_phone = []
emergency_phone = []
website = []
link = []

driver.get("https://acws.ca/shelters/")
time.sleep(3)

for temp_name in driver.find_elements(By.CLASS_NAME, "font-purple"):
    print(temp_name.text)
    name.append(temp_name)

name = name[2:] # remove first 2 unwanted name in the list

for temp_region in driver.find_elements(By.CLASS_NAME, "font-light-purple"):
    print(temp_region.text)
    region.append(temp_region)

for temp_link in driver.find_elements(By.XPATH, '//*[@id="search-results"]/div/div/div/div/div[3]/div[1]/h4/a'):
    print(temp_link.get_attribute("href"))
    link.append(temp_link)

df = pd.DataFrame(list(zip(name, region, link)), columns=["name", "region", "link"])
df.to_csv('/Users/jedi/Desktop/sample_data.csv')

driver.close()