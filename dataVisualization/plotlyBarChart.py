import plotly.express as px
import pandas as pd

# reading the database
data = pd.read_csv("./dataVisualization/tips.csv")

# # plotting the scatter chart
# fig = px.bar(data, x='day', y='tip', color='sex')


# # creating a dropdown menu in plotly :


# # showing the plot
# fig.show()

# viewing data
# print("DATAHEAD")
# print(data.head())
# print("DATAINFO")
# print(data.info())
# print("DATADESCRIPTION")
# print(data.describe())


# slecting columns
# print(data['tip'])
# print(data[['day', 'tip']])



# filter rows

# this first takes the tip amount and then for that amount fetches for particular tips>5 
# tip -> tip>5:true -> print all those rowssss
# print(data[data['tip']>5])

# print(data[data['day']=="Sun"])

# group and summarize data

# group all rows by the day column - sun , sat etc
# select only tip column from each group 
# calculates the average tip for each day group.
# print(data.groupby('day')['tip'].mean())

# increasing order
print(data.sort_values(by='tip' , ascending = True))
# decreasing order
print(data.sort_values(by='tip' , ascending = False))