import pandas as pd

df=pd.DataFrame(
    {"a": [4, 5, 6],
     "b": [7, 8, 9],
     "c": [10, 11, 12]},
    index=[1, 2, 3])

print(df)


df=pd.DataFrame({'Bobby': ['I liked it so much.', 'It was awful'],
              'Sue':['Pretty good to hear that', 'Bland'],},
              index=['Product A','Product B'])

print(df)