#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        real_x = min(x, len(my_list))
        for i in range(real_x):
            print(my_list[i], end=" ")
        print()
        return (real_x)
    except:
        return (0)
