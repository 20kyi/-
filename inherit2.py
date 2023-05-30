class Person:
    def __init__(self, n='', h='', a='', g=''):
        self.name = n
        self.hp = h
        self.age = a
        self.gender = g
    def __str__(self):
        return '{} ({}) {}세 [{}]'.format(self.name,
                                         self.hp,
                                         self.age,
                                         self.gender)
    def input(self):
        '''
        값이 들어가지 않은 속성을 입력받음 (디폴트 생성인 경우)
        '''
        if (not self.name):
            self.name = input('이름:')
        if (not self.hp):
            self.hp = input('핸폰:')
        if (not self.age):
            self.age = input('나이:')
        if (not self.gender):
            self.gender = input('성별:')

    def happy(self):
        print(f'{self.name} is happy!!')


class Student(Person):
    def __init__(self, n='', h='', a='', g='', m='', sid=''):
        super().__init__(n, h, a, g)
        self.major = m
        self.sid = sid
    def input(self):
        '''
        Person의 input() 메소드를 오버라이딩함
        super의 input()을 먼저 호출하고 나머지 속성을 입력받
        '''
        super().input()
        if (not self.major):
            self.major = input('전공:')
        if (not self.sid):
            self.sid = input('학번:')
    def __str__(self):
        return super().__str__() + f' {self.major} / {self.sid}'
    def study(self):
        print(f'{self.name} studies {self.major}')

if __name__ == '__main__':
    s = Student('lee', '010-1234-5678', 21, 'f', '수학', '223344')
    s2 = Person('kim', '010-5432-2222', 23, 'm')
    s3 = Student()
    s3.input()
    print(s, s2, s3, sep = '\n')
    s2.happy()
    s.study()
    Person.address = 'suwonsi'  # class attribute
    s3.address = 'seoul'        # object attribute
    print(s2, s2.address)
    print(s3, s3.address)
    
'''
---------------- output -----------------
이름:park
핸폰:2345
나이:24
성별:f
전공:cs
학번:21
lee (010-1234-5678) 21세 [f] 수학 / 223344
kim (010-5432-2222) 23세 [m]
park (2345) 24세 [f] cs / 21
kim is happy!!
lee studies 수학
kim (010-5432-2222) 23세 [m] suwonsi
park (2345) 24세 [f] cs / 21 seoul
'''

    
            






        
