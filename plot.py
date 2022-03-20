#importing the libraries
import pandas
from bokeh.plotting import figure
from bokeh.io import output_file, show


df = pandas.read_csv("data.csv")
x = df["x"]
y = df["y"]
#prepare the data
#x =[3,7.5,10]
#y =[3,6,9]

#prepare the output
output_file("Line Data.html")

#create a figure
f=figure()

#create line plot
#f.triangle(x,y)
#f.circle(x,y)  circle
f.line(x,y)   


show(f)