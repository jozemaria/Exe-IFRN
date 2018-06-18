import random
F, L=1, []
N=int(input(' Digite a qtd de numeros a ser digitados (ímpar):'))
for i in range(N):
    L.append(int(input('Digite o numero ')))
C = L[N//2]
print(L)
for i in range(1,C+1):
    F = F * i
print('O fatorial do termo do meio é ',F) 
