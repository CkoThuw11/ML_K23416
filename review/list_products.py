class ListProduct:
    def __init__(self):
        self.products = []
    def add_product(self, p):
        self.products.append(p)
    def print_products(self):
        for p in self.products:
            print(p)
    def output_products(self):
        return self.products
    def desc_sort_products(self):
        for i in range(0, len(self.products)):
            for j in range(i+1, len(self.products)):
                pi = self.products[i]
                pj = self.products[j]
                if pi.price < pj.price:
                    self.products[i] = pj
                    self.products[j] = pi
    # def desc_no_sort_products(self):
    #     self.products.sort(reverse=True, key = lambda price: self.products[][3])