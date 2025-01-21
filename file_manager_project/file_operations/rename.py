import os

def rename_files(target_name, digits_count, source_extension, target_extension, name_range=None, directory="."):
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist. Creating it now.")
        os.makedirs(directory)

    files = [f for f in os.listdir(directory) if f.endswith(source_extension)]
    if not files:
        print(f"No files with extension '{source_extension}' found in '{directory}'.")
        return

    counter = 1
    for file in files:
        original_name, _ = os.path.splitext(file)
        if name_range:
            start, end = name_range
            original_name = original_name[start - 1:end]
        counter_str = str(counter).zfill(digits_count)
        new_name = f"{original_name}{target_name}{counter_str}{target_extension}"
        old_path = os.path.join(directory, file)
        new_path = os.path.join(directory, new_name)
        os.rename(old_path, new_path)
        counter += 1

    print(f"Renamed {len(files)} files in directory '{directory}'.")
