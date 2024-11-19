import pandas as pd

file_path = r'C:\Users\1030 g2 new version\Documents\Python Projects\Pandas\data.csv'
df = pd.read_csv(file_path)

df.loc[7, 'Duration']=45
print(df.duplicated)

print(df)