def two_oldest_ages(ages):
    print(sorted(ages)[-2:])


def two_oldest_ages2(ages):
    max_num = max(ages)
    ages.remove(max_num)
    print([max(ages), max_num])

two_oldest_ages([42, 3, 0,21] )
two_oldest_ages2([421, 3, 0,21] )
