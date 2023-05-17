class Person:
    jobs = ['beggar','drug dealer','pimp','mikeohearn memer','eroe milanese']

    def __init__(self, name, job=None, pay=0):
        if not isinstance(name, str): 
            raise TypeError('name must be a string')
        if not isinstance(pay, (int,float)): 
            raise TypeError('pay must be numeric')

        self._name = name
        self._pay = pay

        if job in self.jobs:
            self._job = job
        else:
            self._job = 'other'

    def getLastName(self):
        return self._name.split()[-1]
    def giveRaise(self, percent, add = 0):
        self._pay += (self._pay/100*percent)+add

    def __str__(self):
        return f'dis mf named {self._name!s} only makes {self._pay}€/month by working his ass off as a {self._job}!!\n'    


if __name__ == '__main__':
    tony = Person('tony da milano','eroe milanese')
    jc = Person('cristo da nazareth','messia')

    print(tony.getLastName())
    print(jc.getLastName())
    print(tony,jc)
    tony.giveRaise(0,1000)
    jc.giveRaise(0,1000)
    print(tony,jc)
    tony.giveRaise(10)
    jc.giveRaise(2)
    print(tony,jc)