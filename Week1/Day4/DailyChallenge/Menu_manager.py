""" Daily Challenge: Coffee Shop Menu Manager """

menu_dict = {
    "espresso" : 7.0,
    "cappuccino" : 10.0,
    "coke" : 7.0,
    "latte" : 13.0,
    "water" : 4.5,
    "coffee" : 9.4
}

def show_menu(menu_dict):
    """Print all drinks and prices."""
    if not menu_dict:
        print("The menu is empty")

    else:
        for key, value in menu_dict.items():
            print(f'{key} \t- \t{value}₪')


def add_item(menu_dict):
    """Add a new drink to the menu."""
    drink_name = input("What is your drink name? ")
    price = float(input("What is your drink price? "))

    if drink_name in menu_dict:
        print(f"Item already exists")

    else:
        menu_dict[drink_name] = price


def update_price(menu_dict):
    """Change the price of an existing drink."""
    update_drink = input("Which drink should be updated?")

    if update_drink not in menu_dict:
        print("Item not found")

    else:
        new_price = float(input("What is your new price? "))
        menu_dict[update_drink] = new_price
        print("Price updated")


def delete_item(menu_dict):
    """Remove a drink from the menu."""
    del_drink = input("Which item should be removed?")


    if del_drink in menu_dict:
        del menu_dict[del_drink]
        print("Item deleted")

    else:
        print("Item not found")


def show_options():
    """Print the available actions."""
    print("What would you like to do?\n"
          "1. Show menu \n"
          "2. Add item\n"
          "3. Update price\n"
          "4. Delete item\n"
          "5. Exit\n"
    )

def run_coffee_shop():
    """Main loop of the program."""
    while True:
        show_options()
        choice = input("Choose an option:")

        if choice == "1":
            show_menu(menu_dict)

        elif choice == "2":
            add_item(menu_dict)

        elif choice == "3":
            update_price(menu_dict)

        elif choice == "4":
            delete_item(menu_dict)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, try again.")




run_coffee_shop()

    
    

