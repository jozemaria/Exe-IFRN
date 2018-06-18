A = [1,2,3,4,5,6,7,8,9,10]
num = int(input('Digite um nº: '))
i=0
for i in range (10):
    a = A[i]
    
    A[i] = a*num
print(A)
