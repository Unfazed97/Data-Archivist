import sys
from typing import IO


def lire_fichier(file: IO[str]) -> str:
    return file.read()


def transform_data(content: str) -> str:
    new_content = ""
    for line in content.splitlines():
        new_content += line + "#\n"
    return new_content


def ask_file_name() -> str:
    try:
        return input("Enter new file name (or empty): ")
    except EOFError:
        return ""


def file_creator(name_file: str, content: str) -> bool:
    file = None
    try:
        file = open(name_file, "w")
        file.write(content)
        return True
    except OSError as e:
        print(f"Error opening file '{name_file}': {e}")
        return False
    finally:
        if file is not None:
            file.close()


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_archive_creation.py <file>")
        return
    content_file = sys.argv[1]
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{content_file}'")

    file = None
    try:
        file = open(content_file, 'r')
        right_file = lire_fichier(file)
        print("---\n")
        print(right_file)
        print("---")
    except (OSError, UnicodeDecodeError) as e:
        print(f"Error opening file '{content_file}': {e}")
        return
    finally:
        if file is not None:
            file.close()
            print(f"File '{content_file}' closed.")

    print("\nTransform data:")
    print("---\n")
    file_transfo = transform_data(right_file)
    print(file_transfo)
    print("---")

    if (namefile := ask_file_name()):
        print(f"Saving data to '{namefile}'")
        if file_creator(namefile, file_transfo):
            print(f"Data saved in file '{namefile}'.")
        else:
            print("Data not saved.")
    else:
        print("Not saving data.")


if __name__ == "__main__":
    main()
