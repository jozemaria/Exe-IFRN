def gera_serie_Fibonacci(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f

N=int(input('Digite um nº '))
F=gera_serie_Fibonacci(N)
print(f'O fatorial de {N} é {F}')
