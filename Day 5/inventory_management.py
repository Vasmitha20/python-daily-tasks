inventory = {}
categories = set()

LOW_STOCK_THRESHOLD = 10

def add_product():
    pid = input("Enter Product ID: ")
    if pid in inventory:
        print("Product ID already exists!")
        return
    name = input("Enter Product Name: ")
    category = input("Enter Category: ")
    qty = int(input("Enter Quantity: "))
    price = float(input("Enter Price: "))
    supplier = input("Enter Supplier: ")
    inventory[pid] = {
        "name": name,
        "category": category,
        "qty": qty,
        "price": price,
        "supplier": supplier
    }
    categories.add(category)
    print("Product added successfully!")

def update_inventory():
    pid = input("Enter Product ID: ")
    if pid not in inventory:
        print("Product not found!")
        return
    print("1. Update Quantity")
    print("2. Update Price")
    choice = input("Enter choice: ")
    if choice == "1":
        qty = int(input("Enter new quantity: "))
        inventory[pid]["qty"] = qty
        print("Quantity updated successfully!")
    elif choice == "2":
        price = float(input("Enter new price: "))
        inventory[pid]["price"] = price
        print("Price updated successfully!")
    else:
        print("Invalid choice!")

def search_product():
    search = input("Enter Product ID or Name: ").lower()
    found = False
    for pid, details in inventory.items():
        if pid.lower() == search or details["name"].lower() == search:
            print("\nProduct Found:")
            print("ID:", pid)
            print("Name:", details["name"])
            print("Category:", details["category"])
            print("Quantity:", details["qty"])
            print("Price:", details["price"])
            print("Supplier:", details["supplier"])
            found = True
    if not found:
        print("Product not found!")

def display_inventory():
    if not inventory:
        print("Inventory is empty!")
        return
    print("\n{:<10} {:<15} {:<15} {:<10} {:<10} {:<15}".format(
        "ID", "Name", "Category", "Qty", "Price", "Supplier"))
    print("-" * 80)
    for pid, details in inventory.items():
        print("{:<10} {:<15} {:<15} {:<10} {:<10.2f} {:<15}".format(
            pid,
            details["name"],
            details["category"],
            details["qty"],
            details["price"],
            details["supplier"]
        ))

def low_stock_alert():
    print("\nLow Stock Products:")
    found = False
    for pid, details in inventory.items():
        if details["qty"] < LOW_STOCK_THRESHOLD:
            print(f"{details['name']} (ID: {pid}) - Qty: {details['qty']}")
            found = True
    if not found:
        print("No low stock products.")

def out_of_stock_alert():
    print("\nOut of Stock Products:")
    found = False
    for pid, details in inventory.items():
        if details["qty"] == 0:
            print(f"{details['name']} (ID: {pid})")
            found = True
    if not found:
        print("No out-of-stock products.")

def show_categories():
    print("\nAvailable Categories:")
    for category in categories:
        print(category)

def inventory_report():
    total_products = len(inventory)
    total_items = 0
    total_value = 0
    category_summary = {}
    for details in inventory.values():
        total_items += details["qty"]
        total_value += details["qty"] * details["price"]
        category = details["category"]
        if category not in category_summary:
            category_summary[category] = 0
        category_summary[category] += details["qty"]
    print("\n===== Inventory Report =====")
    print("Total Products:", total_products)
    print("Total Items:", total_items)
    print("Total Inventory Value: ₹", round(total_value, 2))
    print("\nCategory-wise Summary:")
    for category, qty in category_summary.items():
        print(category, ":", qty)

def delete_product():
    pid = input("Enter Product ID to delete: ")
    if pid in inventory:
        del inventory[pid]
        print("Product deleted successfully!")
    else:
        print("Product not found!")


while True:
    print("\n===== SMART INVENTORY MANAGEMENT SYSTEM =====")
    print("1. Add Product")
    print("2. Update Inventory")
    print("3. Search Product")
    print("4. Display Inventory")
    print("5. Low Stock Alert")
    print("6. Out of Stock Alert")
    print("7. Category Management")
    print("8. Inventory Report")
    print("9. Delete Product")
    print("10. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_product()
    elif choice == "2":
        update_inventory()
    elif choice == "3":
        search_product()
    elif choice == "4":
        display_inventory()
    elif choice == "5":
        low_stock_alert()
    elif choice == "6":
        out_of_stock_alert()
    elif choice == "7":
        show_categories()
    elif choice == "8":
        inventory_report()
    elif choice == "9":
        delete_product()
    elif choice == "10":
        print("Exiting Smart Inventory Management System...")
        break
    else:
        print("Invalid choice! Please try again.")
