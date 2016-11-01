#This code doesn't work quite as expected

def Main():
    x = 1
    y = 1
    i = 1
    print(str(i) + ": " + str(x) + "\n")
    i += 1
    print(str(i) + ": " + str(y) + "\n")
    odd = True
    end = False
    while(end == False):
        if(odd == True):
            i += 1
            x += y
            odd = False
            print(str(i) + ": " + str(x))
            print("Type \"exit\" to quit, type anything else to continue")
            input()
        if(odd == False):
            i += 1
            y += x
            odd = True
            print("Type \"exit\" to quit, type anything else to continue")
            print(str(i) + ": " + str(y))
        if(input() == "exit"):
            end = True

if(__name__ == "__main__"):
    Main()