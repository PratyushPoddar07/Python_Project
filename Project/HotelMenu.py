menu = {
    'Pizza': 40,
    'Pasta': 50,
    'Burger': 60,
    'Salad': 70,
    'Coffee': 80
}


def display_menu():

    """Display the menu item and their prices."""

    print("\nMenu:")
    for item, price in menu.items():
        print(f"{item}: Rs {price}")

def add_item_to_order():

    """aLLOW THE USER TO ADD AN ITEM TO THE ORDER AND RETURN THE PRICE."""

    item_1 =input("Enter the name of item you want to order = ")

    if item_1 in menu:
        print(f"Your item {item_1} has been added to your order")
        return menu[item_1]
    else:
        print(f"Order item {item_1} is not available yet!")
        return 0

def take_order():
    """Handle the order processs for multiple items."""

    total_order = 0
    while True:
        total_order += add_item_to_order()
        another_order =input("Do you want to add another item? (Yes/NO) ")
        if another_order != 'yes':
            break
    return total_order

# Greet customer
print("Welcome to mini Restaurant")

# Display menu
display_menu()

# Take the order
total_amount = take_order()

# Display the total amount to pay
print(f"\n The total amount to pay is Rs {total_amount}.")



