import csv
import pandas as pd
import plotly.express as px
import numpy as np

df = pd.read_csv("data2.csv")

gre = df["GRE Score"].tolist()
chances = df["Chance of Admit"].tolist()

gre2 = np.array(gre)
chances2 = np.array(chances)

m,c = np.polyfit(gre2, chances2, 1)
x = 600
y = []

line = (m*x) + c
print("Chances of getting admission on 600 GRE is: " + str(line))
for x in gre2:
    yvalue = (m*x)+c
    y.append(yvalue)


fig = px.scatter(x=gre2, y=chances2)
fig.update_layout(shapes = [
    dict(
        type = "line",
        y0 = min(y),
        y1 = max(y),
        x0 = min(gre2),
        x1 = max(gre2),
    )
])
fig.show()