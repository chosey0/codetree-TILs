import sys

a, n = [int(val) for val in sys.stdin.readline().split(" ")]

for _ in range(n):
    a += n
    print(a)