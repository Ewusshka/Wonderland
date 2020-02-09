import sys
import methods

# not necessary in our case but why is good to use the following you may check here: https://stackoverflow.com/a/419189/7374363
if __name__ == "__main__":
	print(__name__)
	print("Vítam Vás v programe kalkulačka! Budeme spolu sčítavať, odčítať, násobiť a deliť celé a desatinné čísla.")
	methods.add(1,2)
	# while podminka: loop musi byt tady
		# GoOn = input("Ak si prajete niečo spočítať, napíšte 'a', ak si prajete ukončiť program, napíšte 'n' a stlačte Enter. ")
		# if GoOn == 'n':
		# 	print("Prajem krásny deň! Zas niekedy nabudúce spočítam, čo sa Vám bude páčiť. :")
		# 	exit(0)
		# elif GoOn is 'a':
		# 	a,b = (float(x) for i in input("Prosím zadajte 2 čísla, s ktorými chcete počítať a oddeľte ich " " (medzerou).").split())
		# 	act = ("Prosím, vyberte si funkciu. Pre sčítanie napíšte '+', pre odčítanie napíšte '-', pre násobenie vypíšte '*' a pre delenie vypíšte '/'.")
		# 	if act is '+':
		# 		add(a, b)
		# 		continue
		# 	elif act is '-':
		# 		sub(a,b)
		# 		continue
		# 	elif act is '*':
		# 		mul(a,b)
		# 		continue
		# 	elif act is '/':
		# 		div(a,b)
		# 		continue
		# 	else:
		# 		print("Zadali ste nesprávnu hodnotu.")
		# 		continue #Prepodkladam, ze vrati na zaciatok medzi-loopu"
		# else:
		# 	print("Zadali ste nesprávnu hodnotu. Prosím, zadajte 'a' alebo 'n'. ")
		# 	continue
		# 	#pokracuje v loope

# #Spravim funkciu, ktora scita. Zoberiem premennu a, b z inputu, scitam to a ulozim do c.
# def add(a, b)
# 	c = return a + b
# 	print("Výsledok je: " + c)
# def sub(a, b)
# 	c = return a - b
# 	print("Výsledok je: " + c)
# def mul(a, b)
# 	c = return a * b
# 	print("Výsledok je: " + c)
# def div(a, b)
# 	c = return a / b
# 	print("Výsledok je: " + c)