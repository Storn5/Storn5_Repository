#Guessing the number game
import random

#Game function, takes a number as argument
def game(number):
    #The number of guesses
    guesses = 0
    print('I am thinking of a number between 1 and 20.')
    #The game loop starts here
    while(True):
        #Each time the player guesses, the number of guesses goes up
        guesses += 1
        try:
            guess = input('Take a guess.\n')
            #Show if the number guessed is higher, lower or the same as the required number
            if(int(guess) < number):
                print('Your guess is too low.')
                continue
            elif(int(guess) > number):
                print('Your guess is too high.')
                continue
            else:
                print('Good job! You guessed my number in ' + str(guesses) + ' guesses!')
                break
        #If the entered number is not an integer, try again
        except:
            print('You have to enter a whole number between 1 and 20. Try again!')
            #This wasn't a fair guess if an integer wasn't entered
            guesses -= 1
            continue
        
#Generate a random number between 1 and 20 and start the game
game(random.randint(1, 20))
