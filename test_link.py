import time
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

df = pd.read_csv("/Users/jedi/Desktop/street_data.csv")
city = df.city.values.tolist()
street = df.street.values.tolist()

postal=[]

r = requests.get("https://www.bing.com/search?q=1455+Western+Ave%2C+Williams+Lake")
soup = BeautifulSoup(r.content, "html.parser")

for name in soup.find_all("div", class_=True):
    print(name)
    match = re.findall(r'\b[ABCEGHJ-NPRSTVXY]\d[ABCEGHJ-NPRSTV-Z]\s\d[ABCEGHJ-NPRSTV-Z]\d\b', name.text)
    if len(match) != 0:
        full_address = match[0]
        postal.append(full_address)
        print(full_address)
        break