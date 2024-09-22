import sys

a, b = [int(val) for val in sys.stdin.readline().split(" ")]

if a > b:
    print(a*b)
else:
    print(b//a)