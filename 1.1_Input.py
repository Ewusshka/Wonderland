name = input("Please, enter your name: ")
age = int(input("Please, enter your age: "))
yrs = 100 - age
yr = 2020 + yrs
print("Dear " + name + ", you will turn 100 in " + str(yr) + "!")
phrase = "Dear " + name + ", you will turn 100 in " + str(yr) + "!"
times = int(input("How many times do you want to print the line? "))
phrases = [times * phrase]
for i in range(times):
    print(phrase)
# 1. SEPARATES A LETTER PER LINE: print(*phrase, sep='\n')
# 2. DOES NOT WORK: TypeError: 'int' object is not iterable
# for i in times:
#    print(phrase)
# 3.