import os

script_files = {}
root_dir = '\engineer challenge\venv'

for subdir, dirs, files in os.walk(root_dir):
    for file in files:
        if file.endswith('.sh') or file.endswith('.py'):
            filepath = os.path.join(subdir, file)
            with open(filepath, 'r') as f:
                first_line = f.readline().strip()
                if first_line.startswith('#!'):
                    interpreter = first_line[2:].strip()
                    if interpreter not in script_files:
                        script_files[interpreter] = 1
                    else:
                        script_files[interpreter] += 1

for interpreter, count in script_files.items():
    print(f"{interpreter}: {count} script files")
