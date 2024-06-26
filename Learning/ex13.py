import re
import sys

pattern = re.compile(r'z...z')
for line in sys.stdin:
    line = line.rstrip()
    if pattern.search(line):
        print(line)