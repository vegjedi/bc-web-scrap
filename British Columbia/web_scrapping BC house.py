# author: Minh
# date: Jan 16 2023

import requests
from bs4 import BeautifulSoup
import pandas as pd


# Get URLs from all pages
# for page in range(11):
#     r = requests.get(f'''https://connect.health.gov.bc.ca/assisted-living-residence?f%5B0%5D=residence_type%3ASeniors%20and%20Persons%20with%20Disabilities&f%5B1%5D=year%3A2021&name=&address=&page={page}''')
#     soup = BeautifulSoup(r.content, "html.parser")

#     for name in soup.find_all("a", href=True):
#         if "/assisted-living-residence/" in name["href"] and "unregistered" not in name["href"]:
#             print("https://connect.health.gov.bc.ca/"+name["href"])

df = pd.read_csv("/Users/jedi/Desktop/bc_as_data.csv")
url = df.url.values.tolist()

facility=[]
bed=[]
city=[]
street=[]
authority=[]
website=[]

for link in url:
    r = requests.get(link)
    soup = BeautifulSoup(r.content, "html.parser")

    for name in soup.find_all("span", class_="field field--name-title field--type-string field--label-hidden"):
        facility.append(name.text)
        print(name.text)

    for name in soup.find_all("div", class_="field field--name-field-alr-total-unit-count field--type-integer field--label-inline clearfix"):
        bed.append((name.text).split("\n")[2])
        print((name.text).split("\n")[2])

    for name in soup.find_all("span", class_="locality"):
        city.append(name.text)
        print(name.text)

    for name in soup.find_all("span", class_="address-line1"):
        street.append(name.text)
        print(name.text)

    for name in soup.find_all("div", class_="field field--name-field-alr-health-authority field--type-entity-reference field--label-inline clearfix"):
        authority.append((name.text).split("\n")[2])
        print((name.text).split("\n")[2])

    site = soup.find_all("div", class_="field field--name-field-alr-website field--type-link field--label-inline clearfix")
    
    if len(site) == 0:
        website.append("NA")
        print("NA")
    else:
        for name in site:
            website.append((name.text).split("\n")[2])
            print((name.text).split("\n")[2])

new_df = pd.DataFrame(list(zip(url, facility, bed, city, street, authority, website)), columns=["url", "facility", "bed", "city", "street", "authority", "website"])

new_df.to_csv('/Users/jedi/Desktop/bc_as_result.csv')