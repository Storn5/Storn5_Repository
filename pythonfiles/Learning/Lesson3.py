print('Enter your name:')
name = input()
print('Hello, ' + name)
while True:
    try:
        print('Enter your age:')
        age = input()
        print('You will be ' + str(int(age) + 1) + ' in a year')
    except ValueError:
        print('You have to enter a whole number as your age.')
        continue
    else:
        break
print('The length of your name is ' + str(len(name)))
print('The length of your age is ' + str(len(age)))
