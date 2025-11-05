import plotly.express as px
import pandas as pd

# reading the database
data = pd.read_csv("./dataVisualization/tips.csv")

# group and summarize: average tip per day
avg_tip_per_day = data.groupby('day')['tip'].mean().reset_index()

# sort days by average tip in descending order
avg_tip_per_day = avg_tip_per_day.sort_values(by='tip', ascending=False)

# create bar chart
fig = px.bar(
    avg_tip_per_day,
    x='day',
    y='tip',
    # bar colors depend on tip value (higher tip → darker/brighter color).
    color='tip',
    title='Average Tip Amount per Day',
    text='tip'
)

fig.update_traces(texttemplate='%{text:.2f}', textposition='outside')
fig.show()
