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

link = []
operator = []
name = []
bed = []
address_1 = []
address_2 = []
full_address = []
phone = []
city = []
facilityNumber = []
info = []

for page in range(1, 11):
    driver.get(f"http://personalcarehomes.saskatchewan.ca/PersonalCareHomes/Table?FacilityCountLimit=0&ProgramAreaName=PersonalCareHomes&SortBy=FacilityName&pageNumber={page}")
    time.sleep(3)

    for element in driver.find_elements(By.CLASS_NAME, "hovereffect"):
        temp_link= "http://personalcarehomes.saskatchewan.ca" + re.search(r"'([^']*)'",(element.get_attribute("onclick"))).group(1)
        link.append(temp_link)
        
        bed.append(element.find_element(By.CLASS_NAME, "capacity").text)
        name.append(element.find_element(By.CLASS_NAME, "facilityName").text)
        operator.append(element.find_element(By.CLASS_NAME, "primaryOwner").text)
        phone.append(element.find_element(By.CLASS_NAME, "phoneNumber").text)
        facilityNumber.append(element.find_element(By.CLASS_NAME, "facilityNumber").text)
        info.append(element.find_element(By.CLASS_NAME, "tags").text)

     
        temp_address = element.find_element(By.CLASS_NAME, "siteAddress").text
        full_address.append(temp_address)
        temp_city = element.find_element(By.CLASS_NAME, "community").text
        print(temp_city, temp_address)
        city.append(temp_city)   
        split_address = temp_address.split(temp_city)
        if temp_address != split_address[0]:
            address_1.append(split_address[0][:-1])
            address_2.append(temp_city + split_address[1])
        else:
            address_1.append("None")
            address_2.append("None")

df = pd.DataFrame(list(zip(link, operator, name, bed, address_1, address_2, full_address, phone, city, facilityNumber, info)), columns=["link", "operator", "name", "bed", "address_1", "address_2", "full_address", "phone", "city", "facilityNumber", "info"])
df.to_csv('/Users/jedi/Desktop/sample_data.csv')

driver.close()