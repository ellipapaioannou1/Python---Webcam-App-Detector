import pandas
from bokeh.plotting import figure, show, output_file

df = pandas.read_excel("verlegenhuken.xlsx",sheet_name=0)

x = df["Temperature"]/10
y = df["Pressure"]/10
f=figure(plot_width=500,plot_height=400,tools='pan')
f.xaxis.axis_label="Temperature(C)"
f.yaxis.axis_label="Pressure(hPa)"    
f.title.text="Temperature and Air Pressure"


f.dot(x,y)
output_file("weather.html")
show(f)
