# author: Minh
# date: Jan 16 2023

import requests
from bs4 import BeautifulSoup
import pandas as pd

df = pd.read_csv("/Users/jedi/Desktop/Final.csv")

url = df.url.values.tolist()

for link in url:
    r = requests.get(link)
    soup = BeautifulSoup(r.content, "html.parser")

    for name in soup.find_all("a"):
        if "advocatebc" not in name["href"].lower() and ":" in name["href"] and "mailto" not in name["href"] and "survey" not in name["href"]:
            print(name["href"])