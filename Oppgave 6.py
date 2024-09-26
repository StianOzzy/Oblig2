packing_list = []
while True:
    print("Packing List\n1. Add item to list\n2. Remove item from list\n3. Print List\n4. Exit")
    user_input = input("Write the corresponding number to execute a command\n\n> ")

    if user_input == "1":
        item_to_be_added =str(input("Enter the item to add\n\n> "))
        packing_list.append(item_to_be_added)
        print(f"This is currently your list:{packing_list}")
    elif user_input == "2":
        item_to_remove = str(input("Enter the item to remove\n\n> "))
        if item_to_remove in packing_list:
            packing_list.remove(item_to_remove)
            print(f"This is currently your list:{packing_list}")
        else:
            print("This item is not in the list\n")
    elif user_input == "3":
        print(f"This is currently your list:{packing_list}")
    elif user_input == "4":
        break
    else:
        print("Invalid input, please try again\n")