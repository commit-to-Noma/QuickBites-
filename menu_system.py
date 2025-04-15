#food menu for the ordering system

# Create a menu using a list of dictionaries
menu = [
    {"id": 1, "name": "Vegan Burger", "price": 65},
    {"id": 1, "name": "Coffee", "price": 18},
    {"id": 2, "name": "Fries", "price": 35},
    {"id": 3, "name": "Monster", "price": 21},
    {"id": 4, "name": "Spicy Pizza", "price": 65},
    {"id": 5, "name": "Chicken Wrap", "price": 40}
]

def get_menu():
    # Returns the menu list / fetch menu items.
    return menu

# prints the menu
if __name__ == "__main__":
    print("Menu Items:")
    for item in get_menu():
        print(f"{item['id']}. {item['name']} - R{item['price']:.2f}")
