print('CALCULADORA')
print('1.Soma')
print('2.subtração')
print('3.Multiplicação')
print('4.Divisão')
op=int(input('Digite o nº do operador'))
print('')
x=int(input('Digite um nº: '))
y=int(input('Digite outro nº: '))
if op==1:
    print('A soma entre {} e {} é {}'.format(x,y,x+y))
elif op==2:
    print('A subtração entre {} e {} é {}'.format(x,y,x-y))
elif op==3:
    print('A multiplicação entre {} e {} é {}'.format(x,y,x*y))
elif op==4:
    print('A divisão entre {} e {} é {}'.format(x,y,x/y))
else:
    print('ERRO na escolha do operador!')
