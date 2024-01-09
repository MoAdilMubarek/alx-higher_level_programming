#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    n = len(sys.argv) - 1
    count = 1
    if n == 0:
        print("0 arguments.")
    elif n == 1:
        print("1 argument:")
        print("1: {}:".format(sys.argv[1]))
    else:
        print("{} arguments:".format(n))
        while count <= n:
            print("{}: {}".format(count, sys.argv[count]))
            count += 1
