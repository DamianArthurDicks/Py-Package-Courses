#importing json and csv files

import pandas as pd

file_path_csv = "C:\\dev\\PyPackageCourses\\Py-Package-Courses\\pandas\\importing.csv"

file_path_json = "C:\\dev\\PyPackageCourses\\Py-Package-Courses\\pandas\\importing.json"

df_csv = pd.read_csv(file_path_csv)

df_json = pd.read_json(file_path_json)

#.to_string() prints the entire csv/json file
#be careful when this with big amounts of data
print(df_json.to_string())