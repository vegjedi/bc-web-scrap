# author: Minh
# date: Feb 22 2023

import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd

options = Options()
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=options, executable_path="chromedriver")

# link = []
# operator = []
# name = []
# bed = []
# address = []
# phone = []

driver.get("http://personalcarehomes.saskatchewan.ca/PersonalCareHomes/Table?FacilityCountLimit=0&ProgramAreaName=PersonalCareHomes&SortBy=FacilityName&pageNumber=1")

time.sleep(2)

for element in driver.find_elements(By.CLASS_NAME, "hovereffect"):
    link= "http://personalcarehomes.saskatchewan.ca" + re.search(r"'([^']*)'",(element.get_attribute("onclick"))).group(1)
    print(link)
    print("capacity", element.find_element(By.CLASS_NAME, "capacity").text)
    print("community", element.find_element(By.CLASS_NAME, "community").text)
    print("facility", element.find_element(By.CLASS_NAME, "facilityName").text)
    print("Address", element.find_element(By.CLASS_NAME, "siteAddress").text)
    print("primaryOwner", element.find_element(By.CLASS_NAME, "primaryOwner").text)
    print("phoneNumber", element.find_element(By.CLASS_NAME, "phoneNumber").text)
    print("facilityNumber", element.find_element(By.CLASS_NAME, "facilityNumber").text)
    print("Info", element.find_element(By.CLASS_NAME, "tags").text)
    print(r"\n")


# for id in id:
#     temp_link = f"https://standardsandlicensing.alberta.ca/detail_page.html?ID={id}"
#     driver.get(temp_link)
#     time.sleep(3)

#     link.append(temp_link)
#     operator.append(driver.find_element(By.ID, "OPERATOR").text)
#     facility.append(driver.find_element(By.ID, "FACILITY_TYPE").text)
#     name.append(driver.find_element(By.ID, "FACILITY_NAME").text)
#     bed.append(driver.find_element(By.ID, "UNITS").text)
#     address_1.append(driver.find_element(By.ID, "ADDRESSLINE1").text)
#     address_2.append(driver.find_element(By.ID, "ADDRESSLINE2").text)
#     cityline.append(driver.find_element(By.ID, "CITYLINE").text)
#     phone.append(driver.find_element(By.ID, "PHONE").text)

# df = pd.DataFrame(list(zip(link, operator, facility, name, bed, address_1, address_2, cityline, phone)), columns=["link", "operator", "facility", "name", "bed", "address_1", "address_2", "cityline", "phone"])
# df.to_csv('/Users/jedi/Desktop/sample_data.csv')

driver.close()