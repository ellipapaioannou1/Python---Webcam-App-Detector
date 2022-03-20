import pandas
from bokeh.plotting import figure
from bokeh.io import show, output_file

df = pandas.read_csv("bachelors.csv")
x = df["Year"]
y = df["Engineering"]

output_file("Plot.html")

f= figure()
f.line(x,y)   


show(f)