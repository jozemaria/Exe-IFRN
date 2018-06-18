PA=[]
PA.append(int(input('Digite o 1º termo: ')))
qtd = int(input('Quantidade de termos: '))
R = int(input('Digite a razão: '))
for i in range(qtd-1):
    PA.append(PA[i]+R)
for z in range(qtd):
    print(PA[i])
print('A soma de todos os termos da PA é ',sum(PA))
