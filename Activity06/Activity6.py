class Item:
    def __init__(self, item_id, name, description, price):
        self.item_id = item_id
        self.name = name
        self.description = description
        self.price = price

class ItemManager:
    def __init__(self):
        self.items = {}

    def create_item(self):
        try:
            item_id = input("Enter Item ID: ").strip()
            if item_id in self.items:
                print("Error: Item ID already exists.")
                return

            name = input("Enter Item Name: ").strip()
            description = input("Enter Item Description: ").strip()
            price = float(input("Enter Item Price: "))

            if price < 0:
                print("Error: Price cannot be negative.")
                return

            self.items[item_id] = Item(item_id, name, description, price)
            print("Item successfully added.")

        except ValueError:
            print("Error: Invalid price. Please enter a valid number.")

    def read_items(self):
        if not self.items:
            print("No items found.")
            return
        print("\nItems List:")
        for item in self.items.values():
            print(f"ID: {item.item_id}, Name: {item.name}, Description: {item.description}, Price: ${item.price:.2f}")

    def update_item(self):
        item_id = input("Enter Item ID to update: ").strip()
        if item_id not in self.items:
            print("Error: Item not found.")
            return

        try:
            name = input("Enter new name (leave blank to keep current): ").strip() or self.items[item_id].name
            description = input("Enter new description (leave blank to keep current): ").strip() or self.items[item_id].description
            price_input = input("Enter new price (leave blank to keep current): ").strip()
            price = float(price_input) if price_input else self.items[item_id].price

            if price < 0:
                print("Error: Price cannot be negative.")
                return

            self.items[item_id] = Item(item_id, name, description, price)
            print("Item successfully updated.")

        except ValueError:
            print("Error: Invalid price. Please enter a valid number.")

    def delete_item(self):
        item_id = input("Enter Item ID to delete: ").strip()
        if item_id in self.items:
            del self.items[item_id]
            print("Item terminated")
        else:
            print("Error: Item not found.")

    def menu(self):
        while True:
            print("\nItem Management Menu:")
            print("[1] Add Item")
            print("[2] View Items")
            print("[3] Update Item")
            print("[4] Delete Item")
            print("[5] Exit")

            choice = input("Select an option: ").strip()
            if choice == '1':
                self.create_item()
            elif choice == '2':
                self.read_items()
            elif choice == '3':
                self.update_item()
            elif choice == '4':
                self.delete_item()
            elif choice == '5':
                print("Terminating Session")
                break
            else:
                print("Invalid choice. Please select a valid option.")

manager = ItemManager()
manager.menu()
