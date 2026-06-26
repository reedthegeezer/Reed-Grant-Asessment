import json

#constants
MAX_STOCK = 20
TAX_RATE = 0.15
MAX_BALANCE = 100


def login():  # simple set login information
    max_attempts = 3
    attempts = 0

    print("\n-----LOGIN-----\n")

    while attempts < max_attempts:
        username = input("Enter username:")
        password = input("Enter password:")

        if username == "test" and password == "test":
            print("Login successful!\n")
            return True
        else:
            attempts += 1
            remaining = max_attempts - attempts
            print(f"Login Failed, you have {remaining} more attempts to login")

    print("Maximum login attempts exceeded.")
    return False

def get_balance():
    balance = float(input("How much money would you like to put into your account?(MAXIMUM 100, DO NOT DEPOSIT ANYMORE THAN THAT): $"))

    if balance > MAX_BALANCE:
        balance = MAX_BALANCE

    return balance

def display_menu(menu):
    print("\nWelcome to the school canteen!\n")
    print("MENU")
    print("-" * 40)

    for item in menu:
        print(f"{item['name'].title()} - ${item['price']:.2f} ({item['stock']} left)")

def take_order(menu):
    order = input("\nWhat would you like to order? ").lower()

    for item in menu:
        if item["name"] == order:
            return item

    return None

def process_order(item, balance):
    if item["stock"] <= 0:
        print("Sorry, that item is out of stock.")
        return balance

    tax = item["price"] * TAX_RATE
    total = item["price"] + tax

    if balance < total:
        print("You do not have enough money.")
        return balance
    

    balance -= total
    item["stock"] -= 1

    print("\n----- RECEIPT -----")
    print(f"Item: {item['name'].title()}")
    print(f"Price: ${item['price']:.2f}")
    print(f"GST (15%): ${tax:.2f}")
    print(f"Total: ${total:.2f}")
    print(f"Remaining Balance: ${balance:.2f}")

    save_invoice(item, tax, total)

    return balance

def save_invoice(item, tax, total):
    invoice = {
        "item": item["name"],
        "price": item["price"],
        "tax": round(tax, 2),
        "total": round(total, 2)
    }

    with open("invoice.json", "w") as file:
        json.dump(invoice, file, indent=4)

    print("Invoice saved to invoice.json")

menu = [
    {"name": "butter chicken pie", "price": 5.50, "stock": 10, 
     "calories": 450, "protein": "18g", "carbs": "35g", "fat": "22g", 
     "description": "Traditional New Zealand Pie Filled With Butter Chicken"},

    {"name": "steak and cheese pie", "price": 5.50, "stock": 8,
     "calories": 450, "protein": "18g", "carbs": "35g", "fat": "22g", 
     "description": "Traditional New Zealand Steak and Cheese pie"},

    {"name": "potato topper", "price": 5.50, "stock": 12,
    "calories": 450, "protein": "18g", "carbs": "35g", "fat": "22g", 
    "description": "A mince pastry with some cooked mashed potato on top"},

    {"name": "aqua can", "price": 3.50, "stock": 15},

    {"name": "chicken sub", "price": 6.50, "stock": 5,
     "calories": 450, "protein": "18g", "carbs": "35g", "fat": "22g", 
     "description": "A Sandwich With Bread, Chicken, Lettuce, Cheese and a special sauce"},

    {"name": "pork rib sub", "price": 6.50, "stock": 5,
     "calories": 450, "protein": "18g", "carbs": "35g", "fat": "22g", 
     "description": "A Sandwhich With Pork Ribs, BBQ Sauce and cheese"},
    
    {"name": "wrap", "price": 3.50, "stock": 7,
     "calories": 450, "protein": "18g", "carbs": "35g", "fat": "22g", 
     "description": "A Wrap with chicken, a basic salad inside and some dressing"},

    {"name": "brownie", "price": 3.00, "stock": 10,
     "calories": 450, "protein": "18g", "carbs": "35g", "fat": "22g", 
     "description": "Traditional New Zealand Brownie"},

    {"name": "slushy", "price": 2.50, "stock": 20}
    ] #menu with some items that include prices and stock amounts
if login():
        balance = get_balance()
        display_menu(menu)

        item = take_order(menu)

        if item:
            balance = process_order(item, balance)
        else:
            print("We do not have that item.")