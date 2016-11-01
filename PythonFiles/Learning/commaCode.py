def commaCode(someList):
    someString = ''
    for i in someList:
        if(i == someList[-1]):
            someString += (str(i))
        elif(i == someList[-2]):
            someString += (str(i) + ', and ')
        else:
            someString += (str(i) + ', ')
    return someString
spam = ['apples', 'bananas', 'tofu', 'cats']
print(commaCode(spam))
