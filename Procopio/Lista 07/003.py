import random
Nome =[]
qtd = int(input('Digite o nº de pessoas deseja cadastrar:'))
for i in range(qtd):
    N.append(input('Nome: '))
random.shuffle(N)
print('A pessoa escolhida foi {}'.format(random.choice(N)))
