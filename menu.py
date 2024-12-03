# Menu data
MENU_ITEMS = [
    {"Number": 1, "Item Name": "Hamburger", "Price": 3.99, "Type": "Meal"},
    {"Number": 2, "Item Name": "Cheeseburger", "Price": 4.99, "Type": "Meal"}, 
    {"Number": 3, "Item Name": "Chicken Nuggets", "Price": 2.99, "Type": "Meal"},
    {"Number": 4, "Item Name": "Chicken Tenders", "Price": 3.99, "Type": "Meal"},
    {"Number": 5, "Item Name": "Chicken Fingers", "Price": 3.99, "Type": "Meal"},
    {"Number": 6, "Item Name": "Chicken Sandwich", "Price": 4.99, "Type": "Meal"},
    {"Number": 7, "Item Name": "Chicken Wrap", "Price": 4.99, "Type": "Meal"},
    {"Number": 8, "Item Name": "Chips", "Price": 1.99, "Type": "Snack"},
    {"Number": 9, "Item Name": "Popcorn", "Price": 0.99, "Type": "Snack"},
    {"Number": 10, "Item Name": "Candy", "Price": 0.50, "Type": "Snack"},
    {"Number": 11, "Item Name": "Soda", "Price": 1.99, "Type": "Drink"},
    {"Number": 12, "Item Name": "Water", "Price": 0.99, "Type": "Drink"},
    {"Number": 13, "Item Name": "Coffee", "Price": 0.50, "Type": "Drink"},
    {"Number": 14, "Item Name": "Ice Cream", "Price": 1.99, "Type": "Dessert"},
    {"Number": 15, "Item Name": "Cake", "Price": 0.99, "Type": "Dessert"},
    {"Number": 16, "Item Name": "Pie", "Price": 0.50, "Type": "Dessert"}
]

class OrderSystem:
    def __init__(self):
        self.ordered_items = []
        self.name_spacing = self._find_name_spacing()
        self.price_spacing = self._find_price_spacing()
        self.quantity_spacing = 5

    def _find_name_spacing(self):
        return max(len(item["Item Name"]) for item in MENU_ITEMS)

    def _find_price_spacing(self):
        return max(len(str(item["Price"])) for item in MENU_ITEMS)

    def print_menu(self):
        print("Menu")
        for item in MENU_ITEMS:
            print(f"{item['Type']:<8} | {item['Number']:<2} | {item['Item Name']:<{self.name_spacing}} | ${item['Price']:<{self.price_spacing}.2f}")

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
            selection = input("Please select an item from the menu: ")
            if selection.isdigit():
                selection = int(selection)
                if 1 <= selection <= len(MENU_ITEMS):
                    return MENU_ITEMS[selection - 1]
                print("Please enter a number for an item on the menu")
            else:
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
            selected_item = self.get_menu_selection()
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