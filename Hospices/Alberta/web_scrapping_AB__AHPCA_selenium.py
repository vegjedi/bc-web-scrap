# author: Minh
# date: Mar 02 2023

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd

options = Options()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options, executable_path="chromedriver")

link = []
ahpca_link = []

unwanted = ["https://ahpca.ca/ahpca-resource-directory/", "https://ahpca.ca/ahpca-resource-directory/?wpbdp_view=all_listings", "https://ahpca.ca/ahpca-resource-directory/start-community-hospice-group/"]

for i in range(3):
    driver.get(f"https://ahpca.ca/ahpca-resource-directory/wpbdp_category/hospices/page/{i+1}/")
    time.sleep(1)
    for temp_link in driver.find_elements(By.XPATH, '//*[@id]/div/div[1]/div/a'):
        link.append(temp_link.get_attribute("href"))

for i in link:
    if i not in unwanted:
        ahpca_link.append(i)

area = []
info = []
website = []
phone = []
address = []

for individual_link in ahpca_link:
    print(individual_link)
    driver.get(individual_link)
    time.sleep(2)

    for temp_area in driver.find_elements(By.XPATH, '//*[@id]/div[2]/div[2]/div[1]/div/a[1]'):
        area.append(temp_area.text)
        print(temp_area.text)

    for temp_info in driver.find_elements(By.XPATH, '//*[@id]/div[2]/div[2]/div[2]/div'):
        info.append(temp_info.text.split("\n")[0])
        print(temp_info.text.split("\n")[0])

    for temp_website in driver.find_elements(By.XPATH, '//*[@id]/div[2]/div[2]/div[3]/div/a'):
        website.append(temp_website.get_attribute("href"))
        print(temp_website.get_attribute("href"))

    for temp_phone in driver.find_elements(By.XPATH, '//*[@id]/div[2]/div[2]/div[4]/div'):
        phone.append(temp_phone.text)
        print(temp_phone.text)

    for temp_address in driver.find_elements(By.XPATH, '//*[@id]/div[2]/div[2]/div[5]/div'):
        address.append(temp_address.text)
        print(temp_address.text)
    
    print("=== end of block ===")

print(len(ahpca_link), len(area), len(info), len(website), len(phone), len(address))

df = pd.DataFrame(list(zip(ahpca_link, area, info, website, phone, address)), columns=["ahpca_link", "area", "info", "website", "phone", "address"])
df.to_csv('/Users/jedi/Desktop/sample_data.csv')

driver.close()