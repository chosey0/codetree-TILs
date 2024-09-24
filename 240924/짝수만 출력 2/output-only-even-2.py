import sys

b, a = [int(val) for val in sys.stdin.readline().split(" ")]
result = []

while a < b + 1:
    if a % 2 == 0:
        result.append(str(a))
        a += 1
    else:
        a += 1
        continue
    
result.reverse()
print(" ".join(result))