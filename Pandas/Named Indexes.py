import pandas as pd

data= {
    "calories": [400, 450, 500],
    "duration": [20, 30, 40]

}

df=pd.pandas.DataFrame(data, index=["Day1", "Day2", "Day3"])
print(df)
print(df.loc["Day2"])


students={
    "f_names": ["Joseph", "James", "Jack"],
    "s_name": ["Franklin", "Brown", "Olyphant"]
    }

df=pd.pandas.DataFrame(students, index=["500", "450", "456"])

print(df)



