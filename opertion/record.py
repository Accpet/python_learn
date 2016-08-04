__author__ = 'water'

a=[ 'tom','12', '86','joseph','16','19','lee','15','99']
n=0
f=open('1.txt','w+')
for i in a:
  n+=1
  if n%3 ==0:
      f.write(i)
      f.write(' \n')
  else:
      f.write(i)
      f.write(' ')

f=open('1.txt','r')
line=f.readline()
while line:
    print line
    line=f.readline()
f.close()


