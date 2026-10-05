#selection techniques

import pandas as pd

file_path_csv = "C:\\dev\\PyPackageCourses\\Py-Package-Courses\\pandas\\importing.csv"

#index_col is the label for location of row
df_csv = pd.read_csv(file_path_csv, index_col="Name")

#selection by column
#print(df_csv[["Name", "Type 1", "Type 2"]].to_string())

#selection by row/s
#print(df_csv.loc["Bulbasaur"])

#":" is used to slice a range of rows
# the second series is used to return certain columns 
#print(df_csv.loc["Bulbasaur" : "Metapod", ["Type 1", "Type 2"]])

#integer location
#.iloc[start:stop:step, start:stop(for indices of columns)]
print(df_csv.iloc[0:11:2, 0:3])