a = int(input("Write a number to divide: "))
divisors = list(range(2, a + 1))
divList = []
for x in divisors:
    if a % x == 0:
        divList.append(x)
print(divList)