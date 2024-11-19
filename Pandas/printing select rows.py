import pandas as pd 

data = {
    'Name':["James", "Lawson", "Smith"],
    'Age': [23, 30, 34],
    'Qualification': ["Bachelors", "Masters", "PhD"],
    'Location': ["Nairobi", "Eldoret", "Kitale"]
    }

df=pd.DataFrame(data)
print(data)

print(df[['Name',  'Qualification']])