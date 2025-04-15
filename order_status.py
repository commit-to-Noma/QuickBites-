
# Simulates order progress and notifies the user

import time

def simulate_order_progress(order_summary):

    #  lets pretend like the kitchen is working on it and then quickly does it .

    print("\n Order received! Here's what you ordered:")
    for item in order_summary["items"]:
        print(f"- {item['name']} - R{item['price']:.2f}")
    print(f"Total: R{order_summary['total']:.2f}")
    
    print("\n Preparing your food...")
    time.sleep(2)  # adding a time delay

    print(" Packaging your order...")
    time.sleep(2)

    print("Your order is ready for pickup!\n")
