I, J, A, cont =0,0,0,0
while True:
    idd = int(input('Digite a idade: [0 p/ sair] '))
    if idd == 0:
        break
    elif idd >=11 and idd <=15:
        I+=1
    elif idd >=16 and idd<=17:
        J+=1
    elif idd >=18:
        A+=1
    cont +=1

print(f'''O percentual de Intafil é {100*I/cont:.2f}
O percentual de Juvenil é {100*J/cont:.2f}
O percentual de Adulto é {100*A/cont:.2f}
''')

#{100*I/cont}
