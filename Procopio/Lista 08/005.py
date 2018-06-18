def Verif_Nula(m,l,c):
    N = True
    for i in range(l):
        for j in range(c):
            if m[i][j]!=0:
                N=False
                break
    return N

M = []
L = int(input('Qtd de linhas '))
C = int(input('Qtd de colunas '))

for i in range(L):
    A = []
    for j in range(C):
         A.append(int(input(f'Elemento{i}X{j} ')))
    M.append(A)

X = Verif_Nula(M,L,C)
if X == True:
    print('Matriz Nula')
else:
    print('Matriz não Nula')
