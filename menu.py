#main menu  
mainMenu = [
    {"Number": 1, "Item Name": "Hamberger", "Price": 3.99, "Type": "Meal"},
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

orderedItems = []



#print the menu
def printMenu(menu):
    for item in menu:
        print(f"{item['Type']:<8} | {item['Number']:<2} | {item['Item Name']:<{nameSpacing}} | ${item['Price']:<{priceSpacing}.2f}")

#find the longest item name in the menu
def findNameSpacing(list):
    maxNameLength = 0
    for item in list:
        if len(item["Item Name"]) > maxNameLength:
            maxNameLength = len(item["Item Name"])
    return maxNameLength

#find the longest price in the menu
def findPriceSpacing(list):
    maxPriceLength = 0
    for item in list:
        if len(str(item["Price"])) > maxPriceLength:
            maxPriceLength = len(str(item["Price"]))
    return maxPriceLength

#print the ordered items
def printOrderedItems(orderedItems):
    print("You have ordered:")
    columnInformation = f"{'Item Name':<{nameSpacing}} | {'Price':<{priceSpacing}} | {'Quantity':<{quantitySpacing}}"   
    print(columnInformation)
    print("-" * len(columnInformation))
    for item in orderedItems:
            print(f"{item['Item Name']:<{nameSpacing}} | ${item['Price']:<{priceSpacing}} | {item['Quantity']:<{quantitySpacing}}")

    print("\n")


#set the spacing for the item name, price, and quantity
nameSpacing = findNameSpacing(mainMenu)
priceSpacing = findPriceSpacing(mainMenu)
quantitySpacing = 5 #This is constant. The quantity is the last item on the list and will more than likely never need to be longer than 5 characters.

#print the menu
print("Menu")
printMenu(mainMenu)

#ask user to select an item from the menu
isOrdering = True
while isOrdering:
    menu_selection = 0
    quantity = 1

    #get the menu selection from the user
    while True:
        menu_selection = input("Please select an item from the menu: ")
        if menu_selection.isdigit():
            menu_selection = int(menu_selection)
            if menu_selection > len(mainMenu):
                print("Please enter a number for an item on the menu")
            else:
                break
        else:
            print("Please enter a valid number")

    #get the selected item from the menu
    selectedItem = mainMenu[menu_selection - 1]

#ask user to enter the quantity of the item
    while True:
        quantity = input("Please enter the quantity: ")
        if quantity == "":
            quantity = 1
            break
        if quantity.isdigit():
            quantity = int(quantity)
            break
        print("Please enter a valid number")

    #add the selected item to the orderedItems list
    orderedItems.append({"Item Name": selectedItem["Item Name"], "Quantity": quantity, "Price": f"{selectedItem['Price']:.2f}"})
    printOrderedItems(orderedItems)

    #ask user if they would like to order another item
    while True:
        continueOrdering = input("Would you like to order another item? (y/n): ")
        match continueOrdering.lower():
            case "y":
                printMenu(mainMenu)
                break
            case "n":   
                isOrdering = False
                break
            case _:
                print("Please enter a \'y\' or \'n\'")
#end of ordering loop

#calculate the total price of the order
totalPrice = 0
for item in orderedItems:
    totalPrice += float(item["Price"]) * item["Quantity"]

#print receipt
printOrderedItems(orderedItems)
print(f"The total price of the order is ${totalPrice:.2f}")
print("Thank you for your order!")