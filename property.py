# 실습 - 학생 클래스 프라퍼티
class Student:
    def __init__(self, n, s):
        self.name = n;
        self.__score = s;

    def __str__(self):
        return '{} : {} ({})'.format(self.name,
                                self.__score, self.score)

    @property
    def score(self):
        if self.__score >= 90:
            return 'A'
        if self.__score >= 70:
            return 'C'
        else:
            return 'D'

    @score.setter
    def score(self, s):
        if s < 0:
            self.__score = 0
        elif s > 100:
            self.__score = 100
        else:
            self.__score = s
        

if __name__ == '__main__':
    a = Student('a', 80)
    b = Student('b', 90)
    print(a)
    print(b)
    a.score = 70
    b.score = -30
    print(a)
    print(b)
    print('b.__score = ', b.__score)

'''
a : 80 (C)
b : 90 (A)
a : 70 (C)
b : 0 (D)
Traceback (most recent call last):
  File "C:\Users\edutech\Desktop\수업\PL\2023 강의노트\12주 파이썬\property.py", line 38, in <module>
    print('b.__score = ', b.__score)
AttributeError: 'Student' object has no attribute '__score'. Did you mean: 'score'?
'''
