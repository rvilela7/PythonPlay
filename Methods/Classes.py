# TODO: Classes

class Book:
    def __init__(self, title, author, price): #everything is public
        self._title = title
        self._author = author
        self._price = price
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        self._title = value

b1 = Book("Ensaio sobre a cegueira", "José Saramago", 22)
print (b1) #Shows object

print (b1.title)
b1.title = "";