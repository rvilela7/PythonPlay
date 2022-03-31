from abc import ABC, abstractmethod   

#ABC from standard library gives support for abstract classes
#abstractmethod is a decorator

class graphicShape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod        #decorator
    def calc_area(self):
        pass

class circle(graphicShape):
    def __init__(self, radius):
        self._radius = radius

    def calc_area(self):
        return 3.14 * (self._radius **2)

class square(graphicShape):
    def __init__(self, side):
        self._side = side

    def calc_area(self):
        return self._side * self._side

#g = graphicShape()

c = circle(10)
sq = square(30)

print(c.calc_area())
print(sq.calc_area())
