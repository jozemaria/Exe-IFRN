A = []
for i in range (10):
    A.append(int(input('')))
print(A)
x = -1
for i in range (5):
    t = A[i]
    A[i] = A[x]
    A[x] = t
    x = x - 1
print(A)
