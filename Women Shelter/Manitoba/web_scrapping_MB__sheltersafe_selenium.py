# author: Minh
# date: Mar 01 2023

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import pandas as pd

options = Options()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options, executable_path="chromedriver")

name = []
website = []
phone = []

driver.get("https://sheltersafe.ca/manitoba/")
time.sleep(2)

for temp_name in driver.find_elements(By.XPATH, '//*[@id="gmwd_container_1"]/div[3]/div[2]/div[2]/div/div[1]'):
    name.append(temp_name.text.replace("*", ""))

for temp_phone in driver.find_elements(By.XPATH, '//*[@id="gmwd_container_1"]/div[3]/div[2]/div[2]/div/div[2]/div/p[1]'):
    temp_phone_list = temp_phone.text.split("\n")
    phone.append(temp_phone_list[0])

for i in range(len(name)):
    temp_website = driver.find_elements(By.XPATH, f'//*[@id="gmwd_container_1"]/div[3]/div[2]/div[2]/div[{i+1}]/div[2]/div/a')
    if len(temp_website) == 0:
        print("no website") 
        website.append("no website")
    else:
        website.append(temp_website[0].text.replace("email: ", ""))

print(len(name), len(website), len(phone))

df = pd.DataFrame(list(zip(name, website, phone)), columns=["name", "website", "phone"])
df.to_csv('/Users/jedi/Desktop/sample_data.csv')

driver.close()