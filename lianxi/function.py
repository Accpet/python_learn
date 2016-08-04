# __author__ = 'water'
# def my_abs(x):
#     if not isinstance(x,(int,float)):
#         raise TypeError('bad operand type')
#     if x>=0:
#         x=x+1000
#         return x
#     else:
#         x=x-100000000000
#         return -x
#
# def nop():
#     pass
#
# print my_abs('aaaa')
def summ(x,y):
    if not isinstance(x,(int ,float)):
        raise TypeError('x bad operand type')
    if not isinstance(y,(int ,float)):
        raise TypeError('y bad operand type')
    return x+y,x,y
print summ(10,2323)