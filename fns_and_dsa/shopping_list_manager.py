# shopping_list_manager.py

# Start with an empty shopping list

def display_menu():
    print("\nShopping List Manager")
    print("1. Add an item")
    print("2. Remove an item")
    print("3. View the list")
    print("4. Exit")

shopping_list = []
while True:
    display_menu()
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        item = input("Enter the item to add: ")
        shopping_list.append(item)
        print(f"'{item}' has been added to the shopping list.")

    elif choice == "2":
        item = input("Enter the item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"'{item}' has been removed from the shopping list.")
        else:
            print(f"'{item}' was not found in the shopping list.")

    elif choice == "3":
        if shopping_list:
            print("\nYour Shopping List:")
            for i, item in enumerate(shopping_list, start=1):
                print(f"{i}. {item}")
        else:
            print("Your shopping list is empty.")

    elif choice == "4":
        print("Exiting Shopping List Manager. Goodbye!")
        break

    else:
        print("Invalid choice! Please select a valid option (1-4).")
