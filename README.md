# FileOrganizer

Simple script to organize files in a folder by extension.

## Usage

1. Run the script.
   
2. Enter the path of the target folder when prompted, e.g.:
   ```text
   C:\Users\Admin\Documents\MyFolder
   ```
3. The script creates subfolders like:
   - `TXT_files`
   - `PDF_files`
   - `NO_EXT_files` (files without extension)

## Behavior

- It checks the input is an existing directory.
- It skips non-files (directories, symlinks that are not regular files) and the script file itself.
- Files are moved into a folder named by extension (uppercase + `_files`).
- Files without extension are moved to `NO_EXT_files`.
- If a move operation fails, it prints an error and continues.

## Notes

- Use with a backup or test folder first. It moves files permanently.
- Avoid running inside a folder with important path-dependence while script is running.
