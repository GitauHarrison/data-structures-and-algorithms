def square_it(digits):
    """
    Find a perfect square from the length of an integer
    """

    # 1. Import sqrt from math
    from math import sqrt

    # 2. Convert input integer into list
    digit_list = [int(elem) for elem in str(digits)]

    # 3. Get the length of the length of the list
    len_digit_list = len(digit_list)

    # 4. Get the multiplication factor of the input integer
    factor = int(sqrt(digits))

    # 5. Check if the length of the list is the same as the factor
    if len_digit_list == pow(factor, 2):

        # 6. If so, find equal chuncks of numbers in the list based on the length of the list
        for loop in range(0, len(digit_list), int(sqrt(len_digit_list))):
            num = digit_list[loop:loop + int(sqrt(len_digit_list))]

            # 7. Join the result of the chuncks
            print(''.join(str(item) for item in num))
    else:
        # 8. If the length of the list is not the same as the factor
        print(digits, "Not a perfect square!")

square_it(112141568)
