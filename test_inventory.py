import pytest
from product import Product
from validator import StockValidator
from inventory_manager import InventoryManager

# Test 1: Successful Sale (Normal Case)
def test_successful_sale():
    product = Product("Laptop", 10)
    manager = InventoryManager()
    result = manager.process_sale(product, 3)
    assert product.stock == 7
    assert "Success" in result

# Test 2: Insufficient Stock (Edge Case - Black Box)
def test_insufficient_stock():
    product = Product("Mouse", 2)
    manager = InventoryManager()
    result = manager.process_sale(product, 5)
    assert product.stock == 2  # Stock should not change
    assert "Insufficient stock" in result

# Test 3: Invalid Input (Negative Number - TDD Example)
def test_negative_quantity():
    product = Product("Keyboard", 5)
    manager = InventoryManager()
    result = manager.process_sale(product, -1)
    assert "Invalid quantity" in result