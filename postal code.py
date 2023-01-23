# author: Minh
# date: Jan 16 2023

import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

df = pd.read_csv("/Users/jedi/Desktop/street_data.csv")
city = df.city.values.tolist()
street = df.street.values.tolist()
full = df.full.values.tolist()
p_code = df.code.values.tolist()

postal=[]
short_postal=[]
code=[]

print(len(city))

for i in range(len(city)):
    print(p_code[i], p_code[i] == "abc")
    if p_code[i] == "abc":
        search=("+".join(street[i].split()))+"%2C+"+("+".join(city[i].split()))
        print(f'https://www.google.com/search?q={search}')

        r = requests.get(f'https://www.google.com/search?q={search}')

        soup = BeautifulSoup(r.content, "html.parser")

        bs4_div = soup.find_all("div")
        for name in bs4_div:
            match = re.findall(r'\b[ABCEGHJ-NPRSTVXY]\d[ABCEGHJ-NPRSTV-Z]\s\d[ABCEGHJ-NPRSTV-Z]\d\b', name.text)
            if len(match) != 0:
                full_address = street[i]+", "+city[i]+", "+match[0]
                short_postal.append(street[i])
                postal.append(full_address)
                code.append(match[0])
                print(full_address, len(postal), i+1)
                break
        if len(postal) != (i+1):
            short_postal.append(street[i])
            postal.append("abc")
            code.append("abc")
            print("Not add")

new_df = pd.DataFrame(list(zip(city, postal, short_postal, code)), columns=["city", "full", "street", "code"])
new_df.to_csv('/Users/jedi/Desktop/final_posta_result.csv')
new_df.to_csv('/Users/jedi/Desktop/street_data.csv')