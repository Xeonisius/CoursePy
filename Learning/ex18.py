import sys
import re

for line in sys.stdin:
    line = line.strip()
    new_line = re.sub(r'(\b\w)(\w)', r'\2\1', line)
    print(new_line)