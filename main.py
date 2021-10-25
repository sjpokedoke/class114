import csv
import pandas as pd
import plotly.express as px
import numpy as np

df = pd.read_csv("data.csv")

height = df["Height"].tolist()
weight = df["Weight"].tolist()

weight2 = np.array(weight)
height2 = np.array(height)

#slope and y-intercept using prebuilt function of numpy
m,c = np.polyfit(height2, weight2, 1)
x = 250
y = []

line = (m*x) + c
print("Weight of someone: " + str(line))

for x in height2:
    yvalue = (m*x)+c
    y.append(yvalue)
fig = px.scatter(x=height2, y=weight2)
fig.update_layout(shapes = [
    dict(
        type = "line",
        y0 = min(y),
        y1 = max(y),
        x0 = min(height2),
        x1 = max(height2),
    )
])
fig.show()