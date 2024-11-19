import pandas

mydataset={
    'Cars': ["Volvo", "BMW", "Ford"],
    'passings': [3, 7, 12]
    
}

myvar = pandas.DataFrame(mydataset)

print(myvar)


#printing a cross
def print_x_pattern(n):
    for i in range(n):
        for j in range(n):
            if j == i or j ==n - i - 1:
                print('*', end='')
            else:
                print(' ', end='')
        print()

print_x_pattern(8)