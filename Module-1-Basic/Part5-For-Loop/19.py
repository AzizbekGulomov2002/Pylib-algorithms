
# N(N>0) va K  musbat butun sonlar berilgan. Darajali sonlar yig`indisini hisoblansin. 1**K+2**K+…+N**K.

n = int(input("N sonini kiriting = "))
k = int(input("K sonini kiriting = "))

sum = 0
for i in range(1, n+1):
    sum += i ** k
print(sum)