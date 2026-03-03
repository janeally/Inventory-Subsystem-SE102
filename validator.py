class StockValidator:
    @staticmethod
    def is_transaction_valid(current_stock, requested_amount):
        # Business Logic: No negatives, no over-selling
        if requested_amount <= 0:
            return False, "Invalid quantity"
        if requested_amount > current_stock:
            return False, "Insufficient stock"
        return True, "Valid"