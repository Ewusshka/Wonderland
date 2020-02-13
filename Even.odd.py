import sys

if __name__ == "__main__":
    print("Hi!")
    GoOn = input("Do you want to find out, if your number is even or odd? y/n: ")
    a = int(input("Write an integer, please: "))
    # Pyta sa na integer, ak ked nechcem pocitat.
    b = a % 2
    b = int(b)
    while (GoOn != "y") and (GoOn != "n"):
        GoOn = input("You have written a wrong letter. Please write: 'y' or 'n': ")
        # Napise mi: You have written a wrong letter..., ked zadam n
        continue
    else:
        pass
    while GoOn == "y":
        print("I work.")
        if a == 0 :
            print("Number " + str(a) + " is zero.")
            pass
        elif b == (1 or -1):
            print("Number " + str(a) + " is odd.")
            pass
        else:
            print("Number " + str(a) + " is even.")
            pass
        GoOn = input("Do you want to continue? y/n: ")
        a = int(input("Write an integer, please: "))
        # Pyta sa na integer, ak ked nechcem pocitat.
        b = a % 2
        b = int(b)
        continue
    else:
        print("Cya!")
else:
    print("This is not __main__. It will not work.")
    sys.exit()

