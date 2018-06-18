t=input('Qual é o tamanho da da camisa: [P][M][G][GG][XG]')
if t=='p' or t=='P':
    print('Tamanho Pequeno')
elif t=='m' or t=='M':
    print('Tamanho Médio')
elif t=='g' or t=='G':
    print('Tamanho Grande')
elif t=='GG' or t=='gg':
    print('Tamanho grande-grande')
elif t=='XG' or t=='xg':
    print('Tamanho Extra-Grande')
else:
    print('Tamanho inválido!')
