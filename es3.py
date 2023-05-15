class QuadEquation:
    def __init__(self, a, b, c):
        if not isinstance(a,(float,int)):
            raise TypeError('a must be numeric')
        if not isinstance(b,(float,int)):
            raise TypeError('b must be numeric')
        if not isinstance(c,(float,int)):
            raise TypeError('c must be numeric')
        
        self._a=a
        self._b=b
        self._c=c

    def getSolutions(self):
        if self.hasSolutions()==False:
            return 'Nan'
        else:
            return (-self._b+(self._b**2-4*self._a*self._c)**(1/2)/(2*self._a),-self._b-(self._b**2-4*self._a*self._c)**(1/2)/(2*self._a))

    def hasSolutions(self):
        if self._b**2-4*self._a*self._c >=0:
            return True
        else:
            return False

    def __str__(self):
        return f'dis equation sure has {self._a!s} and {self._b!s}... but dont forget {self._c}! '

if __name__ == '__main__':

    c = QuadEquation(1, -2, 1)
    print(c.hasSolutions())
    print(c.getSolutions())