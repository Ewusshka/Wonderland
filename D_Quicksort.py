l = [int(x) for x in input("Write integers (divided by space) to order: ").split()]
length = len(l)
print('length', length)
div = l[length - 1]                 # last element of the list 'l' will be a divider 'div'
print('divider', div)
smaller = []
bigger = []
same = []
final = [0] * length                # I have created a chain of 0, to be able to change any index into number
print(len(final))
print('smaller, bigger, final', smaller, bigger, final)
i = 0                               # index of the number to compare to div, continuously with loop it will rise
for x in range(length - 1):         # length minus 'div' minus '0 index'
    a = l[i]
    print(a)
    if a < div:                     # divide the chain into 3: smaller, bigger and the same group
        smaller.append(a)
    elif a > div:
        bigger.append(a)
    elif a is div:
        same.append(a)
    i = i + 1
print('smaller, bigger, same, final', smaller, bigger, same, final)
lensmaller = int(len(smaller))
print('lensmaller', lensmaller)
final[lensmaller] = [div]
print(final)
if same is not []:                  # if the 'same' has 1+ elements, we will add it/them behind 'div' into 'final'
    lensame = int(len(same))
    same1 = lensmaller + 1
    same2 = lensmaller + 1 + lensame
    print('same1, same2', same1, same2)
    final[same1:same2] = [div] * lensame    # ako tam pridam hodnotu 'div'u lensame krat?
print('lensame', lensame)
print('smaller, bigger, final', smaller, bigger, final)
# if len(smaller) is 1:
#    print("smaller hotovo")
#    final.append(smaller)               # zle! chceme zaradit dopredu, kuk extend append
# if len(bigger) is 1:
#    print("bigger hotovo")
#    final.append(bigger)                # kuk extend append
"""for x in range(len(smaller) - 2):
    d = smaller[len(smaller) - 1]
    i = 0
    a = smaller[i]
    if a < div:
        smaller.append(a)
    elif a > div:
        bigger.append(a)
    elif a is div:
        final.append(a)
    i = i + 1"""