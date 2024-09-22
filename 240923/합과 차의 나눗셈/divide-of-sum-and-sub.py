import sys

a, b = [int(i) for i in sys.stdin.readline().split(" ")]
try:
    c = (a+b)/(a-b) 
    print(f"""{round(c, 2)}""")
except Exception as e:
    print(e)