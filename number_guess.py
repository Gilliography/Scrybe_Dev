import random

top_of_range=input("type a number: ")
if top_of_range.isdigit():
    top_of_range=int(top_of_range)
    if top_of_range <= 0:
        print("Enter a number greater than 0 next time. ")
        quit()
else:
    print("Enter a number next time.")
    quit()

random_number=random.randint(0, top_of_range)
guesses=0
while True:
    guesses+=1
    user_guess=input("Make a guess: ")
    if user_guess.isdigit():
        user_guess=int(user_guess)
    else:
        print("Please type a number next time.")
        continue
    if random_number ==user_guess:
        print("You got it")
        break
    else:
        if user_guess > random_number:
            print("You were above the number!")
        else:
            print("You were below the number!")
print("You got it in", guesses, "guesses")
