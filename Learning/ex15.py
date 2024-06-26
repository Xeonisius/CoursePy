import sys
import re

pattern = re.compile(r'\b(\w+)\1\b')
for line in sys.stdin:
    line = line.rstrip()
    if pattern.search(line):
        print(line)
