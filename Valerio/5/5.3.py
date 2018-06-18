A = []
cont = 1
menor = 0
maior = 0
while cont <= 3:
    a = int(input('Digite um valor: '))
    A.append(a)

    if maior >= a:
        maior = a
    else:
        menor = a

    cont += 1

print(A)
print(menor)
print(maior)