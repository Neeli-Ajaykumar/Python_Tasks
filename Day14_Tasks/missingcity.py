"""Missing City Data (NaN Handling) 
A dataset contains city populations: 
cities = {"Delhi": 2000000, "Mumbai": 3000000, "Chennai": 1500000} 
Scenario: 
You want data for: 
["Delhi", "Chennai", "Bangalore"] 
Task: 
● Create a Series with the above index 
● Identify which cities have missing values (NaN) """

import pandas as pd

cities = pd.Series({"Delhi": 2000000, "Mumbai": 3000000, "Chennai": 1500000}) 
print(cities)

new_cities = cities.reindex(["Delhi", "Chennai", "Bangalore"])
print("\nReindexed Series:\n", new_cities)

missing_values = new_cities.isnull()
print("\nMissing Values:\n", missing_values)
