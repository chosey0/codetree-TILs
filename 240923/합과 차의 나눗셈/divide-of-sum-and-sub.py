import sys

a, b = [int(i) for i in sys.stdin.readline().split(" ")]
print(f"""{round((a+b)/(a-b), 2)}""")