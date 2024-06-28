import pandas as pd

x = pd.read_csv("path")

print(x['Primary Type'].value_counts())


