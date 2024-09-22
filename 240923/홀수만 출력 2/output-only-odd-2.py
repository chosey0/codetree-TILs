import sys

ba = [int(val) for val in sys.stdin.readline().split(" ")]
ba.sort() # a -> b

result = [i for i in range(ba[0], ba[1]+1) if i % 2 != 0]
result.reverse()

print(str(result).replace("[", "").replace("]", "").replace(",", ""))