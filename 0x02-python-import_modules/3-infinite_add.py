#!/usr/bin/python3
if __name__ == "__main__":
    import sys
narg = len(sys.argv)
sum = 0
for arg in range(1, narg):
    sum = sum + int(sys.argv[arg])
print(f"{sum}")
