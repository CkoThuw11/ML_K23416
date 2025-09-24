from review.list_products import ListProduct
from review.product import Product
lp = ListProduct()
lp.add_product(Product(100, "Product 1", 10, 10))
lp.add_product(Product(10, "Product 2", 20, 60))
lp.add_product(Product(200, "Product 3", 30, 20))
lp.add_product(Product(30, "Product 4", 50, 60))
lp.add_product(Product(50, "Product 5", 16, 13))
lp.add_product(Product(60, "Product 6", 70, 10))

print("List of Products: ")
lp.print_products()
lp.output_products()
# lp.desc_sort_products()
#
# print("List of Products after descending order: ")
# lp.print_products()