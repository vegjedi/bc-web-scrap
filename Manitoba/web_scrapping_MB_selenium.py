# author: Minh
# date: Feb 24 2023

import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import pandas as pd

options = Options()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options, executable_path="chromedriver")

df = pd.read_csv("/Users/jedi/Desktop/input.csv")
city = df.city.values.tolist()
name = df.name.values.tolist()

address_1 = []
address_2 = []
phone_1 = []
phone_2 = []
link = []

for i in range(len(name)):
    gName = "+".join(name[i].split(" ") + city[i].split(" "))
    temp_link = f"https://www.google.com/search?q={gName}"
    print(name[i], city[i])
    print(temp_link)
    link.append(temp_link)

    driver.get(temp_link)
    time.sleep(2)

    try:
        temp_address = driver.find_element(By.XPATH, '//*[@id="kp-wp-tab-overview"]/div[1]/div/div/div/div/div/div[4]/div/div/div/span[2]')
        print(temp_address.text)
        address_1.append(temp_address.text)
    except NoSuchElementException:
        print("No Address 1")
        address_1.append("No Address 1")
        pass

    try:
        temp_address = driver.find_element(By.XPATH, '//*[@id="kp-wp-tab-overview"]/div[1]/div/div/div/div/div/div[5]/div/div/div/span[2]')
        print(temp_address.text)
        address_2.append(temp_address.text)
    except NoSuchElementException:
        print("No Address 2")
        address_2.append("No Address 2")
        pass

    try:
        temp_phone = driver.find_element(By.XPATH, '//*[@id="kp-wp-tab-overview"]/div[1]/div/div/div/div/div/div[6]/div/div/div/span[2]/span/a/span/span')
        print(temp_phone.text)
        phone_1.append(temp_phone.text)
    except NoSuchElementException:
        print("No Phone 1")
        phone_1.append("No Phone 1")
        pass

    try:
        temp_phone = driver.find_element(By.XPATH, '//*[@id="kp-wp-tab-overview"]/div[1]/div/div/div/div/div/div[7]/div/div/div/span[2]/span/a/span/span')
        print(temp_phone.text)
        phone_2.append(temp_phone.text)
    except NoSuchElementException:
        print("No Phone 2")
        phone_2.append("No Phone 2")
        pass

new_df = pd.DataFrame(list(zip(link, name, city, address_1, address_2, phone_1, phone_2)), columns=["link", "name", "city", "address 1", "address 2", "phone 1", "phone 2"])
new_df.to_csv('/Users/jedi/Desktop/sample_data.csv')

driver.close()