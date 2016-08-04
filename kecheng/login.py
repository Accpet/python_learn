__author__ = 'huaishuo'
num=1
user='wangmiaolong'
passwd='huaishuo'
while 1:
    if num==4:
      print 'Logins already full '
      break
    else:
        iuser=raw_input('please input you username:')
        ipasswd=raw_input('please input you passwd:')
        if (iuser==user) and (ipasswd==passwd):
            print 'login successful ....'
            print 'welcome ....'
            break
        else:
            print 'user/passwd is wrong,please input you name.passwd'
            num+=1
