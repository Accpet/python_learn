__author__ = 'water'
import fibo
fibo.fib(1000)
print '\n'
print fibo.fib2(1000)
if __name__ =='__main__':
    import sys
    fib(int(sys.argv[1]))