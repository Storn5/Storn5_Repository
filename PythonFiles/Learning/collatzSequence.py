#Collatz sequence
def collatz(number):
    originalNumber = number
    steps = 0
    while(True):
        print(str(number))
        if(number == 1):
            print('It took ' + str(steps) + ' steps for ' + str(originalNumber) + ' to come down to 1.')
            break
        elif(number < 1):
            print('Please, enter a number higher than or equal to 1.')
            break
        else:
            if(number % 2 == 0):
                number = number // 2
                steps += 1
                continue
            elif(number % 2 == 1):
                number = number * 3 + 1
                steps += 1
                continue

while(True):
    try:
        n = int(input('Enter a whole number greater than or equal to 1 (Enter 0 to stop): '))
        if(n == 0):
            print('Thank you for using this Collatz Sequence program!')
            break
        else:
            collatz(n)
    except ValueError:
        print('You have to enter a whole number.')
