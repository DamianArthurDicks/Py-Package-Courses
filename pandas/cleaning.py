#Data cleaning = the process of fixing/removing incomplete, incorrect, or irrelevant data.
#~75% of work done with pandas is data cleaning

import pandas as pd 

file_path_csv = "C:\\dev\\PyPackageCourses\\Py-Package-Courses\\pandas\\importing.csv"

df = pd.read_csv(file_path_csv)

#1. drops columns

#df = df.drop(columns=["Total"])

#2. handle missing data

#drops empty rows within selected columns 
#df = df.dropna(subset=["Type 2"])

#fills empty columns
#df = df.fillna({"Type 2": "None"})

#3. fix incosistent values
#df["Type 1"] = df["Type 1"].replace({"Normal" : "Regular"})

#4. Standardize text
#df["Name"] = df["Name"].str.lower()

#5. fix data types
#recommended for when having data with a 2 base number system
#df["Type 2"] = df["Type 2"].astype(bool)

#6. remove duplicate values
#df = df.drop_duplicates()

print(df.to_string())