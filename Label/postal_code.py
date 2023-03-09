# author: Minh
# date: Jan 16 2023

import pandas as pd

df = pd.read_csv("/Users/jedi/Desktop/sample.csv")
post = df.post.values.tolist()

line_1=[]
line_2=[]
postal = []
address = []

for i in range(len(post)):
    post[i] = post[i].replace("\n", "\r")
    split = post[i].split("\r")
    line_1.append(split[0])
    line_2.append(split[1])
    postal.append(split[1][-7:])
    address.append(split[0] + split[1])

new_df = pd.DataFrame(list(zip(address, line_1, line_2, postal)), columns=["address", "line_1", "line_2", "postal"])
new_df.to_csv('/Users/jedi/Desktop/street_data.csv')