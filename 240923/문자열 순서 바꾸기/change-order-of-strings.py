import sys

[print(string.strip()) for string in sys.stdin.readlines()[::-1]]