l = [int(x) for x in input("Write integers (divided by space) to order: ").split()]
length = len(l)
print('length', length)
div = l[length - 1]                 # last element of the list 'l' will be a divider 'div'
print('divider', div)
smaller = []
bigger = []

i = 0                               # index of the number to compare to div, continuously with loop it will rise
for x in range(0, length-1):         # length minus 'div' minus '0 index'
    a = l[i]
    print(a)
    if a > div:
        l[i] = div
        l[length-1] = a
        print(l)
    i = i + 1
print('list', l)

for s in range(0, div-1):
    smaller.append(l[s])
# ZLE: nie div, ale pozicia div, plati aj na 24.riadok
print('smaller', smaller)
for b in range(div+1, length):
    bigger.append(l[b])
print('bigger', bigger)
print(l)