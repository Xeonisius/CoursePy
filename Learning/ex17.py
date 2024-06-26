import sys
import re

pattern = re.compile(r'\b[aA]+\b', re.IGNORECASE)
for line in sys.stdin:
    line = line.rstrip()
    modified_line = pattern.sub('argh', line, count=1)
    print(modified_line)
