def display_menu(menu):
    print("\nWelcome to the school canteen!\n")
    print("MENU:")
    print("-" * 30)
    for item in menu:
        # item[0] is name, item[1] is price
        print(f"{item[0].title()} - ${item[1]:.2f}")

def take_order(menu):
    order = input("\nWhat would you like to order:").lower() #ordering what the user wants
    if order in menu:
        print(f"You ordered a {order}, thank you have a nice day")
    else:
        print("we do not have that item") #checks if it has item ordered, if not prints it doesn't have it

menu = [
    ("butter chicken pie", 5.50),
    ("steak and cheese pie", 5.50),
    ("potato topper", 5.50),
    ("steak and cheese pie", 5.50),
    ("aqua can", 3.50),
    ("chicken sub", 6.50),
    ("pork rib sub", 6.50),
    ("wrap", 3.50),
    ("brownie", 3.00),
    ("slushy", 2.50),
] #menu with some items

display_menu(menu)
take_order(menu)