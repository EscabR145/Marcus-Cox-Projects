from pydoc import doc
import random as rand

class GuessGame():
    def __init__(self):
        pass
       
    def RunGame(self,user_Guess):
        #Generate random number between 1 - 10
        randomNumber = rand.randint(1,10)
        result = " "
        #Check against user guess
        if user_Guess == randomNumber:
            return "Congratulations Thats Correct"
        else:
            return f"Incorrect Try Again, Number was {randomNumber}."
       

#Welcome Message
print("Welcome to My Guessing Game, Try and Guess My Number in 3 tries")

# Do While
while(1):
    #Get user input
    print("Generating Number...")
    user_Input = int(input("Enter your Guess: "))
    game = GuessGame()
    print(game.RunGame(user_Input))
    again = input("Play Again? Y/N: ")
    if again == 'n' or again == 'N':
        break




   


    