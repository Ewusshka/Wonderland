import sys
from methods import add, sub, mul, div

if __name__ == "__main__":
    print("Vítam Vás v kalkulačke!")
    GoOn = input("Chcete pokračovať? a/n : ")
    # pokud zadam cokoliv jineho nez 'a' tak program skonci, co se ma tedy stat pokud zadam 'n'?
    # EV: Ja som 'n' bolo opatrene mala, si mi to vymazal. :) Bola som v tom, ze to bolo dokonca funkcne,
    # EV: ale mozno som to dostatocne netestovala. Myslienka bola, ze pokial je
    # EV: 1. "while GoON = a", tak pocita,
    # EV: 2. ak nie je (if) ani 'a' ani 'n', tak vypise, ze to je zle, zobere si nove GoOn a hodi na zaciatok
    # EV: 3. a ak nie je ani 'a', ani nie je ani 'a' ani 'n', tak (else: ), cize ostava len to, ze je 'n', povie "Cya" a program ukonci.
    # EV: Menim to teda nasledovne. line 14-20.
    if GoOn not in ['a', 'n']:
        GoOn = input("Zadali ste zlú hodnotu. Prosím, zadajte 'a' alebo 'n': ")
        pass
        # EV: Ako to, prosim, mozem vratit spat na zaciatok podmienky? Ci to nejde, plz? "continue" mi nedovoli napisat a asi vie preco. :D
    if GoOn == 'n':
        print("Prajem krásny deň!")
        sys.exit()
    while GoOn == 'a':
        a = float(input("Zadajte 1. celé alebo desatinné číslo: "))
        act = input("Vyberte si funkciu. '+', '-', '*', '/': ")
        if act not in ['+','-','*','/']:
            print('Neznámá operace')
            act = input("Vyberte si funkciu. '+', '-', '*', '/': ")
            continue
        b = input("Zadajte 2. číslo: ")
        b = float(b)
        # c = None
        if act is '+':
            add(a, b)
            # print("Výsledok je: " + str(c))
        elif act is '-':
            sub(a, b)
        elif act is '*':
            mul(a, b)
            # -  Mimochodem pro prehlednost by vypisovani vysledku melo byt zde nikoli v methods.py. Metody by mely vracet pouze vysledek, nic vic
            # EV: Ked to zmazala z methods.py 'print...' a dala do riadku 46 sem, identation 2, premennu c to nepoznalo.
            # EV: Ked som zadala do 30. riadku 'c = None', tak vypisalo po vypocte None.
            # EV: Ked som zadala hned za funkcie v 'if'cykle print, l. 33, indentation 3, tiez to nespoznalo 'c'.
            # EV: PROGRAM NEPREBERIE PREMENNU "c" Z INEHO skriptu? Na to je PRIKAZ?
            # EV: Ja teda radsej vraciam print spat do methods.py. Ako sa to da spravit, aby sa dal vypisat vysledok 'print c' tu, plz?
        elif act is '/':
            div(a, b)
        # print("Výsledok je: " + str(c))
        GoOn = None
        # EV: Aky zmysel ma plz 'GoOn = None'? GoOn treba premazat alebo to robis ako strategiu, ako spustit dalsi while cyklus?
        while not GoOn:
            GoOn = input("Chcete pokračovať? a/n : ")
            if GoOn not in ['a', 'n']:
                print("Zadali ste zlú hodnotu.")
                GoOn = None
                continue
            elif GoOn == 'a':
                break
                # EV: Co robi, prosim, toto break? Preskakuje na riadok 21? Dik. :)
            else: # lebo zadal 'n'
                print("Prajem krásny deň!")
                sys.exit()
else: # lebo to nie je funkcia main
    print("Prajem krásny deň!")
    sys.exit()