# author: Minh
# date: Feb 23 2023

import re
import requests
from bs4 import BeautifulSoup
import pandas as pd

r = requests.get("http://personalcarehomes.saskatchewan.ca/PersonalCareHomes/Table?pageNumber=10")
soup = BeautifulSoup(r.content, "html.parser")

for name in soup.find_all("td", class_="hovereffect"):
    print(name.text)

# df = pd.read_csv("/Users/jedi/Desktop/bc_as_data.csv")
# url = df.url.values.tolist()

# facility=[]
# bed=[]
# city=[]
# street=[]
# authority=[]
# website=[]

# new_df = pd.DataFrame(list(zip(url, facility, bed, city, street, authority, website)), columns=["url", "facility", "bed", "city", "street", "authority", "website"])

# new_df.to_csv('/Users/jedi/Desktop/bc_as_result.csv')