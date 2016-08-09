__author__ = 'water'
#!/usr/bin/python
#-*- coding: UTF-8 -*-

count=0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if (i!=k) and (j!=k) and (i!=j):
                sum=i*100+j*10+k
                count+=1
                print sum
print count
