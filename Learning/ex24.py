def build_dependencies(data):
    dependencies = {}
    for item in data:
        child = item["name"]
        parents = item["parents"]
        dependencies[child] = parents
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
    input_data = input().strip()

    data = eval(input_data)

    dependencies = build_dependencies(data)

    descendants_count = {cls: 0 for cls in dependencies}

    for cls in dependencies:
        for potential_descendant in dependencies:
            if is_descendant(dependencies, potential_descendant, cls) and cls != potential_descendant:
                descendants_count[cls] += 1

    for cls in sorted(descendants_count):
        print(f"{cls} : {descendants_count[cls]+1}")

if __name__ == "__main__":
    main()
