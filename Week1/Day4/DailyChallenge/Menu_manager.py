""" Daily Challenge: Coffee Shop Menu Manager """

drinks_dict = {
    "fanta" : 7.0,
    "sprite" : 7.0,
    "coke" : 7.0,
    "milk" : 13.0,
    "water" : 4.5,
    "coffee" : 9.4
}
 #Print all the items in the required formats
def show_menu(drinks_dict):
    print('Current Menu:')
    for key, value in drinks_dict.items():
        print(f'{key.title()} \t- \t{value}₪')
show_menu(drinks_dict)