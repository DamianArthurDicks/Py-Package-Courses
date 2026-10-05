import pandas as pd

#series -> is an array with index's that can hold any type of data
data = [100, 102, 104]

calories = {"day 1" : 1800, "day 2" : 1720, "day 3" : 1678}

series = pd.Series(calories)

#you can change the names of the columns/index in the array
#series = pd.Series(data, index=["a", "b", "c"])

#this is how to access the location of the index by label
#series.loc["a"] = 95
#print(series.loc["a"])
series.loc["day 3"] += 500

#this is how to access the integer location of index
#print(series.iloc[1])
#print(series)

#to return data that meets conditions
#print(series[series > 100])

print(series)