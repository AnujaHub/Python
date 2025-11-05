import pandas as pd
from IPython.display import display


# reading data
data = pd.read_csv("./dataVisualization/tips.csv")

# top 10 rows
display(data.head(10))