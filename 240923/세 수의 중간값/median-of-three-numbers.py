import sys

a, b, c = [int(val) for val in sys.stdin.readline().split(" ")]

if c > b > a: print(1)
else: print(0)