def display_menu():
    print("1. Add item")
    print("2. View list")
    print("3. Quit")

shopping_list = []

while True:
    display_menu()
    try:
        choice = int(input("Enter your choice (number): "))  # <-- cast to int
    except ValueError:
        print("Please enter a number!")
        continue

    if choice == 1:
        item = input("Item to add: ")
        shopping_list.append(item)
    elif choice == 2:
        print("Shopping List:", shopping_list)
    elif choice == 3:
        print("Goodbye!")
        break
    else:
        print("Invalid option.")
