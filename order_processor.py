# This handles taking user selections and generating an order summary

from menu_system import get_menu


# for demo purposes: a student number with credit balance
student_credits = {
    "ST10492795": 235.00 
}

def process_order(selected_ids):
    # Takes a list of selected menu item IDs and returns a summary of the order.
    
    menu = get_menu()
    ordered_items = []
    total = 0

    for item_id in selected_ids:
        # Search the menu for a matching item by ID
        for item in menu:
            if item["id"] == item_id:
                ordered_items.append(item)
                total = total + item["price"]
                break

    # Create a result 
    return {
        "items": ordered_items,
        "total": round(total, 2)
    }

def check_balance(student_id):
    #Check food credit balance for the student
    return student_credits.get(student_id, 0.00)  # Return balance or 0.00 if not found

def choose_payment_method():
    #Prompt user to choose a payment method
    print("\nChoose a payment method:")
    print("1. Food credits")
    print("2. Card")
    print("3. Cash")

    while True:
        try:
            method = int(input("Enter the number of your choice: "))
            if method == 1:
                return "Food credits"
            elif method == 2:
                return "Card"
            elif method == 3:
                return "Cash"
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
        except ValueError:
            print("Please enter a number.")

if __name__ == "__main__":
    # Example order with item IDs
    test_order = [1, 3, 5]
    summary = process_order(test_order)

    # Display the order summary
    print("\n Order Summary:")
    for item in summary["items"]:
        print(f"- {item['name']} - R{item['price']:.2f}")
    print(f"Total: R{summary['total']:.2f}")

    # Choose payment method
    payment_method = choose_payment_method()
    

    if payment_method == "Food credits":
        # Ask user for their student ID (to check credits)
        student_id = input("Enter your student ID: ")
        balance = check_balance(student_id)

        if balance >= summary["total"]:
            student_credits[student_id] -= summary["total"]  # Deduct credits after successful payment
            print(f" Payment successful. Remaining balance: R{student_credits[student_id]:.2f}")
            # Generate confirmation code for pickup
            import random
            pickup_code = random.randint(1000, 9999)
            print(f"\n Order confirmed! Show this pickup code: #{pickup_code}")
        else:
            print(f" Not enough credits (Balance: R{balance:.2f}). Please choose another payment method.")
    else:
        print(f" Payment method selected: {payment_method}")
        # Generate confirmation code for pickup only for successful payment
        print("\n Payment successful.")
        import random
        pickup_code = random.randint(1000, 9999)
        print(f" Show this pickup code: #{pickup_code}")
