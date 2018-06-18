def carrega_lista(a):
    e=3
    L=[]
    for i in range(a):
        L.append(int(input('Digite um valor ')))
    return L

def retorna_elemento_central_lista(a,b):
    p = a/2
    Cent = b[int(p)]
    return Cent

def calcula_fatorial(c):
    S=1
    for i in range(1,c+1):
        S=S*i
    return S

while True:
    N = int(input('Digite a quant. de itens da lista[impar e maior q 1][0 p/ sair] '))
    if N%2!=0 and N>=1:
        X = carrega_lista(N)
        Y = retorna_elemento_central_lista(N,X)
        Z = calcula_fatorial(Y)
        
        print()
        print(f'O fatorial de {Y} é {Z}')
        print()
    elif N == 0:
        break
