def calcula_media_geometrica(l):
    s=1
    y=len(l)
    for i in range(y):
        s=s*l[i]
    mg= s**(1/y)
    return(mg)

L=[]
while True:
    x=input('digite um nº ["s" p/sair] ')
    if x=='s':
        break
    else:
        L.append(int(x))
        
MG=calcula_media_geometrica(L)
print(f'A media Geometrica da lista escolhida é {MG:.2f}')
