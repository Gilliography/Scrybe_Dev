names=["James", "John", "Allan", "Orenge"]
print("Original list is:", names)

#Using Append method to add elements to a list
#append function takes only one argument as seen below
names.append("Michuki")
print("Updated list is:", names)

#Using insert() function to add elements into a list
names.insert(5, "Mwakazi")
print("The list with newly inserted name is", names)

#Printing a name in a specific index
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])
print(names[5])

#Adding elements to a list from other iterables using extend() function
cows=["Cheboit", "Cheptilit", "Ringas", "Tuimet"]
new_cows=("Tumbo", "Mardad", "Chepsoimet")
cows.extend(new_cows)
print("Updated cow names is:", cows)

# Changing list items using "=" operator
colors = ["Blue", "Red", "Green"]
print("The original list of colors is:", colors)

# Changing the third color
colors[2] = "Maroon"
print("Updated list of colors is:", colors)

