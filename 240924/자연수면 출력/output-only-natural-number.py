import sys

a, b = [int(val) for val in sys.stdin.readline().split(" ")]

result = []

if a > 0:
    for _ in range(b):
        result.append(str(a))
    print("".join(result))
else:
    print(0)