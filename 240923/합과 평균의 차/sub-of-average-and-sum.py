import sys

vals = [int(val) for val in sys.stdin.readline().split(" ")]
v_sum = sum(vals)
v_mean = int(v_sum/len(vals))

print(f"{v_sum}\n{v_mean}\n{v_sum-v_mean}")