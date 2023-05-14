class Product:
    def __init__(self, name, price=0):
        #add precondition check
        if not isinstance(name, str):
            raise TypeError('name must be str')
        if not isinstance(price, (float,int)):
            raise TypeError('price must be numeric')
        self._name = name
        self._price = price
    
    def getName(self):
        return self._name
    def getPrice(self):
        return self._price
    def reducePrice(self,rate):
        self._price -= self._price*(rate/100)
    
    def __repr__(self):
        return f'Product({self._name!r}, {self._price!s})'
    

if __name__ == '__main__':
    in1 = input('set name and price for 1st product:')
    in2 = input('Set name and price for 2nd product:')
    p1 = Product(' '.join((in1.split()[0:-1])),float(in1.split()[-1]))
    p2 = Product(' '.join((in2.split()[0:-1])),float(in2.split()[-1]))

    pes = [p1, p2]
   
    if pes[0].getPrice() > pes[1].getPrice():
        pes[0],pes[1]=pes[1],pes[0]

    print(f'{pes[0].getName()} {pes[0].getPrice()}\n{pes[1].getName()} {pes[1].getPrice()}')
    pes[1].reducePrice(float(input('insert percentage for price reduction of most expensive: ')))

    if pes[0].getPrice() > pes[1].getPrice():
        pes[0],pes[1]=pes[1],pes[0]
    print(f'{pes[0].getName()} {pes[0].getPrice()}\n{pes[1].getName()} {pes[1].getPrice()}')