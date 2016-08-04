# #coding:utf-8
# __author__ = 'water'
# class  animal(object):
#     def run(self):
#         print 'animal is running...'
#     def eat(self):
#         print 'eating meat...'
#
# class dog(animal):
#     pass
#
# class cat(animal):
#     pass
# #
# # idog=dog()
# # idog.run()
# # icat=cat()
# # icat.run(),icat.eat()
# #
# #
# # ##    判断一个变量是否是某个类型可以用isinstance()判断：
# # #
# # # >>> isinstance(a, list)
# # # True
# # # >>> isinstance(b, animal)
# # # True
# # # >>> isinstance(c, Dog)
# # # True
# #
# # print isinstance(idog,list )
# #
# # print isinstance(icat,animal)
#
#
# def run_twice(animal):
#     animal.run()
#     animal.run()
#
#
# # run_twice(animal())
#
# run_twice(dog())

class Animal(object):
    def run(self):
        print 'Animal is running...'


class dog(Animal):
    def run(self):
        print 'Dog is running...'
    def eat(self):
        print 'Eating meat...'

# idog=dog()
# idog.run()

def run_twice(Animal):
    Animal.run()
    Animal.run()

#run_twice(Animal())

run_twice(dog())
