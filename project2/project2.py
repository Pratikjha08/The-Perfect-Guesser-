#The Perfect Guesser


import random 
randNumber = random.randint(1,100)
userGuess = None
guesses = 0

while(userGuess != randNumber):
    userGuess = int(input("Enter your Guess: "))
    guesses += 1
    if (userGuess==randNumber):
        print("You Guessed Right Number!")
    else:
        if(userGuess>randNumber):
            print("You Guessed Wrong Number!")
            print("Enter a smaller number")
        elif(userGuess<randNumber):
            print("You Guessed Wrong Number!")
            print("Enter a larger number")
       

print(f"You guessed number in {guesses} guesses")

with open("project2/hiscore.txt", "r") as f:
    hiscore = int(f.read())

if (guesses<hiscore):
    print("You have broken the high score")
    with open("project2/hiscore.txt", "w") as f:
        f.write(str(guesses))