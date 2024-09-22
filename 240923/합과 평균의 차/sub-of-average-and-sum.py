import sys
import statistics as st

vals = [int(val) for val in sys.stdin.readline().split(" ")]
print(f"{sum(vals)}\n{st.mean(vals)}\n{sum(vals)-st.mean(vals)}")