import sys

a, s = sys.stdin.readlines()
b, c, d, e = s.strip().split(" ")
a, b, c, d, e = int(a), int(b), int(c), int(d), int(e)

for i in [b, c, d, e]:
    if a > i:print(1)
    else: print(0)