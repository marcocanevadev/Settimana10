class Numbers:
    def __init__(self, x, y):
        if not isinstance(x, (int,float)):
            raise ValueError
        if not isinstance(y, (int,float)):
            raise ValueError
        self._x = x
        self._y = y