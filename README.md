# SequenciPy: Sequencing Your Files, Python-Style

SequenciPy is a Python script that helps you seamlessly rename files in a directory, following a specific naming convention. It's designed to make file sequencing and renaming easy and efficient.

## How It Works

The main script, `SequenciPy.py`, provides a function called `rename_files_with_padding(directory, extensions)`, which performs the following tasks:

- Validates the directory's existence.
- Verifies that the provided extensions are in the correct format.
- Renames files in the specified directory, adding leading zeros to ensure proper sequencing.

## Test Script

We provide a test script, tester.py, which helps you create a directory with a specific number of files for testing SequenciPy's functionality. It also deletes the directory if it already exists. Here's how you can use it:

```bash
python tester.py
```

The script will create a directory called "Directory1" and generate 11 files with the naming convention "1_file.txt," "2_file.txt," and so on. These files are ideal for testing SequenciPy's file renaming capabilities.
