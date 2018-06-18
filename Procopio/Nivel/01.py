s=0
for i in range(5):
    n1 = float(input('1º nota '))
    n2 = float(input('2º nota '))
    m = (n1+n2)/2
    if m >=2 and m <=6:
        s+=1

print(f'O percentual de alunos em prova final é {100*s/5}')



