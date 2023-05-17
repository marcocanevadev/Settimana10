class Numbers:
    MULTIPLIER = 0.8
    def __init__(self, x, y):
        if not isinstance(x, (int,float)):
            raise ValueError
        if not isinstance(y, (int,float)):
            raise ValueError
        self._x = x
        self._y = y

    def add(self):
        return self._x +self._y

    def getValues(self):
        return (self._x,self._y)

    @classmethod
    def multiply(cls,a):
        if not isinstance(a, (int,float)):
            raise ValueError
        return a * cls.MULTIPLIER

    @staticmethod
    def subtract(a,b):
        if not isinstance(a, (int,float)):
            raise ValueError
        if not isinstance(b, (int,float)):
            raise ValueError
        return b - a
        
if __name__ == '__main__':
    a = Numbers(10, 20)
    print(a.add())
    print(a.getValues())

    print(a.multiply(5))
    print(Numbers.multiply(5))

    print(a.subtract(5,10))
    print(Numbers.subtract(5,10))

    


