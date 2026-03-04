class Product:
    def __init__(self, product_id, name, stock):
        self.product_id = product_id
        self.name = name
        self.stock = stock
        self.status = "In Stock" if stock > 0 else "Out of Stock"