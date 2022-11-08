import store

class Product:
    all_products = []
    count = 0

    def __init__(self, name, price, category):
        self.name = name
        self.price = round(price, 2)
        self.category = category
        self.id = Product.count
        Product.count += 1
        Product.all_products.append(self)

    def update_price(self, percent_change, is_increased):
        if is_increased:
            self.price *= (1+percent_change)
        else:
            self.price *= (1-percent_change)
        self.price = round(self.price, 2)
        return self

    def print_info(self):
        print(
            f"Name: {self.name}, Category: {self.category}, Price: {self.price}")
        return self

    @classmethod
    def print_all_products(cls):
        for i in cls.all_products:
            print(
                f"Name: {i.name}, Category: {i.category}, Price: {i.price}, ID: {i.id}")
