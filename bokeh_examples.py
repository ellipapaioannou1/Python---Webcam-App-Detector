#time-series plot
from turtle import width
import pandas
from bokeh.plotting import figure, show, output_file

df = pandas.read_csv("timeseries.csv", parse_dates=["Date"])

f= figure(width = 500, height = 200, x_axis_type = "datetime", sizing_mode='scale_width')

f.line(df["Date"],df["C"],color = "Red", alpha = 0.8)

output_file("Time-Series.html")
show(f)