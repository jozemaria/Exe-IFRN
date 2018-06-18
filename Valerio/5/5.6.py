gab = ['A','B','B','C','B','C','C','A','B','C']
gabaluno = []
acerto = 0
cont = 0
while cont <= 9:
    gabaluno.append(input('Digite a sua resposta da questão {}:'.format(cont+1)))
    if (gab[cont] == gabaluno[cont]):
        acerto += 1
    cont += 1

print('O aluno acertou  {} questões.'.format(acerto))