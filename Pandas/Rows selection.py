import pandas as pd 

data = pd.read_csv(r"C:\Users\1030 g2 new version\Documents\Python Projects\Pandas\nba.csv", index_col="Name")

first = data.loc["Avery Bradley"]
second = data.loc["R.J. Hunter"]

print(first, "\n\n\n", second)