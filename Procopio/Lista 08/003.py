def mult(A,l,c):
    for i in range(l):
        for j in range(c):
            A[i][j]=A[i][j]*3            
    return A

A= []
L= int(input('Digite a qtd de Linhas: '))
C= int(input('Digite a qtd de Colunas: '))
for i in range(L):
    x = []
    for j in range(C):
        x.append(int(input(f'Elemento{i}X{j} ')))
    A.append(x)
    
print('==A Matriz que você digitou==')
for i in range(L):
    for j in range(C):
        print(A[i][j],end=(' '))
    print()
    
print()
X = mult(A,L,C)

print(f'A multiplicação entre a constante 3 e a Matriz é...')
for i in range(L):
    for j in range(C):
        print(A[i][j],end=(' '))
    print()
