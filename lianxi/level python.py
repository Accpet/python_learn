__author__ = 'water'
print abs(-10),
def add(x,y,aa):
    return aa(x)+aa(y)


print add(-5,6,abs)

def f(x):
    return x*x

print map (f,[1,2,3,4,5,6,7,8,9])

l=[]
for n in range(1,10):
    l.append(n*n)
print l