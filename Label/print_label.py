# author: Minh
# date: Jan 16 2023

import pandas as pd
from blabel import LabelWriter

df = pd.read_csv("/Users/jedi/Desktop/input.csv")

name = df.name.tolist()
line_1 = df.line_1.tolist()
line_2 = df.line_2.tolist()
records = []
name_1 = []
name_2 = []

for i in range(len(name)):
    temp_dict = dict(facility_name = (name[i].upper()).replace(".",""), add_line_1= (line_1[i].upper()).replace(".", ""), add_line_2 = line_2[i].upper())
    records.append(temp_dict)

label_writer = LabelWriter("item_template.html", default_stylesheets=("style.css",))

label_writer.write_labels(records, target='/Users/jedi/Desktop/qrcode_and_label.pdf')