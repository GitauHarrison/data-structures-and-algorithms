#!/usr/bin/env python3

def find_middle_element(n):
    """
    Create a function that when provided with a triplet,
    returns the index of the numerical element that lies
    between the other two elements.

    Example 1:

    func([20,7, 49])

    The middle element in this list is 20 since it lies
    between 7 and 49. Given the list above, 20 is at index 0.

    Example 2:

    func([7, 8, 13])

    The middle element is 8 since it lies between 7 and 13.
    The exact index of element 8 in the above list is 1.
    """

    # 1. Sort list in ascending order

    sorted_list = sorted(n)

    # 2. Find the middle element from the sorted list

    index_middle_elem = len(sorted_list)//2
    elem = sorted_list[index_middle_elem]

    # 3. Find the index of the middle elem in the original list

    index_elem_original_list = n.index(elem)

    # 4. Print result

    print(index_elem_original_list)


find_middle_element([20,7, 49])
