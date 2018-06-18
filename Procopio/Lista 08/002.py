def verificar_Matriz(a,b):
    M=[]
    for i in range(a):
        X=[]
        for j in range(b):
            X.append(float(input(f'Digite o elemento da posição {i}X{j} ')))
        M.append(X)
    A = True
    for i in range(a):
        for j in range(b):
            if i == j:
                if M[i][j] != 1:
                    A=False
                    break
            else:
                if M[i][j] !=0:
                    A=False
                    break
    return A
                

while True:
    print('A MATRIZ deve ser Quadrada!!')
    lin = int(input('Digite a quant de linhas: '))
    col = int(input('Digite a quant de colunas: '))
    if lin == col:
        I = verificar_Matriz(lin,col)
        if I == True:
            print('A Matriz é identidade')
        else:
            print('A Matriz não é identidade')
            
    print()
