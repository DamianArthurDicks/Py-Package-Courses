#aggregate functions = reduces a set of values into a single summary value
#                      used to summarize and analyze data, often used with groupby() function

import pandas as pd 

file_path_csv = "C:\\dev\\PyPackageCourses\\Py-Package-Courses\\pandas\\importing.csv"

df = pd.read_csv(file_path_csv)

#whole dataframe aggregate functions
#the kwarg "numeric_only" analyzes the data that are numeric only 
#returns the mean value of columns 
#print(df.mean(numeric_only=True))

#returns the sum value of the columns
#print(df.sum(numeric_only=True))

#returns the minimum value of the columns
#print(df.min(numeric_only=True))

#returns the maximum value of the columns
#print(df.max(numeric_only=True))

#returns the number of values in each column columns
#print(df.count())

#single column aggregate functions
#columns are slected so kwargs aren't needed
#print(df["Total"].mean())
#print(df["Total"].sum())
#print(df["Total"].min())
#print(df["Total"].max())
#print(df["Total"].count())

#groupby() = groups by selcted data
#you can use aggregate functions on groupby() data
#pokemons are grouped by Type 1 and are selected by HP to calculate the mean of each groups HP
group = df.groupby("Type 1")
print(group["HP"].mean())
