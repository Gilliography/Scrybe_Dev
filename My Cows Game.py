print("Welcome to My Cows Game!")

playing=input("Do you want to play the cows game? ")

print(playing)
if playing.lower()!="yes":
    quit()
print("Let's start the game!")
score=0

answer=input("What is the Kalenjin name for a cow with big ears? ")
if answer.lower()=="cheboit":
    print("correct!")
    score += 1
else:
    print("try again!")

answer=input("What is the Kalenjin name of a cow with a white head? ")
if answer.lower()=="lelmet":
    print("correct!")
    score += 1
else:
    print("try again")

answer=input("What is the Kalenjin name of a cow with a cut in the ear? ")
if answer.lower()=="cheptilit":
    print("correct!")
    score += 1
else:
    print("try again")

answer=input("What is the Kalenjin name of a cow with black head? ")
if answer.lower()=="tuimet":
    print("correct")
    score += 1
else:
    print("try again!")

print("You got " +str(score) +" questions correct!")
print("You got " +str((score /4)*100) +"%")