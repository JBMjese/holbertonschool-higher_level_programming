#!/usr/bin/python3
# 2-args.py

if __name__ == "__main__":
    import sys
    """Print the number of and list of arguments."""
    count = int(len(sys.argv))
    if count == 1:
        print("{} arguments.".format(count -1))
    elif count == 2:
        print("{} argument:".format(count -1))
    else:
        print("{} arguments:".format(count -1))
    for i in range(1, count):
        print("{}: {}".format(i, sys.argv[i]))
