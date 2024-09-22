import sys

a = int(sys.stdin.readline())
for i in [3, 5]:
    if a % i == 0:
        print("YES")
    else:
        print("NO")