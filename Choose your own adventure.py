name= input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer=input("You are on a dirt road, it has come to the end and you can only go left or right. Which way would you like to go? ").lower()

if answer=="left":
    answer=input("You have come to a river, you can walk around it or swim across? Type walk to walk around and swim to swim accross: ")
    if answer=="swim":
        print("You attempted to swim and was eaten by an alligator! ")

    elif answer == "walk":
        print("You walked around the river with nothing to show for it. You lost the game! ")

    else:
        print("Not a valid option. You lose.")

elif answer=="right":
    answer=input("Here is the bridge. Do you want to cross it? cross/back ")
        
    if answer=="back":
        print("You returned to the beginning ! ")

    elif answer == "cross":
        answer=input("You crossed the river and met a stranger. Do you want to talk to him or move ahead? yes/no? ")
        if answer=="yes":
            print("You talked to the stranger and they gave you gold. You WIN!")
        
        elif answer=="no":
            print("You avoided the stranger and you lost the opportunity to grab gold:)")
        else: 

            print("Not a valid option. You lose.")
       
    else:
        print("Not a valid option. You lose.")

else:
    print("Not a valid option. You lose.") 

print("Thank you for trying", name)