import time

#Welcome and ask for name/class
print("Welcome to GHS School Canteen!")
time.sleep(1)

student_name = input("Name? ")
student_class = input("Class? ")

print(f"\nHello {student_name}! What would you like today?\n")
time.sleep(1)

# Menu dictionary
menu = {
    "1": ("Burger", 5),
    "2": ("Fries", 2.5),
    "3": ("Soda", 1.5),
    "4": ("Sandwich", 4),
    "5": ("Garlic Bread", 2)
}

# Store selected items
order = []

# Loop to select multiple items or remove
while True:
    print("----- SCHOOL CANTEEN MENU -----")
    for number, (item, price) in menu.items():
        print(f"{number}. {item} - ${price}")
    print("-------------------------------")
    print("Type 'done' to finish or 'remove' to remove an item.\n")
    
    choice = input("Enter the number of your choice: ")
    
    if choice.lower() == "done":
        break
    elif choice.lower() == "remove":
        if not order:
            print("Your order is empty, nothing to remove!\n")
            continue
        print("\nYour current order:")
        for i, (item, price) in enumerate(order, 1):
            print(f"{i}. {item} - ${price}")
        remove_choice = input("Enter the number of the item to remove: ")
        if remove_choice.isdigit() and 1 <= int(remove_choice) <= len(order):
            removed_item = order.pop(int(remove_choice)-1)
            print(f"Removed {removed_item[0]} from your order.\n")
        else:
            print("Invalid choice!\n")
    elif choice in menu:
        order.append(menu[choice])
        print(f"Added {menu[choice][0]} to your order!\n")
    else:
        print("Invalid choice! Try again.\n")

# -------- DISCOUNT FUNCTION --------
def apply_discount(total):
    discount_rate = 0.20  # 20% discount
    if total >= 20:
        discount = total * discount_rate
        total -= discount
        print(f"\nDiscount applied: -${discount:.2f}")
    else:
        print("\nNo discount applied.")
    return total
# -----------------------------------

# Print receipt
print("\n===== RECEIPT =====")
time.sleep(1)
print(f"Name: {student_name}")
time.sleep(1)
print(f"Class: {student_class}\n")
time.sleep(1)

total = 0
for item, price in order:
    print(f"{item} - ${price}")
    total += price

# Apply discount
total = apply_discount(total)

print(f"\nFinal Total: ${total:.2f}")
time.sleep(1)
print("===================")
time.sleep(1)
print("Thank you for your order!")
