import sys

n = int(sys.stdin.readline())

if n >= 3000: print("book")
elif 3000 > n >= 1000: print("mask")
else: print("no")