import random

# a = [int(x) for x in input("Write the first list of numbers divided by ' ': ").split()]
# b = [int(y) for y in input("Write the second list of numbers divided by ' ': ").split()]
a = [random.randint(0, 20) for i in range(8)]
b = [random.randint(0, 20) for i in range(7)]
print(a)
print(b)
final = []
i = 0
for x in range(4):
    c = b[i]
    if c in a:
        final.append(c)
    i = i + 1
print(final)


