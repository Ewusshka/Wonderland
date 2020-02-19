import sys

GoOn = 'y'
while GoOn is 'y':
    # students = []
    # how to store the list of names and grades? for cycle? array appending?
    name = input("Enter student's name: ")
    m = int(input('Enter points from math: '))
    p = int(input("Enter points from physics: "))
    c = int(input("Enter points from chemistry: "))
    # students.append(name, m, p, c)
    if m < 36:
        print(str(name) + " has failed math, his/her score is: " + str(m))
    if p < 36:
        print(str(name) + " has failed physics, his/her score is: " + str(p))
    if c < 36:
        print(str(name) + " has failed chemistry, his/her score is: " + str(c))
    if (m < 36) or (p < 36) or (c < 36):
        sys.exit()
    else:
        print("Congratulations! You have passed!")
    a = (m + p + c)/ 3
    if a < 60:
        print("Your average is " + str(a) + " points, your grade is C.")
    elif a < 70:
        print("Your average is " + str(a) + " points, your grade is B.")
    else:
        print("Your average is " + str(a) + " points, your grade is A.")
    GoOn = input("Enter 'y' to continue or 'n' to stop: ")
else:
    sys.exit("Thank you!")
