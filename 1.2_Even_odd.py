import sys

if __name__ == "__main__":
    GoOn = "y"
    a = int(input("Hi! Write an integer, please: "))
    b = int(a % 2)
    while GoOn == "y":
        # print("I work.")
        if a == 0:
            print("Number " + str(a) + " is zero.")
        elif b == 1:
            print("Number " + str(a) + " is odd.")
        else:
            print("Number " + str(a) + " is even.")
        GoOn = input("Do you want to continue? y/n: ")
        if GoOn == 'n':
            print("Cya!")
            sys.exit()
        elif GoOn == 'y':
            a = int(input("Write an integer, please: "))
            b = int(a % 2)
            continue
# else:
#   sys.exit()

