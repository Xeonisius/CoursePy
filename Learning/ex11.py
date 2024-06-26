def count_substring_occurrences(s, t):
    count = 0
    start = 0
    
    while start <= len(s) - len(t):
        if s[start:start + len(t)] == t:
            count += 1
        start += 1
    
    return count
s = input()
t = input()
print(count_substring_occurrences(s, t))
