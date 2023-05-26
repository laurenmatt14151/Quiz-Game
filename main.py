#Welcome to game message
print("Welcome!")

#Ask if they want to play
playing = input("Do you want to take my Algebra quiz? Yes or No: ")

#Check if answer is yes .lower prints all lowercase
if playing.lower() != "yes":
    print("Okay, goodbye!")
    quit()
print("Good Luck!")

#Keep track of score
score = 0

#Questions
answer = input("#1) 2x + 3 = 13. x = ")
if answer == "5":
    print("Correct!")
    score += 1
else:
    print("Sorry, this is incorrect :(")
    
answer = input("#2) 3^x = 27. x =  ")
if answer == "3":
    print("Correct!")
    score += 1
else:
    print("Sorry, this is incorrect :(")
    
answer = input("#3) x/3 + 10 = 15. x =  ")
if answer == "15":
    print("Correct!")
    score += 1
else:
    print("Sorry, this is incorrect :(")
    
#Display score
print("You answered " + str(score) + "/3 correct. You got a " + str((score/3)*100) + "%")
