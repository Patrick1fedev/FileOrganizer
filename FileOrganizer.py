import os
import shutil


def organize_folder(path):
    if not os.path.isdir(path):
        print("Folder not found or not a directory")
        return

    current_script = os.path.abspath(__file__)

    for file in os.listdir(path):
        file_path = os.path.join(path, file)

        if not os.path.isfile(file_path):
            continue

        if os.path.abspath(file_path) == current_script:
            # do not move the script itself
            continue

        _, ext = os.path.splitext(file)
        if not ext:
            folder_name = "NO_EXT_files"
        else:
            folder_name = f"{ext[1:].upper()}_files"

        folder_path = os.path.join(path, folder_name)

        try:
            os.makedirs(folder_path, exist_ok=True)
            shutil.move(file_path, os.path.join(folder_path, file))
        except OSError as e:
            print(f"Error moving '{file}': {e}")

    print("Files organized successfully!")


if __name__ == "__main__":
    folder = input("Enter folder path: ")
    organize_folder(folder)