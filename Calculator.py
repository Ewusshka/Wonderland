import sys

print("Vítam Vás v programe kalkulačka! Budeme spolu sčítavať, odčítať, násobiť a deliť celé a desatinné čísla.")

GoOn = input(("Ak si prajete niečo spočítať, napíšte 'a', ak si prajete ukončiť program, napíšte 'n' a stlačte Enter. ") 
if GoOn is 'n':
	print("Prajem krásny deň! Zas niekedy nabudúce spočítam, čo sa Vám bude páčiť. :)"
	break
elif GoOn is 'a':
	a,b = (float(x) for i in input("Prosím zadajte 2 čísla, s ktorými chcete počítať a oddeľte ich " " (medzerou).").split())
	act = ("Prosím, vyberte si funkciu. Pre sčítanie napíšte '+', pre odčítanie napíšte '-', pre násobenie vypíšte '*' a pre delenie vypíšte '/'.")
	if act is '+':
		add(a, b)
		continue
	elif act is '-':
		sub(a,b)
		continue
	elif act is '*':
		mul(a,b)
		continue
	elif act is '/':
		div(a,b)
		continue
	else:
		print("Zadali ste nesprávnu hodnotu.")
		continue #Prepodkladam, ze vrati na zaciatok medzi-loopu"
else:
	print("Zadali ste nesprávnu hodnotu. Prosím, zadajte 'a' alebo 'n'. ")
	continue
	#pokracuje v loope

#Spravim funkciu, ktora scita. Zoberiem premennu a, b z inputu, scitam to a ulozim do c.
def add(a, b)
	c = return a + b
	print("Výsledok je: " + c)
def sub(a, b)
	c = return a - b
	print("Výsledok je: " + c)
def mul(a, b)
	c = return a * b
	print("Výsledok je: " + c)
def div(a, b)
	c = return a / b
	print("Výsledok je: " + c)