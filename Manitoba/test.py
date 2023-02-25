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

# df = pd.read_csv("/Users/jedi/Desktop/input.csv")
# city = df.city.values.tolist()
# name = df.name.values.tolist()

# address = []
# phone = []

# for i in range(len(name)):
#     gName = "+".join(name[i].split(" ") + city[i].split(" "))

driver.get("https://www.google.com/search?q=Birtle+Health+Centre/Sunnyside+Manor+Birtle")
time.sleep(2)

try:
    temp_address = driver.find_element(By.XPATH, '//*[@id="kp-wp-tab-overview"]/div[1]/div/div/div/div/div/div[4]/div/div/div/span[2]')
    print(temp_address.text)
except NoSuchElementException:
    print("No Address")
    pass

try:
    temp_phone = driver.find_element(By.XPATH, '//*[@id="kp-wp-tab-overview"]/div[1]/div/div/div/div/div/div[7]/div/div/div/span[2]/span/a/span/span')
    print(temp_phone.text)
except NoSuchElementException:
    print("No Phone")
    pass

# new_df = pd.DataFrame(list(zip(name, city, address, phone)), columns=["name", "city", "address", "phone"])
# new_df.to_csv('/Users/jedi/Desktop/sample_data.csv')

# driver.close()