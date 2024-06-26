def min_operations(s, a, b):
    count = 0
    while a in s:
        s = s.replace(a, b)
        count += 1
        if count > 1000:
            return "Impossible"
    
    return count
s = input()
a = input()
b = input()
print(min_operations(s,a,b))