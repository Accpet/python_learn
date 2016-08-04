__author__ = 'water'
# import global.py
def xf(money,cp):
    global x
    if x-money<0 :
         print 'Sorry, your credit is running low...'
         je=x
         print '''Balance:%d  '''%(je)
         return x
    else:
        # xfmx(money,cp)
         x=x-money
         je=x
         print ''' Balance:%d  '''%(je)
         return x


def hk(money):
  global x
  if money<0:
      print 'huan kuan jin e <0 '
  else:
      # xfmx(money,cp)
      x=x+money
      print '''ke yong yu e %s .'''%(x)

def xfmx(money,cp):
   pass
    # cc=cp
    # zd[pp]  =money

def init():
  zd={}
  products={}
  f=open('shop1.txt','r')
  for i in f.readlines():
      pp=i.split()[0]
      products[pp]  =i.split()[1]
  return products
aa=init()
global x
x=15000
n=1

while x:
    tp=input('please input you type '
             '1:sale'
             '2:zz'
             '3:mx (select):')
    if tp==1:
            while 1:
                a=raw_input('please input you cp:  please exit......')
                if(a=='exit'):break
                if a in aa.keys():
                    price=int(aa.get(a))
                    xf(price,a)
                else:
                    print 'without this product.. '

    elif tp==2:
            while 1:

                a=int(raw_input('please input you zhizhi money:  please exit.....'))
                if(a=='exit'):break

                hk(a)
    elif tp==3:
        pass
    else:
        print 'Without this type'



