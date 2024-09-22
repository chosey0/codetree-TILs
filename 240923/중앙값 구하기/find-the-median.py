import sys

abc = [int(val) for val in sys.stdin.readline().split(" ")]
n = len(abc)
abc.sort()

if len(abc) % 2 == 0:
    print(abc[n//2])
else:
    print(abc[(n - 1) // 2])