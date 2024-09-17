import pandas

mydataset={
    'Cars': ["Volvo", "BMW", "Ford"],
    'passings': [3, 7, 12]
    
}

myvar = pandas.DataFrame(mydataset)

print(myvar)