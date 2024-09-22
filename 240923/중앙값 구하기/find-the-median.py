import sys
import statistics as st

abc = sorted([int(val) for val in sys.stdin.readline().split(" ")])
print(abc[len(abc)//2]) if len(abc) % 2 == 0 else print(abc[(len(abc) - 1) // 2])