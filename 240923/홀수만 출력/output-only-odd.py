import sys

ab = [int(val) for val in sys.stdin.readline().split(" ")]
ab.sort()

print(" ".join([str(i) for i in range(ab[0], ab[1]+1) if i % 2 != 0]))