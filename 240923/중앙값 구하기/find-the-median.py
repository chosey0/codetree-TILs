import sys
import statistics as st

abc = [int(val) for val in sys.stdin.readline().split(" ")]

print(st.median(abc))