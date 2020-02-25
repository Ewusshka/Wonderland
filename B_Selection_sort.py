import sys

a = [int(x) for x in input("Write numbers (divided by space): ").split()]
print(a)
length = len(a)
i = int(0)
for i in range(length - 1):         # for loop continues (length - 1) number of times
                                    # every time caring only about last 'length', (length - 1, length - 2, ...) numbers
    mina = min(a[i:length])
    # print(mina)
    mini = a.index(mina)
    # print(mini)
    i0 = a[i]
    # print(i0)
    del(a[i])                       # delete value at index 0
    # print(a)
    a.insert(i, mina)               # insert on index '0', (1, 2, ...) min value
    # print(a)
    del(a[mini])                    # delete value at index
    # print(a)
    a.insert(mini, i0)              # insert value of index '0', (1, 2, ...) at index of min
    i = i + 1
    print(a)                        # so: I have exchanged the numbers on index '0', (1, 2, ...) with the min
    # There is a possibility to stop the loop, when 2 chains after one another are the same.
print("Thank you.")