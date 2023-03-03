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
    time.sleep(2)
    for temp_link in driver.find_elements(By.XPATH, '//*[@id]/div/div[1]/div/a'):
        link.append(temp_link.get_attribute("href"))

for i in link:
    if i not in unwanted:
        ahpca_link.append(i)
name = []
area = []
info = []
website = []
phone = []
address = []

for individual_link in ahpca_link:
    print(individual_link)
    driver.get(individual_link)
    time.sleep(3)

    for temp_name in driver.find_elements(By.CLASS_NAME, "sc_layouts_title_caption"):
        name.append(temp_name.text)
        print(temp_name.text)

    temp_area = driver.find_elements(By.XPATH, '//*[@id]/div[2]/div[2]/div[1]/div/a[1]')
    if len(temp_area) == 0:
        print("no area")
        area.append("no area")
    else:
        area.append(temp_area[0].text)
        print(temp_area[0].text)

    temp_info = driver.find_elements(By.XPATH, '//*[@id]/div[2]/div[2]/div[2]/div')
    if len(temp_info) == 0:
        print("no info")
        info.append("no info")
    else:
        info.append(temp_info[0].text.split("\n")[0])
        print(temp_info[0].text.split("\n")[0])

    temp_website = driver.find_elements(By.XPATH, '//*[@id]/div[2]/div[2]/div[3]/div/a')
    if len(temp_website) == 0:
        print("no website") 
        website.append("no website")
    else:
        website.append(temp_website[0].get_attribute("href"))
        print(temp_website[0].get_attribute("href"))

    temp_phone = driver.find_elements(By.XPATH, '//*[@id]/div[2]/div[2]/div[4]/div')
    if len(temp_phone) == 0:
        print("no phone")
        phone.append("no phone")
    else:
        phone.append(temp_phone[0].text)
        print(temp_phone[0].text)

    temp_address = driver.find_elements(By.XPATH, '//*[@id]/div[2]/div[2]/div[5]/div')
    if len(temp_address) == 0:
        print("no address")
        address.append("no addresss")
    else:
        address.append(temp_address[0].text)
        print(temp_address[0].text)
    
    print("===============")

print(len(ahpca_link), len(name), len(area), len(info), len(website), len(phone), len(address))

print(ahpca_link)
print(name)
print(area)
print(info)
print(website)
print(phone)
print(address)

df = pd.DataFrame(list(zip(ahpca_link, name, area, info, website, phone, address)), columns=["ahpca_link", "name", "area", "info", "website", "phone", "address"])
df.to_csv('/Users/jedi/Desktop/sample_data.csv')

driver.close()