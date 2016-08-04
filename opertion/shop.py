#_*_ coding: UTF-8 _*_
products=[]
prices=[]
f=open('shop1.txt','r')
for i in f.readlines():
    p=i.split()[0]
    pri=i.split()[1]
    products.append(p)
    prices.append(pri)


print products,prices

