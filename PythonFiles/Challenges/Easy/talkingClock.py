def main():
    strTime = input("Enter the time (HH:MM): ")
    hour, minute = int(strTime[:2]), int(strTime[3:])
    if hour <= 11:
        am = True
    else:
        am = False
    if not hour == 12 and not am:
        hour -= 12
    elif am and hour == 0:
        hour = 12
    print("It's " + str(hour) + ":" + str(minute) + " am") if am else print("It's " + str(hour) + ":" + str(minute) + " pm")

if __name__ == "__main__":
    main()