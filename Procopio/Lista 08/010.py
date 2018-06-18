from random import randint

def carrega_lista(n):
    l = []
    for i in range(n):
        l.append(randint(1,10))
    print(f'A lista adicionada é {l}')
    return(l)
    
def calcula_media_geometrica(l):
    s = 1
    y = len(l)
    for i in range(y):
        s=s*l[i]
    mg = s**(1/y)
    return(mg) 

        
N =int(input('Digite um nº '))
L = carrega_lista(N)
MG = calcula_media_geometrica(L)
print(f'A media Geometrica da lista escolhida é {MG:.2f}')
