class StockValidator:
    @staticmethod
    def validate_sale(current_stock, requested_amount):
        if requested_amount <= 0:
            return False, "Invalid quantity"
        if requested_amount > current_stock:
            return False, "Insufficient stock"
        return True, "Valid"