import store
import product

store_target = store.Store("Target")
product_bread = product.Product("Bread", 5.99, "Food")
product_rice = product.Product("Rice", 3.99, "Food")
product_bike = product.Product("Bike", 199.99, "Sports")
product_xbox = product.Product("XBOX", 299.99, "Technology")
product_macbook = product.Product("MacBook", 900, "Technology")
store_target.add_product(product_bread).add_product(product_rice).add_product(product_bike).add_product(product_xbox)