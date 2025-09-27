# shopping_list_manager.py

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            item = input("Enter item name to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"Added: {item}")
            else:
                print("No item entered.")
        elif choice == '2':
            item = input("Enter item name to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"Removed: {item}")
            else:
                print(f"{item} not found in the shopping list.")
        elif choice == '3':
            if not shopping_list:
                print("Shopping list is empty.")
            else:
                print("Current shopping list:")
                for i, it in enumerate(shopping_list, start=1):
                    print(f"{i}. {it}")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
