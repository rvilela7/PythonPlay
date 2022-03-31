class Publication:
    def __init__(self, title, price):    #tip: no error syntax for __imit__
        self._title = title
        self._price = price

class Book(Publication):                        #Notice the parenthisis
    def __init__(self, title, author, price):
        super().__init__(title, price)
        #self._title = title
        self._author = author
        #self._price = price
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        self._author = value

    @property
    def price(self):
        return self._price
     
    @price.setter
    def price(self, value):
        self._price = value
    
#Let's create an instance
mybook = Book("O Mundo de Sofia", "Justin Gardneer", 30.99)
print(mybook.author)
print(mybook.price)
print(mybook.title)
