__author__ = 'water'
# for (i=0; i<list.length; i++) {
#     n = list[i];
# }
d={'a':1,'b':2,'c':10}
for key in d:
        print key

from collections import Iterable
print isinstance('abc',Iterable)
print isinstance([1,2,3],Iterable)
print isinstance(1234,Iterable)



