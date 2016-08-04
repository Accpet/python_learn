__author__ = 'water'
print_num=input('which loop do you want itto be printed out?')
count=1
while 1:
    if count==print_num:
        print 'there you go the number:',count
        chioce=raw_input('Do you want to continue the loop?(y/n)')
        if chioce=='n':
            break
        else:
            print_num=input('which loop do you want itto be printed out?')
            count=0
    else:
        print "loop:",count
        count+=1
