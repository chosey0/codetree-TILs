import sys

a, b = [int(val) for val in sys.stdin.readline().split(" ")]
print(f"{a} {b} {a+b}")