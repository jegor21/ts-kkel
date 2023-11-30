from math import *
from random import random
from random import seed
from random import randint
#1-----

t = 0
print("Enter 15 numbers")
for x in range(15):
    A = float(input("Enter number: "))
    if A.is_integer(): #Näide:  5 = True; 4.24 = False
        t += 1
print(t)

#2-----

summa = 0
A = int(input("Sisesta A: "))
for x in range(1,A+1,1):
    summa+=x
print("summa: {0}".format(summa))

#3-----

p=1
lause=""
for x in range(8):
    A = float(input("{0}. samm\nEnter A: ".format(x+1)))
    if A>0:
        p*=A
        lause=lause+str(A)+"*"

print(lause[:-1], "=",p)



#4-----

for x in range(10,21):
    print(x ** 2)

#12-----

N=randint(2,10)
m=randint(1,10)
summa=m
print("Masinad: ",N)
print("Tunnid: ",m)
for t in range(N-1):
    summa+=m
    m=(m/6)*7
    print(m)
print("Kokku masinad töötasid: ",summa,"tunnid")


#14-----

N=randint(2,20)
print("Random N = {0}".format(N))

p=1
for i in range(1,N+1):
    p*=i
print(f"from 1 to {N}: {p}")


#15-----

for y in range(10):
    for x in range(10):
        print(x,end=" ")
    print()

#16-----

n=9

for i in range(1,n+1):
    row=[0]*n
    row[i-1]=i
    print(" ".join(map(str, row)))





#17-----

a = 0
while a<9:
    a += 1
    v=2*a
    print("2*{0}={1}".format(a,v))


#29-----


for i in range(9):
    for x in range(9):
        if x==0 or i==x:
            print("x",end=" ")
        else:
            print("0",end=" ")
    print()






