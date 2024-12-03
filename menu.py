# Menu data
MENU_ITEMS = [{
    "type": "Meal", 
    "items": [
        {"Number": 1, "Item Name": "Hamburger", "Price": 3.99},
        {"Number": 2, "Item Name": "Cheeseburger", "Price": 4.99}, 
        {"Number": 3, "Item Name": "Chicken Nuggets", "Price": 2.99},
        {"Number": 4, "Item Name": "Chicken Tenders", "Price": 3.99},
        {"Number": 5, "Item Name": "Chicken Fingers", "Price": 3.99},
        {"Number": 6, "Item Name": "Chicken Sandwich", "Price": 4.99},
        {"Number": 7, "Item Name": "Chicken Wrap", "Price": 4.99},
    ]
},  
    {"type": "Snack", 
    "items": [
        {"Number": 1, "Item Name": "Chips", "Price": 1.99},
        {"Number": 2, "Item Name": "Popcorn", "Price": 0.99},
        {"Number": 3, "Item Name": "Candy", "Price": 0.50},
        {"Number": 4, "Item Name": "Pretzels", "Price": 1.50},
        {"Number": 5, "Item Name": "Trail Mix", "Price": 2.99},
        {"Number": 6, "Item Name": "Crackers", "Price": 1.25},
        {"Number": 7, "Item Name": "Nuts", "Price": 2.50},
        {"Number": 8, "Item Name": "Fruit Snacks", "Price": 0.99},
    ]
},
    {"type": "Drink", 
    "items": [
        {"Number": 1, "Item Name": "Soda", "Price": 1.99},
        {"Number": 2, "Item Name": "Water", "Price": 0.99}, 
        {"Number": 3, "Item Name": "Coffee", "Price": 0.50},
        {"Number": 4, "Item Name": "Tea", "Price": 0.99},
        {"Number": 5, "Item Name": "Lemonade", "Price": 1.50},
        {"Number": 6, "Item Name": "Juice", "Price": 1.99},
        {"Number": 7, "Item Name": "Smoothie", "Price": 2.99},
        {"Number": 8, "Item Name": "Hot Chocolate", "Price": 1.50},
        {"Number": 9, "Item Name": "Iced Tea", "Price": 1.50},
        {"Number": 10, "Item Name": "Energy Drink", "Price": 2.99},
    ]
},
    {"type": "Dessert", 
    "items": [
        {"Number": 1, "Item Name": "Ice Cream", "Price": 1.99},
        {"Number": 2, "Item Name": "Cake", "Price": 0.99}, 
        {"Number": 3, "Item Name": "Pie", "Price": 0.50},
        {"Number": 4, "Item Name": "Brownie", "Price": 1.50},
        {"Number": 5, "Item Name": "Cookies", "Price": 0.99},
        {"Number": 6, "Item Name": "Milkshake", "Price": 2.99},
        {"Number": 7, "Item Name": "Sundae", "Price": 3.99},
        {"Number": 8, "Item Name": "Cheesecake", "Price": 2.99}
    ]
}
]

class OrderSystem:
    def __init__(self):
        self.ordered_items = []
        self.name_spacing = self._find_name_spacing()
        self.price_spacing = self._find_price_spacing()
        self.quantity_spacing = 5

    def _find_name_spacing(self):
        name_spacing = 0
        for item in MENU_ITEMS:
            for sub_item in item["items"]:
                if len(sub_item["Item Name"]) > name_spacing:
                    name_spacing = len(sub_item["Item Name"])
        return name_spacing

    def _find_price_spacing(self):
        price_spacing = 0
        for item in MENU_ITEMS:
            for sub_item in item["items"]:
                if len(str(sub_item["Price"])) > price_spacing:
                    price_spacing = len(str(sub_item["Price"]))
        return price_spacing

    def print_menu(self):
        print("Menu")
        index = 1
        for item in MENU_ITEMS:
            print(f"{index}: {item['type']:<8}")
            index += 1

    def print_order(self):
        print("You have ordered:")
        column_info = f"{'Item Name':<{self.name_spacing}} | {'Price':<{self.price_spacing}} | {'Quantity':<{self.quantity_spacing}}"   
        print(column_info)
        print("-" * len(column_info))
        for item in self.ordered_items:
            print(f"{item['Item Name']:<{self.name_spacing}} | ${item['Price']:<{self.price_spacing}} | {item['Quantity']:<{self.quantity_spacing}}")
        print("\n")

    def get_menu_selection(self):
        while True:
            selection = input("Please select an group from the menu: ")
            if selection.isdigit() and int(selection) <= len(MENU_ITEMS):
                return MENU_ITEMS[int(selection) - 1]
            print("Please enter a number for an item on the menu")

    def get_sub_menu_selection(self, menu_item):
        for item in menu_item["items"]:
            print(f"{item['Number']:<2} | {item['Item Name']:<{self.name_spacing}} | ${item['Price']:<{self.price_spacing}.2f}")
        while True:
            selection = input("Please select an item from the menu: ")
            if selection.isdigit() and int(selection) <= len(menu_item["items"]):
                selection = int(selection)
                return menu_item["items"][selection - 1]
            print("Please enter a valid number")

    def get_quantity(self):
        while True:
            quantity = input("Please enter the quantity: ")
            if quantity == "":
                return 1
            if quantity.isdigit():
                return int(quantity)
            print("Please enter a valid number")

    def process_order(self):
        self.print_menu()
        
        while True:
            selected_item = self.get_sub_menu_selection(self.get_menu_selection())
            quantity = self.get_quantity()
            
            self.ordered_items.append({
                "Item Name": selected_item["Item Name"],
                "Quantity": quantity,
                "Price": f"{selected_item['Price']:.2f}"
            })
            
            self.print_order()
            
            if not self.continue_ordering():
                break

    def continue_ordering(self):
        while True:
            response = input("Would you like to order another item? (y/n): ").lower()
            if response == 'y':
                self.print_menu()
                return True
            if response == 'n':
                return False
            print("Please enter a 'y' or 'n'")

    def calculate_total(self):
        return sum(float(item["Price"]) * item["Quantity"] for item in self.ordered_items)

    def print_receipt(self):
        self.print_order()
        total = self.calculate_total()
        print(f"The total price of the order is ${total:.2f}")
        print("Thank you for your order!")

def main():
    order_system = OrderSystem()
    order_system.process_order()
    order_system.print_receipt()

if __name__ == "__main__":
    main()