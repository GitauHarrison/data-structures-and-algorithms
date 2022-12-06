def unique_in_order(test_list):
    # 1. Covert string to list
    my_list = [elem for elem in test_list]

    # 2. Create a new list to store unique elements
    unique_list = []

    # 3. Loop through the list
    for elem in my_list:
        # 4. Check if the unique list is empty
        if not unique_list:
            # 5. If so, add an item to it
            unique_list.append(elem)
        # 6. With one item added, confirm if this item is similar to the iteration
        elif unique_list[-1] != elem:
            # 7. If it is not, then append to the unique list
            unique_list.append(elem)
    # Return the unique list
    print(unique_list)

unique_in_order('AAAABBBCCDAABBB')