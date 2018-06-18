x, TS = 0,0
print('''1. Enfermeiro
2. Nutricionista
3. Médico
0. sair
''')
while True:
    cod = int(input('Digite o codigo '))
    if cod == 0:
        break
    elif cod >=1 and cod <=3:
        sal = float(input('Digite o salário '))
        if cod ==2:
            TS = TS+sal
            x+=1
print(f'A media salarial dos nutricionista é R${TS/x:.2f}')
            
    
