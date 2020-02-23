lst = [int(x) for x in input("Please, write numbers divided by ' ': ").split()]
# print(lst)
l = int(input("Write a number to be the upper limit of the list: "))
a = [int(y) for y in lst if y < l]
print(a)