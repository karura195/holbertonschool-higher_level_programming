#!/usr/bin/python3
import sys
if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("0")
    elif len(sys.argv) == 2:
        print("{:d}".format(sys.argv[2]))
    else:
        sum = 0
        for i in range(1, len(sys.argv)):
            sum = sum + int(sys.argv[i])
        print("{:d}".format(sum))
