# author: Minh
# date: Mar 03 2023

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd

options = Options()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options, executable_path="chromedriver")

chpca_link = []

name = []
website = []
phone = []
address = []
bed = []

driver.get("https://www.chpca.ca/listings/?loc=&prv%5B%5D=277&go=true#results")
time.sleep(2)

for temp_link in driver.find_elements(By.XPATH, '//*[@id="results"]/div/div[5]/a'):
    chpca_link.append(temp_link.get_attribute("href"))

for link in chpca_link:
    driver.get(link)
    time.sleep(2)

    for temp_name in driver.find_elements(By.CLASS_NAME, "entry-title"):
        print(temp_name.text)
        name.append(temp_name.text)

    temp_label = driver.find_elements(By.CLASS_NAME, "clear-label")

    print("phone", temp_label[0].text)
    phone.append(temp_label[0].text)

    print("bed", temp_label[-1].text)
    bed.append(temp_label[-1].text)

    print("address", temp_label[-2].text)
    address.append(temp_label[-2].text)

    if len(temp_label) > 3:
        print("website", temp_label[-3].text)
        website.append(temp_label[-3].text)
    elif len(temp_label) == 3:
        print("no website")
        website.append("no website")
  
    print("----------------")

print(len(chpca_link), len(name), len(website), len(phone), len(address), len(bed))

df = pd.DataFrame(list(zip(chpca_link, name, website, phone, address, bed)), columns=["chpca_link", "name", "website", "phone", "address", "bed"])
df.to_csv('/Users/jedi/Desktop/sample_data.csv')

driver.close()