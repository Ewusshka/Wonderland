import sys
import numpy as np

GoOn = 'y'
students = np.array([])
while GoOn is 'y':
    name = input("Enter student's name: ")
    m, p, c = [int(x) for x in input('Points from math, physics, chemistry (divided by space bar): '). split()]
    if m < 36:
        print(str(name) + " has failed math, his/her score is: " + str(m))
    if p < 36:
        print(str(name) + " has failed physics, his/her score is: " + str(p))
    if c < 36:
        print(str(name) + " has failed chemistry, his/her score is: " + str(c))
    if (m < 36) or (p < 36) or (c < 36):
        students = np.append(students, [name, m, p, c, 0, 'Failed'])
        print(students)
        GoOn = input("Enter 'y' to continue or 'n' to stop: ")
        continue
    else:
        print("Congratulations! You have passed!")
    a = (m + p + c)/ 3
    if a < 60:
        print("Your average is " + str(a) + " points, your grade is C.")
        students = np.append(students, [name, m, p, c, a, 'C'])
    elif a < 70:
        print("Your average is " + str(a) + " points, your grade is B.")
        students = np.append(students, [name, m, p, c, a, 'B'])
    else:
        print("Your average is " + str(a) + " points, your grade is A.")
        students = np.append(students, [name, m, p, c, a, 'A'])
    print(students)
    # I would like to make a MATRIX out of the results.
    GoOn = input("Enter 'y' to continue or 'n' to stop: ")
else:
    sys.exit("Thank you!")
