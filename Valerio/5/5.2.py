lista = []
cont = 0
while cont <= 10:
    lista.append(float(input('Digite um nº: ')))
    if(lista [cont] < 0 ):
        lista[cont] = 1

    cont+=1
print(lista)