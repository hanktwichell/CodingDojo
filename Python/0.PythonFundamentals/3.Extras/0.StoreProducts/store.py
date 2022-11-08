class Store:
    products_list = []

    def __init__(self, name):
        self.name = name
        self.products = Store.products_list

    def add_product(self, new_product):
        Store.products_list.append(new_product)
        return self

    def sell_product(self, id):
        Store.products_list.pop(id).print_info()
        return self

    def inflation(self, percent_increase):
        for i in Store.products_list:
            i.update_price(percent_increase, True)
        return self

    def set_clearance(self, category, percent_discount):
        for i in Store.products_list:
            if (i.category == category):
                i.update_price(percent_discount, False)
        return self

    @classmethod
    def display_inventory(cls):
        for i in cls.products_list:
            print(f"Name: {i.name}, Category: {i.category}, Price: {i.price}")
