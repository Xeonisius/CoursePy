import sys
for line in sys.stdin:
    line = line.rstrip()
    x = line.replace("human", "computer")
    print(x)