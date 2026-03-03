from product import Product
from validator import StockValidator

class InventoryManager:
    def process_sale(self, product, amount):
        is_valid, message = StockValidator.is_transaction_valid(product.stock, amount)
        if is_valid:
            product.stock -= amount
            return f"Success! Remaining: {product.stock}"
        return f"Error: {message}"