__author__ = 'water'

print range(1,11)
L=[]
for  x in range(1,11):
    L.append(x*x)

print L

print [x * x for x in range(1,11) if x % 2==0]

print[m+n for m in 'abc' for n in 'xyz']