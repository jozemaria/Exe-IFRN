def Verif_Matriz(m,l,c):
    A=True
    for i in range(l):
        for j in range(c):
            if c!=l:
                m[i][j]!=0
                A=False        
                break
            if c==l:
                m[i][j]==0
                A=False
                break
    return A

while True:
    L=int(input('Qtd de linhas '))
    C=int(input('Qtd de colunas '))
    if L==C:
        break
    
M=[]
for i in range(L):
    a=[]
    for j in range(C):
        a.append(int(input(f'Elemento {i}X{j} ')))
    M.append(a)
    
X = Verif_Matriz(M,L,C)
if X==True:
    print('A matriz é diagonal')
else:
    print('A matriz não é diagonal')
