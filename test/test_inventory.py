from src.product import Product
from src.inventory_manager import InventoryManager
from src.validator import StockValidator

def test_successful_sale():
    p = Product("001", "Widget", 10)
    m = InventoryManager()
    assert "Success" in m.process_transaction(p, 5)
    assert p.stock == 5

def test_insufficient_stock():
    p = Product("002", "Gadget", 2)
    m = InventoryManager()
    assert "Insufficient stock" in m.process_transaction(p, 5)
    assert p.stock == 2

def test_out_of_stock_status():
    p = Product("003", "Tool", 1)
    m = InventoryManager()
    m.process_transaction(p, 1)
    assert p.status == "Out of Stock"