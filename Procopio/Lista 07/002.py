T=[]
N=[]
for i in range(7):
    N.append(input('Digite o nome: '))
    T.append(float(input('Digite o tempo: ')))
mi = min(T)
Ma = max(T)
print('O menor tempo foi {} feito pelo {}'.format(mi, N[T.index(mi)])
print('O pior tempo foi {} feito pelo {}'.format(Ma, N[T.index(Ma)]))
print('O tempo medio dos nadadores foi {}'.format(sum(T)/7))
      
