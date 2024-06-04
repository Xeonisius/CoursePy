def build_dependencies(n):
    dependencies = {}
    for _ in range(n):
        line = input()
        if ':' in line:
            child, parents = line.split(' : ')
            parents = parents.split()
            dependencies[child] = parents
        else:
            child = line
            dependencies[child] = []
    return dependencies

def is_descendant(dependencies, start, end):
    if start == end:
        return True
    if start not in dependencies:
        return False
    for parent in dependencies[start]:
        if is_descendant(dependencies, parent, end):
            return True
    return False

def main():
    n = int(input())
    dependencies = build_dependencies(n)
    i = int(input())
    queries = []
    for _ in range(i):
        start, end = input().split()
        queries.append((start, end))
    
    for start, end in queries:
        if is_descendant(dependencies, end, start):
            print("Yes")
        else:
            print("No")

if __name__ == "__main__":
    main()
