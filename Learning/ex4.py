def build_dependencies(n):
    dependencies = {}
    for _ in range(n):
        line = input().strip()
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
    n = int(input().strip())
    dependencies = build_dependencies(n)
    m = int(input().strip())
    exceptions = [input().strip() for _ in range(m)]
    
    redundant_exceptions = []
    for i in range(m):
        for j in range(i):
            if is_descendant(dependencies, exceptions[i], exceptions[j]):
                redundant_exceptions.append(exceptions[i])
                break
    
    for exception in redundant_exceptions:
        print(exception)

if __name__ == "__main__":
    main()
