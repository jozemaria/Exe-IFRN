def mat_esp(m,l,c):
    E=0
    for i in range(l):
        for j in range(c):
            if m[i][j]!=0:
                E-=1
            else:
                E+=1
    return E

M = []
L = int(input('Qtd de linhas '))
C = int(input('Qtd de colunas '))

for i in range(L):
    A = []
    for j in range(C):
         A.append(int(input(f'Elemento{i}X{j} ')))
    M.append(A)

X = mat_esp(M,L,C)
if X>0:
    print('Matriz Esparsa')
else:
    print('Matriz não Esparsa')
