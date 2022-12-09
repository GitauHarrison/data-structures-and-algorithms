# def comp(list1, list2):
#     # your code
#     for list1_elem in list1:
#         for list2_elem in sorted(list2):
#             if pow(list1_elem, 2) == list2_elem:
#                 print(pow(list1_elem, 2), "=", list1_elem, "*" , list1_elem)
#                 print(True)
#                 return True
#             else:
#                 print(False)
#                 return False


# a1 = [121, 144, 19, 161, 19, 144, 19, 11]
# a2 = [11*11, 121*121, 144*144, 190*190, 161*161, 19*19, 144*144, 19*19]

# comp(a1, a2)



def comp(list1, list2):
    # your code
    try:
        return sorted(pow(i, 2) for i in list1) == sorted(list2)
    except:
            return False


a1 = [121, 144, 19, 161, 19, 144, 19, 11]  
a2 = [132, 14641, 20736, 361, 25921, 361, 20736, 361]

comp(a1, a2)