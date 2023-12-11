import os


def rename_files_with_padding(directory, extensions):
    if not os.path.isdir(directory):
        raise FileNotFoundError("🚫 Directory does not exist.")

    if not isinstance(extensions, list):
        raise TypeError(
            "🚫 Extensions should be a list of file extensions (e.g., ['md', 'txt']).")

    # List all files found in the directory
    print("List of files found in the directory:\n")
    for i, file in enumerate(os.listdir(directory)):
        print(f"{i+1}) {file}")

    rename_results = []

    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_name, file_extension = os.path.splitext(file)

            if file_extension[1:] in extensions:
                parts = file_name.split('_', 1)
                if len(parts) == 2 and parts[0].isdigit():
                    number, name = parts
                    new_name = f"{int(number):02d}_{name}{file_extension}"
                    new_path = os.path.join(root, new_name)

                    if file_path != new_path:
                        os.rename(file_path, new_path)
                        rename_results.append((file, new_name))
                        print(f"✅ Renamed: {file} to {new_name}")
                else:
                    print(
                        f"⚠️ Warning: {file_path} does not follow the expected naming convention.")

    if rename_results:
        # Calculate the maximum width for the columns
        max_original_name_length = max(len("Original Name"), max(
            len(original_name) for original_name, _ in rename_results))
        max_modified_name_length = max(len("Modified Name"), max(
            len(modified_name) for _, modified_name in rename_results))

        # Print the table with centered headings
        print(f"\n{'Original Name'.center(max_original_name_length)}\t➡️\t{'Modified Name'.center(max_modified_name_length)}\n")
        for original_name, modified_name in rename_results:
            print(
                f"{original_name.center(max_original_name_length)}\t➡️\t{modified_name.center(max_modified_name_length)}")

        print("\n✅ All files have been renamed.")
    else:
        print("✅ No files have been renamed.")


if __name__ == "__main__":
    directory = "./Directory1/"
    extensions = ["md", "txt"]

    try:
        rename_files_with_padding(directory, extensions)
    except Exception as e:
        print(f"❌ Error: {str(e)}")
