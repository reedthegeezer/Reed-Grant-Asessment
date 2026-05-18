menu = [
    "butter chicken pie",
    "steak and cheese pie",
    "mince and cheese pie",
    "aqua cna",
    "chicken sub",
    "juicy",
    "afghan cookie",
    "pork steam bun"
] #menu with some items

print("\nWelcome to the school canteen!\n")
for item in menu:
    print(f"{item.title()}") #printing menu items

order = input("\nWhat would you like to order:").lower() #ordering what the user wants

if order in menu:
    print(f"You ordered a {order}, thank you have a nice day")
else:
    print("we do not have that item") #checks if it has item ordered, if not prints it doesn't have it