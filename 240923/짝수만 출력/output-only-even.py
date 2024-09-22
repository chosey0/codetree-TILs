import sys

a, b = [int(val) for val in sys.stdin.readline().split(" ")]
b = b + 1 if b % 2 == 0 else b

numbers = [i for i in range(a, b) if i % 2 == 0]
n = len(numbers)
s_numbers = []

while len(s_numbers) < n:
    s_numbers.append(str(numbers.pop(0)))
print(" ".join(s_numbers))