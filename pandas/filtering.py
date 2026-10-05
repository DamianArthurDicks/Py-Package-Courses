#filtering = keeping the rows that match a condition

import pandas as pd

file_path_csv = "C:\\dev\\PyPackageCourses\\Py-Package-Courses\\pandas\\importing.csv"

df = pd.read_csv(file_path_csv)

#how to select filtered rows
high_HP_pokemon = df[df["HP"] >= 50]

#how to select rows with 2 filtered conditions
#make sure to put each condition in it's own parenthesis
#use | instead of or, & instead of and, ! instead of not because pandas is written in C
water_pokemon = df[(df["Type 1"] == "Water") |
                   (df["Type 2"] == "Water")]
print(water_pokemon)