# Import pandas package
import pandas as pd
 
# Define a dictionary containing employee data
data = {'Name':['Gilbert', 'Joan', 'Patrick', 'Sheila'],
        'Age':[27, 24, 22, 32],
        'Address':['New York', 'Washington', 'San Francisco', 'Texas'],
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']}
 
# Convert the dictionary into DataFrame 
df = pd.DataFrame(data)
 
# select two columns
print(df[['Name', 'Address', 'Qualification']])
