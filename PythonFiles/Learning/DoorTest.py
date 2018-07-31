import random

def main():
    #Number of times the player won or lost when stayed or changed door
    stayedWins, stayedLosses, changedWins, changedLosses = 0, 0, 0, 0
    #Input the number of iterations
    n = int(input('How many iterations: '))
    #Main loop
    for i in range(n):
        correctDoor = random.randint(1, 3)
        chosenDoor = int(input('Which door do you choose (1/2/3): '))
        for i in range(1, 4):
            if not i == correctDoor and not i == chosenDoor:
                revealedDoor = i
                break
        for i in range(1, 4):
            if not i == chosenDoor and not i == revealedDoor:
                doorToChange = i
                break
        print('The host reveals that a goat was hiding behind door ' + str(revealedDoor) + '! Now, only doors ' + str(chosenDoor) + ' and ' + str(doorToChange) + ' are left, and behind one of them you\'ll find a car!')
        choice = input('Do you stay or do you change (stay/change): ').strip()
        if choice == 'stay':
            print('You\'ve stayed at door ' + str(chosenDoor) + '.')
            if chosenDoor == correctDoor:
                print('You find a car! You\'ve won!')
                stayedWins += 1
            else:
                print('You find a goat. You\'ve lost!')
                stayedLosses += 1
        else:
            print('You\'ve changed to door ' + str(doorToChange) + '.')
            if doorToChange == correctDoor:
                print('You find a car! You\'ve won!')
                changedWins += 1
            else:
                print('You find a goat. You\'ve lost!')
                changedLosses += 1

    #The final win/lose count
    print('Stayed win/loss percentage: ' + str(100*(stayedWins/(stayedWins+stayedLosses))) + '%\nChanged win/loss percentage: ' + str(100*(changedWins/(changedWins+changedLosses))) + '%')
    if input('Try again (yes/no): ').strip() == 'yes':
        main()
if __name__ == '__main__':
    main()