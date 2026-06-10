def login():
    print("\n-----LOGIN-----\n")
    username = input("Enter username:")
    password = input("Enter password:")

    if username == "test" and password == "test":
        print("Login successful!\n")
        return True
    else:
        print("Login failed!\n")
        return False
def display_menu(menu):
    print("\nWelcome to the school canteen!\n")
    print("MENU:")
    print("-" * 30)
    for item in menu:
        # item[0] is name, item[1] is price
        print(f"{item[0].title()} - ${item[1]:.2f}")
def take_order(menu):
    order = input("\nWhat would you like to order:").lower()  #ordering what the user wants

    menu_items = [item[0] for item in menu]
    if order in menu_items:
        for item in menu:
            if item[0] == order:
                print(f"You ordered a {order}")
                print(f"That will be ${item[1]:.2f}, thank you come again!")
                break
    else:
        print("We do not have that item.")
menu = [
    ("butter chicken pie", 5.50),
    ("steak and cheese pie", 5.50),
    ("potato topper", 5.50),
    ("aqua can", 3.50),
    ("chicken sub", 6.50),
    ("pork rib sub", 6.50),
    ("wrap", 3.50),
    ("brownie", 3.00),
    ("slushy", 2.50),
] #menu with some items
if login():
    display_menu(menu)
    take_order(menu)