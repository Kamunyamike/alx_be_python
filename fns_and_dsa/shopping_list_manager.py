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
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            Item_to_add = input("Enter the item to add: ")
            shopping_list.append(Item_to_add)
            pass
        elif choice == '2':
            # Prompt for and remove an item
            Item_to_remove = input("Enter the name of the item to be removed: ")
            shopping_list.remove(Item_to_remove)
            pass
        elif choice == '3':
            # Display the shopping list
            print(shopping_list)
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
main()

#/tmp/correction/7255496186836638723287432318175711409967_5/100741/1002469/fns_and_dsa/shopping_list_manager.py doesn't contain input\(['\"]Enter the item to add: ['\"]\)
