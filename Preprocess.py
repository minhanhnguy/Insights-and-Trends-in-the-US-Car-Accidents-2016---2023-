import pandas as pd

#data = pd.read_csv("US_Accidents_March23.csv")

#data.head(100).to_csv("sample.csv", index=True)

data_sample = pd.read_csv("US_Accidents_March23.csv")

states = {}

for index, row in data_sample.iterrows():
    if row["Start_Time"][0:4] == "2023":
        if row["State"] not in states:
            states[row["State"]] = 1
        else:
            states[row["State"]] += 1

print(states)
    