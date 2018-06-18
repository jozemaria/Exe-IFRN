idade = []
soma = 0
cont = 0

while cont < 10:
    idade.append((int(input('Coloque a idade: '))))
    soma += idade[cont]
    cont += 1
print('As idades das pessoas: {}'.format(idade))
print('A média das idades é {}'.format(soma/cont))
