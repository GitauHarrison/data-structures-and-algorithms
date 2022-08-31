def count_bits(n):
    """
    Count occurance of bits equal to 1
    """
    # 1. Covert integer to binary (returns a string)
    my_binary = f'{n:b}'

    # 2. Loop through the result to create list elements
    binary_list = [int(value) for value in my_binary]

    # 3. Find the number of occurance of bits equivalent to 1
    print(binary_list.count(1))

count_bits(10)
