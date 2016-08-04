__author__ = 'water'

def xf(money,cp):
    if(x-money<0):
         print 'yu e i zu ...'
    else:
         x=x-money
         xfmx(money,cp)
    print '''ke yong yu e %s .'''%(x)

def hk(money,cp):
  if(money<0):
      print 'huan kuan jin e <0 '
  else:
      x=x+money
      print '''ke yong yu e %s .'''%(x)
      xfmx(money,cp)

def xfmx(money,cp):
   mx.append(money,cp)

def cz(mx):
    for j,k in mx:
        print mx[j][k]
def int():
  products=[]
  prices=[]
  f=open('shop1.txt','r')
  # for i in f. readlines():
  #   p=i.split()[0]
  #   pri=i.split()[1]
  #   products.append(p)
  #   prices.append(pri)

def main():
    int()
    mx=[]
    x=15000
    a=input('please input you cp:')
