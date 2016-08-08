# # __author__ = 'water'
# # class student(object):
# #     pass
# #
# # bart=student()
# # bart.name = 'Bart Simpson'
# #
# # print bart
#
# class test(object):
#     def __init__(self,name,score):
#         self.name=name
#         self.score=score
#
# try=test('huaishuo','90')
# print try.name

class student(object):
    def __init__(self,name,score):
        self.name=name
        self.score=score

gid = student('Bart Simpson', 59)
wml = student('huai Simpson', 39)

wml.score=200
print gid.score
print wml.score