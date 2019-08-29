class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Prise can not be negative")
        self.__price = value

    # other way to create a property in pthon
    # price = property(get_price, set_price)


product = Product(-20)
print(product.price)
