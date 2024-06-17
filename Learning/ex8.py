import os

def find_directories_with_py_files(root_dir, archive_name):
    directories_with_py_files = set()

    for dirpath, _, filenames in os.walk(root_dir):
        if any(filename.endswith('.py') for filename in filenames):
            rel_path = os.path.relpath(dirpath, root_dir)
            full_path = os.path.join(archive_name, rel_path)
            directories_with_py_files.add(full_path)

    return sorted(directories_with_py_files)

archive_name = "main"

root_dir = "C:\\path\\main"

directories_with_py_files = find_directories_with_py_files(root_dir, archive_name)

output_file = 'directories_with_py_files.txt'

with open(output_file, 'w') as f:
    for directory in directories_with_py_files:
        f.write(directory + '\n')

print(f"Найденные директории сохранены в файл: {output_file}")
