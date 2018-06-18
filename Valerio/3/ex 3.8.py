print('  Média Escolar ')
n1=float(input('Digite a 1º nota: '))
n2=float(input('Digite a 2º nota: '))
m=(n1*2+n2*3)/6
if m<2:
    print('A Média é {}, aluno reprovado!'.format(m))
elif m>=6:
    print('A Média é {}, aluno Aprovado! '.format(m))
else:
    print('A Média é {}, Prova final!'.format(m))
