__author__ = 'water'
# class student(object):
#     @property
#     def birth(self):
#         return self._birth
#     @birth.setter
#
#     def birth(self,value):
#         self._birth=value
#     @property
#     def age(self):
#         return 2016-self._birth


class student(object):
    def get_score(self):
        return self._score


    def set_score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be int')
        if value <0 or value >100:
            raise ValueError('sorce muste be 0-100')
        self._score=value

s=student()
s.set_score(63)
s.get_score()
print s._score

# s._score=22000
# print s._score
