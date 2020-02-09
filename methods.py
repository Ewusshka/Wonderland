def add(a, b):
    c = a + b
    print("Výsledok je: " + str(c))
    return c

def add_eva(a, b):
    if (a > 0 and b > 0):
        c = a + b
        return c
    else:
        return "Nejsou kladne cisla"
    

if __name__ == "__main__":
    print('tady je taky kod')
    print(__name__)
    result = add_eva(-1, 2)
    print(result)