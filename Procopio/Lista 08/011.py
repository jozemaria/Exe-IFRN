from random import randint

def carrega_lista(n):
    l = []
    for i in range(n):
        l.append(randint(1,10))
    print(f'A lista adicionada é {l}')
    return(l)

def exc_Par(n,l):
    nl=[]
    for i in range(len(l)):
        if l[i]%2 != 0:
            nl.append(l[i])
    return nl


N = int(input('Digite um nº '))
L = carrega_lista(N)
NL = exc_Par(N,L)
print()
print(f'A nova lista é {NL}')
