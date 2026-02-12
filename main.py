import time

# 1️⃣ Welcome and ask for name/class
print("Welcome to GHS School Canteen!")
time.sleep(1)

student_name = input("Name? ")
student_class = input("Class? ")

print(f"\nHello {student_name}! What would you like today?\n") # The /n makes python go to the new line
time.sleep(1)

# 2️⃣ Menu dictionary
menu = {
    "1": ("Burger", 5),#Comma makes it so that the one below doesnt come up as red
    "2": ("Fries", 2.5),
    "3": ("Soda", 1.5),
    "4": ("Sandwich", 4),
    "5": ("Garlic Bread", 2)
}

# 3️⃣ Store selected items
order = []

# 4️⃣ Loop to select multiple items or remove
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
        # Show current order
        print("\nYour current order:")
        for i, (item, price) in enumerate(order, 1):
            print(f"{i}. {item} - ${price}")
        # Ask which one to remove
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

# 5️⃣ Print receipt
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

print(f"\nTotal: ${total}")
time.sleep(1)
print("===================")
time.sleep(1)
print("Thank you for your order!")
