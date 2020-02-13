import sys
from methods import add, sub, mul, div

if __name__ == "__main__":
    # print(__name__)
    print("Vítam Vás v programe kalkulačka! Budeme spolu sčítavať, odčítať, násobiť a deliť celé a desatinné čísla.")
    GoOn = input("Pre počítanie napíšte 'a', pre ukončenie programu, napíšte 'n': ")
    while GoOn == 'a':
        # print("Super") # Pomocka. Vymazem.
        a = input("Zadajte 1. celé alebo desatinné číslo: ")
        a = float(a)
        act = input("Prosím, vyberte si funkciu. Pre sčítanie '+', pre odčítanie '-', pre násobenie '*' a pre delenie '/': ")
        b = input("Zadajte 2. celé alebo desatinné číslo: ")
        b = float(b)
        if act is '+':
            # print("+") # Pomocka. Vymazem.
            add(a, b)
            GoOn = input("Ak si prajete niečo spočítať, napíšte 'a', ak si prajete ukončiť program, napíšte 'n' a stlačte Enter. ")
            continue
        elif act is '-':
            # print("-") # Pomocka. Vymazem.
            sub(a, b)
            GoOn = input("Ak si prajete niečo spočítať, napíšte 'a', ak si prajete ukončiť program, napíšte 'n' a stlačte Enter. ")
            continue
        elif act is '*':
            # print("*") # Pomocka. Vymazem.
            mul(a, b) # Preco to, plz, musi byt string pri zobrazeni vysledku? Dik. :)
            GoOn = input("Ak si prajete niečo spočítať, napíšte 'a', ak si prajete ukončiť program, napíšte 'n' a stlačte Enter. ")
            continue
        elif act is '/':
            # print("/") # Pomocka. Vymazem.
            div(a, b)
            GoOn = input("Ak si prajete niečo spočítať, napíšte 'a', ak si prajete ukončiť program, napíšte 'n' a stlačte Enter. ")
            continue
        else:
            act = input("Zadali ste nesprávnu hodnotu. Zadajte, prosím '+', '-', '*' alebo '/': ")
            continue
    if GoOn != ('a' and 'n'):
        GoOn = input("Zadali ste zlú hodnotu. Prosím, zadajte 'a' alebo 'n': ")
        # print(GoOn)
        sys.exit() # continue nefunguje. Co tam, plz, dat, aby to slo na zaciatok if-loopu? Dala som tam exit radsej. Dik. :)
    else: # lebo zadal 'n'
        print("Prajem krásny deň!")
        sys.exit()
else: # lebo to nie je funkcia main
    print("Prajem krásny deň!")
    sys.exit()

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
# 	pokracuje v loope