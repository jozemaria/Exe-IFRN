CC = []
saldo = []
qtd = int(input('Digite a quantidades de correntistas: '))
for i in range (qtd):
    CC.append(input('Digite o nº da conte: '))
    saldo.append(float(input('Difgite o saldo atual: ')))
for i in range (qtd):
    if saldo[i]>=5000:
        print('A conta {} está com o saldo {}'.format(CC[i], saldo[i]))
