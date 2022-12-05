def same_case(a, b): 
    # your code here
    if  a.isalpha() and b.isalpha():
        if a.islower() == b.islower() or a.isupper() == b.isupper():
            # return 1
            print(1)
        else:
            # return 0
            print(0)
    else:
        # return -1
        print(-1)
    