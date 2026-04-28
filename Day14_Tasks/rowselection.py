""" Row Selection & Deletion 
A DataFrame: 
df = pd.DataFrame({ 
"A": [10, 20, 30], 
"B": [5, 15, 25] 
}, index=["x", "y", "z"]) 
Task: 
● Select row with index "y" 
● Delete row "x" 
● Print updated DataFrame """

import pandas as pd

df = pd.DataFrame({"A": [10, 20, 30], "B": [5, 15, 25]}, index=["x", "y", "z"])
print("original data:\n", df)

df = pd.DataFrame(df)
print("\nRow Selection(y):\n", df.loc['y'])

df = df.drop('x')
print("\nDeleting row(x):\n", df)

print("\nupdated DataFrame:\n", df)
