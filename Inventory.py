import os
import time

class Product:
    def __init__(self, category, name, desc, price, quantity) -> None:
        self.category = category
        self.name = name
        self.desc = desc
        self.price = price
        self.quantity = quantity

    def view_products(self):
        return f"| {self.category} | {self.name} | {self.price} | {self.quantity} | {self.desc} |"
    
products = []

os.system("cls")

def add_product():
    while True:
        os.system("cls")
        print("--|Inventory Managment|--")
        print("--|  Add to invetory  |--")
        print("")

        category = input("Category: ")
        name = input("Product name: ")
        desc = input("Product Description: ")
        price = int(input("Price: "))
        quantity = int(input("Quantity: "))

        print("")
        
        user_input = input("Confirm (Y/N): ").lower()

        total_price = price * quantity

        if user_input == "y":
            products.append(Product(category, name, desc, price, quantity))
            print("")
            print(f"Added {quantity} {name} to {category}. Price: {price} kr/st, Total price: {total_price} kr")
            print("")
            user_input = input("Do you wish to add another more? (Y/N): ")
            if user_input == "y":
                add_product()
            else:
                main_menu()
        else:
            main_menu()

def show_inventory():
    os.system("cls")
    print("--|Inventory Managment|--")
    print("--|     Inventory     |--")
    print("")

    try:
        products[0]
    except:
        print("Awfully empty here...") 
    else:
        for product in products:
            print(product.view_products())
    
    print("")
    input("Press enter to go back to main menu")
    main_menu()

def main_menu():
    os.system("cls")
    print("--|Inventory Managment|--")
    print("--|     Main Menu     |--")
    print("\n1: Add to invetory\n2: Show inventory\n3: Save and Exit\n")

    menu_choice = int(input("Choice: "))

    if menu_choice == 1:
        add_product()
    elif menu_choice == 2:
        show_inventory()
    elif menu_choice == 3:
        os.system("cls")
        exit()
    else:
        print("INVALID INPUT")
        time.sleep(2)
        os.system("cls")
        main()

def main():
    main_menu()

for product in products:
    print(Product.view_products())

main()