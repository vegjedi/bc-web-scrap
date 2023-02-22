# author: Minh
# date: Jan 16 2023

# import requests
from bs4 import BeautifulSoup
import pandas as pd

with open("/Users/jedi/Desktop/Assited.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

facility_name=[]
beds_total=[]
city=[]
health_auth=[]
phone=[]
address=[]
url=[]
room=[]

for name in soup.find_all("a"):
    facility_name.append(name["data-facility-name"])
    beds_total.append(name["data-beds-total"])
    city.append(name["data-city"])
    health_auth.append(name["data-hlth-auth"])
    phone.append(name["data-phone"])
    address.append(name["data-street-address"])
    url.append(name["data-url"])
    room.append(name["data-room-configuration"])

df = pd.DataFrame(list(zip(facility_name, beds_total, city,  health_auth, phone, address, url, room)), columns=["name", "bed", "city", "authority", "phone", "address", "url", "room"])

df.to_csv('/Users/jedi/Desktop/result1.csv')