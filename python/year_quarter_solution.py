def quarter_of(month):
    # your code here
    if month > 0 and month <= 12:
        months = list(range(1, 13))
        if month in months[:3]:
            # return 1       
            print(1)
        if month in months[3:6]:
            # return 2
            print(2)
        if month in months[6:9]:
            # return 3
            print(3)
        if month in months[9:]:
            # return 4
            print(4)

quarter_of(8)