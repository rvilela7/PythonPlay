#See magic methods docs

class magicmethods():
    def __init__(self, name, size):
        self._name = name
        self._size = size

    def __str__(self):
        return f"Magic methods object {self._name} is {self._size}"

    def __repr__(self): #for debugginc purposes
        return f"<magicmethods class (name:{self._name}),(size:{self._size})>"

    def __eq__(self, other):
        return self._name == other

mm1 = magicmethods("obj1", 10)
mm2 = magicmethods("obj2", 20)
mm3 = magicmethods("obj3", 30)

print(mm1) #Has __str__ method
print(repr(mm1))

print (mm1 == mm2)
print (mm3 == mm3)