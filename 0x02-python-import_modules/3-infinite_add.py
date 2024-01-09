#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    count = 1
    res = 0
    while count < len(sys.argv):
        res += int(sys.argv[count])
        count += 1
    print(res)
