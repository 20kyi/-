class Length:
    '''
    길이를 나타내는 클래스
    길이와 단위를 가지고 길이 변환이나  계산 기능을 제공
    '''
    standards = {'mm': 0.001, 'cm': 0.01, 'm': 1.0,
                'mile' : 1609.34, 'in' : 0.0254, 'ft': 0.3048 }

    
    def __init__(self, value, unit='m'):
        ''' 
        길이 객체 초기화, 미터를 디폴트로 함
        '''
        self.value = value      # 길이
        self.unit = unit        # 단위


    @staticmethod   #새로운 unit 추가
    def add_unit(unit, value):
        Length.standards[unit] = value

        
    def __str__(self):  #self가 오면 value와 unit을 문자열로 표현 
        return "{0:.2f} {1}".format(self.value, self.unit)


    def __repr__(self): #객체가 어떤 객체인지 정보 나타냄
        return 'Length(' + str(self.value) + ', "' + self.unit + '")'
    
    # 수업 실습
    def changeTo(self, newunit):
        self.value = self.value * (Length.standards[self.unit] / Length.standards[newunit])
        self.unit = newunit
    
    def __add__(self, other): 
        if type(other) == int:
            x = self.value + other
        else:
            x = self.value + other.value * (Length.standards[other.unit] / Length.standards[self.unit])
        return Length(x, self.unit)
    
    def __iadd__(self, other):
        if type(other) == int:
            self.value += other
        else:
            self.value += other.value * (Length.standards[other.unit] / Length.standards[self.unit])
        return self
    
    def __radd__(self, other):
        return self + other
    
    # - 연산 (a-b 형식)
    def __sub__(self, other):
        if type(other) == int:
            x = self.value - other
        else:
            x = self.value - other.value * (Length.standards[other.unit] / Length.standards[self.unit])
        return Length(x, self.unit)
    # - 연산 (10-a 형식)
    def __rsub__(self, other):
        if type(other) == int:
            x = other - self.value
        else:
            x = other.value - self.value * (Length.standards[self.unit] / Length.standards[other.unit])
        return Length(x, self.unit)
    
    
        
if __name__ == '__main__':
    a = Length(100, 'm')
    b = Length(20, 'ft')
    c = Length(50, 'cm')
    print('a = 100m  = ', a)
    print('b = 20 ft = ', b)
    print('c = 50 cm = ', c)
    
    #수업 실습
    a.changeTo('mile')
    print('a = 100m (mile) =', a)
    b.changeTo('m')
    print('b = 20ft (m) =', b)
    
    d = b + c
    print('d = b + c = ', d)
    d = b + 5
    print('d = b + 5 = ', d) 
    d += c
    print( 'd += c = ', d )
    d += 5
    print( 'd += 5 = ', d )
    d = 2 + b
    print( 'd = 2 + b = ', d )
    
    # - 연산
    e = b - c
    print('e = b - c =', e)
    e = b - 5
    print('e = b - 5 =', e)
    e = 10 - b
    print('e = 8 - b =', e)
    