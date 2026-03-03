import os
from product import Product
from inventory_manager import InventoryManager

def main_menu():
    # Setup the subsystem (The 'Environment Setup' Task 2)
    item = Product("SKU-99", "Premium Widget", 25)
    manager = InventoryManager()
    
    while True:
        print("\n" + "="*30)
        print(" RETAIL INVENTORY SUBSYSTEM ")
        print("="*30)
        print(f"Product: {item.name} | Stock: {item.stock}")
        print(f"Status:  {item.status}")
        print("-" * 30)
        print("1. Process Sales Transaction")
        print("2. View Product Details")
        print("3. Exit")
        
        choice = input("\nSelect Option > ")

        if choice == "1":
            try:
                qty = int(input("Enter quantity to sell: "))
                # Logic Processing (Task 3)
                result = manager.process_transaction(item, qty)
                print(f"\n[SYSTEM]: {result}")
            except ValueError:
                print("\n[ERROR]: Please enter a numeric value.")
        
        elif choice == "2":
            print(f"\n[DATA]: {item.name} (ID: {item.product_id})")
            print(f"Current Available Units: {item.stock}")
            
        elif choice == "3":
            print("Closing Subsystem...")
            break