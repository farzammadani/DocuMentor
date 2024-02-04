import os

def is_binary(file_path):
    """
    Simple heuristic to check if a file is binary:
    Attempts to decode a small portion of the file.
    """
    try:
        with open(file_path, 'rb') as file:
            chunk = file.read(1024)  # Read the first 1024 bytes
            if b'\0' in chunk:
                return True  # Found a null byte, likely a binary file
            chunk.decode('utf-8')
        return False
    except UnicodeDecodeError:
        return True

def create_clone_directory(source_dir, target_dir):
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    for root, dirs, files in os.walk(source_dir):
        for dir_ in dirs:
            os.makedirs(os.path.join(target_dir, os.path.relpath(os.path.join(root, dir_), source_dir)), exist_ok=True)

        for file in files:
            source_file_path = os.path.join(root, file)
            relative_path = os.path.relpath(root, source_dir)
            target_file_path = os.path.join(target_dir, relative_path, file + ".md")

            if is_binary(source_file_path):
                open(target_file_path, "w").close()
            else:
                with open(source_file_path, "r", encoding='utf-8', errors='replace') as source_file, open(target_file_path, "w", encoding='utf-8') as target_file:
                    target_file.write("Enter the documentation for this code below.\n\n---\n\n")
                    target_file.write(source_file.read())
                    target_file.write("\n\n---\n\nEnd of documentation")


def main():
    print("Enter the path to the codebase directory (use a format compatible with your operating system):")
    source_dir = input().strip().strip('"')
    print("Enter the directory path to create the clone (use a format compatible with your operating system):")
    target_dir = input().strip().strip('"')

    create_clone_directory(source_dir, target_dir)
    print("Clone creation complete!")

if __name__ == "__main__":
    main()
