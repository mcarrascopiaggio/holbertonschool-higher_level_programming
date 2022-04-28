#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
narg = len(sys.argv)
if narg != 4:
    print(f"Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)
a = int(sys.argv[1])
b = int(sys.argv[3])
op = sys.argv[2]
if op == "+":
    print(f"{a} {op} {b} = {add(a, b)}")
elif op == "-":
    print(f"{a} {op} {b} = {sub(a, b)}")
elif op == "/":
    print(f"{a} {op} {b} = {div(a, b)}")
elif op == "*":
    print(f"{a} {op} {b} = {mul(a, b)}")
else:
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)
