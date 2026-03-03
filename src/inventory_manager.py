from product import Product
from validator import StockValidator

class InventoryManager:
    def process_transaction(self, product, amount):
        is_valid, message = StockValidator.validate_sale(product.stock, amount)
        if is_valid:
            product.stock -= amount
            if product.stock == 0:
                product.status = "Out of Stock"
            return f"Success: {product.name} updated. New stock: {product.stock}"
        return f"Error: {message}"