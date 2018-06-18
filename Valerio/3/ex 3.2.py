x=int(input('Digite um nº: '))
y=int(input('Digite outro nº: '))
s=x+y
if s<10:
    print('Como o resultado da soma deu {} eu somei 5 e deu {}'.format(s,s+5))
else:
    print('Como o resultado da soma do números deu {} eu subtrai 7 e deu {}'.format(s,s-7))
