# author: Minh
# date: Feb 22 2023

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd

options = Options()
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=options, executable_path="chromedriver")

id = []
link = []
operator = []
facility =[]
name = []
bed = []
address_1 = []
address_2 = []
cityline = []
phone = []

driver.get("https://standardsandlicensing.alberta.ca/search-results.html?VALUE=_FOC_NULL&FACILITY_TYPE=Supportive%20Living%20AccommodationLodge&DISTANCE=_FOC_NULL&POSTAL_CODE=_FOC_NULL")
time.sleep(2)

for element in driver.find_elements(By.CSS_SELECTOR, "#search-results-table > div"):
    if element.get_attribute("facility_id") != None:
        page_id = element.get_attribute("facility_id")
        id.append(page_id)

for id in id:
    temp_link = f"https://standardsandlicensing.alberta.ca/detail_page.html?ID={id}"
    driver.get(temp_link)
    time.sleep(3)

    link.append(temp_link)
    operator.append(driver.find_element(By.ID, "OPERATOR").text)
    facility.append(driver.find_element(By.ID, "FACILITY_TYPE").text)
    name.append(driver.find_element(By.ID, "FACILITY_NAME").text)
    bed.append(driver.find_element(By.ID, "UNITS").text)
    address_1.append(driver.find_element(By.ID, "ADDRESSLINE1").text)
    address_2.append(driver.find_element(By.ID, "ADDRESSLINE2").text)
    cityline.append(driver.find_element(By.ID, "CITYLINE").text)
    phone.append(driver.find_element(By.ID, "PHONE").text)

df = pd.DataFrame(list(zip(link, operator, facility, name, bed, address_1, address_2, cityline, phone)), columns=["link", "operator", "facility", "name", "bed", "address_1", "address_2", "cityline", "phone"])
df.to_csv('/Users/jedi/Desktop/sample_data.csv')

driver.close()