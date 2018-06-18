def calcula_IMC(m,a):
    imc=m/a**2
    return imc

M=float(input('Informe sua massa '))
A=float(input('Informe sua altura '))
IMC = calcula_IMC(M,A)
print(f'O IMC é {IMC:.2f}')
