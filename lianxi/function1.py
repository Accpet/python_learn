#__author__ = 'water'
def enroll(name, gender, age=6, city='Beijing'):
    print 'name:', name
    print 'gender:', gender
    print 'age:', age
    print 'city:', city

# print enroll('huaishuo','M',15,'hangzhou')
# print enroll('Bob', 'M', 7)
# print enroll('Bob', 'M', city='shaoxing')
def add_end(l=[]):
    l.append('end')
    return l

print add_end()
print add_end()
print add_end()
print add_end(['1','2','3'])
print add_end(['x','y','z'])



def add_endd(l=None):
    if l is None:
        l=[]
    l.append('end')
    return l

print add_endd()
print add_endd()
print add_endd()
print add_endd(['x','y','z'])
t = ['Michael', 'Bob', 'Tracy']
print add_endd(['dddd','y','z'])
