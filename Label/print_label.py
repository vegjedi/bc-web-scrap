# author: Minh
# date: Jan 16 2023

import pandas as pd
import click
from blabel import LabelWriter

# df = pd.read_csv("/Users/jedi/Desktop/sample.csv")
# post = df.post.values.tolist()

# line_1=[]
# line_2=[]
# postal = []
# address = []

# for i in range(len(post)):
#     post[i] = post[i].replace("\n", "\r")
#     split = post[i].split("\r")
#     line_1.append(split[0])
#     line_2.append(split[1])
#     postal.append(split[1][-7:])
#     address.append(split[0] + split[1])

# new_df = pd.DataFrame(list(zip(address, line_1, line_2, postal)), columns=["address", "line_1", "line_2", "postal"])
# new_df.to_csv('/Users/jedi/Desktop/street_data.csv')

@click.command()
@click.option('-i', '--input',  required=True, type=str, help="CSV file with columns that match the variables in the HTML template")
@click.option('-o', '--output', default="output.pdf", type=str, help="Name of the output PDF")
@click.option('-t', '--template', default="item_template.html", type=str, help="Name of the HTML template file", show_default="item_template.html")
@click.option('-s', '--style', default="style.css", type=str, help="Name of the CSS file", show_default="style.css")

def write_labels(input, output, template, style):
    df = pd.read_csv(input)
    records = df.to_dict('records')

    label_writer = LabelWriter(template, default_stylesheets=(style,))
    label_writer.write_labels(records, target=output)     

if __name__ == '__main__':
    write_labels()   