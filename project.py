class InventoryItem:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}: {self.quantity} in stock"

class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, name, quantity):
        if name in self.items:
            self.items[name].quantity += quantity
        else:
            self.items[name] = InventoryItem(name, quantity)
        print(f"Added {quantity} {name}(s).")

    def remove_item(self, name, quantity):
        if name in self.items and self.items[name].quantity >= quantity:
            self.items[name].quantity -= quantity
            print(f"Removed {quantity} {name}(s).")
            if self.items[name].quantity == 0:
                del self.items[name]
                print(f"{name} is now out of stock.")
        else:
            print(f"Cannot remove {quantity} {name}(s) - insufficient stock.")

    def display_inventory(self):
        if not self.items:
            print("Inventory is empty.")
        else:
            for item in self.items.values():
                print(item)

    def check_stock(self, name):
        if name in self.items:
            print(f"{name} stock level: {self.items[name].quantity}")
        else:
            print(f"{name} is not in inventory.")

def main():
    inventory = Inventory()
    print("Welcome to the Inventory Management System")
    while True:
        print("\nOptions:")
        print("1. Add item")
        print("2. Remove item")
        print("3. Display inventory")
        print("4. Check stock")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter the item name: ")
            quantity = int(input("Enter the quantity: "))
            inventory.add_item(name, quantity)
        elif choice == '2':
            name = input("Enter the item name: ")
            quantity = int(input("Enter the quantity to remove: "))
            inventory.remove_item(name, quantity)
        elif choice == '3':
            inventory.display_inventory()
        elif choice == '4':
            name = input("Enter the item name to check stock: ")
            inventory.check_stock(name)
        elif choice == '5':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

