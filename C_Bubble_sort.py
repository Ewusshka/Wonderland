a = [int(x) for x in input("Write numbers (divided by space): ").split()]
# zoberie prve dve, porovna a vymeni ak vlavo je vacsie
# zoberie druhe dve, porovna a vymeni ak vlavo je vacsie
# ... robi az po posledny index
# zacne zas zlava... pokracuje, kym sa nestane, ze sa nic nezmeni
# print

print(a)
length = len(a)
i = int(0)
j = int(1)
for x in range(length - 1):
    # b = a
    while j != length:              # The loop compares 1.& 2. value (then 2+3, 3+4, 4+5, ...)
        prva = a[i]
        druha = a[j]
        if prva > druha:            # It compares the values next to each other.
            del (a[i])              # If the second is bigger, it will switch them.
            a.insert(i, druha)
            del (a[j])
            a.insert(j, prva)
        i = i + 1
        j = j + 1
        # print("Round.")
    if j is length:                 # With every finished round, we begin the loop once more.
    if j is length:                 # With every finished round, we begin the loop once more.
        i = int(0)
        j = int(1)
        # c = a
        # print("Thank you.")
#   if c is b: break
# I wanted to stop the loop, if the list at the beginning is the same as at the end 'b = c', but this way does not work.
print(a, "This is an ordered list.")