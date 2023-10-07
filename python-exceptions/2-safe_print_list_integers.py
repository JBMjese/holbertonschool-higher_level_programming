#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        real_x = min(x, len(my_list))
        printed = 0
        for i in range(real_x):
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end=" ")
                printed += 1
            print()
            return (printed)
    except:
        return (0)
