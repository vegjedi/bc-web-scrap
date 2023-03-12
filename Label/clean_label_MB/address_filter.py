# author: Minh
# date: Jan 16 2023

import pandas as pd

df = pd.read_csv("my_input.csv")
city = df.city.values.tolist()
address = df.full_address.tolist()
name = df.name.tolist()

street_1 = []
street_2 = []
split_city = []
postal = []
factor = [] 

for i in range(len(address)):
    x = address[i].split(", ")
    street_1.append(x[0])
    postal.append(x[-1])
    split_city.append(x[-2])
    if len(x) > 3:
        street_2.append(x[1])
    else:
        street_2.append("nil")
    factor.append(len(x))

print(len(street_1), len(street_2), len(split_city), len(postal), len(factor))

new_df = pd.DataFrame(list(zip(street_1, street_2, split_city, postal, factor)), columns=["street_1", "street_2", "split_city", "postal", "factor"])
new_df.to_csv('/Users/jedi/Desktop/mb_output.csv')