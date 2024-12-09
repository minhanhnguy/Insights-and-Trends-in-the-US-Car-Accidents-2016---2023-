import pandas as pd

data = pd.read_csv("US_Accidents_March23.csv")

data.head(100).to_csv("sample.csv", index=True)