def find_next_square(sq):
    """
    Return the next square if sq is a square, -1 otherwise
    
    I have added the time.sleep() function to slow it down
    I have added more print statements so the output can be seen
    """
    from math import sqrt
    import time

    # 1. Loop through factors
    while True:

        # 2. Check if the parameter is a perfect square
        if sq / int(sqrt(sq)) == int(sqrt(sq)):

            # 3. If it is, find the next perfect square by adding 1 to its factor
            sq = pow(int(sqrt(sq)) + 1, 2)
            print(sq, ' = ', int(sqrt(sq)), '*', int(sqrt(sq)))
            print(sq, ' is perfect!')
            time.sleep(3)

        # 4. If the parameter is not a perfect square
        else:
            # 5. Print -1
            print(-1)
            print(sq, ' = ', int(sqrt(sq)), '*', int(sqrt(sq)))
            print(sq, ' is not a perfect square')
            time.sleep(3)
            sq = pow((int(sqrt(sq)) + 1), 2)
            continue

find_next_square(4)
