import pandas as pd
# Create a DataFrame with multi-index
df = pd.DataFrame({'Name': ['John', 'Anna', 'Peter'],
                   'City': ['NY', 'NY', 'LA'],
                   'Age': [23, 29, 21]})
df.set_index(['City', 'Name'], inplace=True)

print(df)
