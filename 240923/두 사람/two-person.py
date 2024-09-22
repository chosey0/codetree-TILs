import sys

a = [items.strip().split(" ") for items in sys.stdin.readlines()]
result = 0

for age, sex in a:
    if int(age) >= 19 and sex == "M": result = 1
    else: continue

print(result)