print('        CARGO')
print('1,Programador')
print('2.Analista de Sistemas')
print('3.Analista de Banco de Dados')
cargo=int(input('Digite o cargo: '))
sal=float(input('Digite o salário: '))

if cargo ==1:
    print('O novo salário é {} reais'.format(sal+(sal*50/100)))
elif cargo==2:
    print('O novo salário é {} reais'.format(sal+(sal*40/100)))
elif cargo==3:
    print('O novo salário é {} reais'.format(sal+(sal*30/100)))
else:
    print('CARGO INVÁLIDO!')
