#DataFrame = A tabular data structure with rows and columns.(2 dimensional)

import pandas as pd

data = {
    "name" : ["Jeff", "George", "Shaun"],
    "age": [21, 69, 67]
    }

df = pd.DataFrame(data, index=["Gardener", "Private Chef", "Butler"])

#to acces location by label
#print(df.loc["Butler"])

#add new column
df["work hours"] =  [6, 4, 8]

#add new row(each dictionary represents a new row)
#create a new dictionary then concatinate
new_rows = pd.DataFrame([{"name" : "drake", "age" : 25, "work hours" : 12},
                        {"name" : "dr. dre", "age" : 43, "work hours" : 10}],
                       index=["maid", "personal physician"])
df = pd.concat([df, new_rows])
print(df)