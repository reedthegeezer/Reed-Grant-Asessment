menu = [
    "butter chicken pie",
    "steak and cheese pie",
    "mince and cheese pie",
    "aqua cna",
    "chicken sub",
    "juicy",
    "afghan cookie",
    "pork steam bun"
]

print("\nWelcome to the school canteen!\n")
for item in menu:
    print(f"{item.title()}")

order = input("\nWhat would you like to order:").lower()

if order in menu:
    print(f"You ordered a {order}, thank you have a nice day")
else:
    print("we do not have that item")