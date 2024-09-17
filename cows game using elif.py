print("Welcome to My Cows Game!")

playing = input("Do you want to play the cows game? ")

if playing.lower() != "yes":
    quit()

print("Let's start the game!")
score = 0

answer = input("What is the Kalenjin name for a cow with big ears? ")
if answer.lower() == "cheboit":
    print("Correct!")
    score += 1
elif answer.lower() == "wrong_guess":
    print("Close, but not quite!")
else:
    print("Try again!")

answer = input("What is the Kalenjin name of a cow with a white head? ")
if answer.lower() == "lelmet":
    print("Correct!")
    score += 1
elif answer.lower() == "another_wrong_guess":
    print("You're almost there!")
else:
    print("Try again!")

# The rest of your code would follow similarly...

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + " %")
