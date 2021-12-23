#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    le = len(argv) - 1
    if le == 0:
        print("0 arguments.")
    elif le == 1:
        print("1 argument:")
        print("1: {}".format(argv[1]))
    elif le >= 2:
        print("{:d} arguments:".format(le))
        for i in range(1, le + 1):
            print("{:d}: {:s}".format(i, argv[i]))
