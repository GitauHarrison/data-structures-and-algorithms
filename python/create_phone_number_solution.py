def create_phone_number(n):
    number_list = [str(x) for x in n]
    str_number_list = ''.join(number_list)
    part1 = str_number_list[0:3]
    part2 = str_number_list[3:6]
    part3 = str_number_list[6:]
    return f'({part1}) {part2}-{part3}'

create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
