def Main():
    #decimal - (binary - 62mal) (whole numbers only)
    str1 = input("Type a number in decimal: ")
    str2 = input("\nType the number of the base to convert to: ")
    output = ""
    num = int(str1)
    base = int(str2)
    numsAboveNine = {10:"a", 11:"b", 12:"c", 13:"d", 14:"e", 15:"f", 16:"g", 17:"h", 18:"i", 19:"j", 20:"k", 21:"l", 22:"m", 23:"n", 24:"o", 25:"p", 26:"q", 27:"r", 28:"s", 29:"t", 30:"u", 31:"v", 32:"w", 33:"x", 34:"y", 35:"z", 36:"A", 37:"B", 38:"C", 39:"D", 40:"E", 41:"F", 42:"G", 43:"H", 44:"I", 45:"J", 46:"K", 47:"L", 48:"M", 49:"N", 50:"O", 51:"P", 52:"Q", 53:"R", 54:"S", 55:"T", 56:"U", 57:"V", 58:"W", 59:"X", 60:"Y", 61:"Z"}
    if(num >= 1):
        while(num >= 1):
            if(num % base >= 10):
                output = numsAboveNine[num % base] + output
                num //= base
            else:
                output = str(num % base) + output
                num //= base
    elif(num == 0):
        output = "0"
    elif(num <= -1):
        num *= -1
        while(num >= 1):
            output = str(num % base) + output
            num //= base
        output = "-" + output
    print("\n\n" + str1 + " in base " + str2 + " is: " + output)

if(__name__ == "__main__"):
    Main()