import sys
from typing import IO


def lire_fichier(file: IO[str]) -> str:
    return file.read()


def file_creator(name_file: str):
    open(f"{name_file}", "x")


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return
    content_file = sys.argv[1]
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{content_file}'")

    file = None
    try:
        file = open(content_file, 'r')
        right_file = lire_fichier(file)
        print("---")
        print(right_file)
        print("---")
    except OSError as e:
        print(f"Error opening file '{content_file}': {e}")
    finally:
        if file is not None:
            file.close()
            print(f"File: '{content_file}' closed.")

    print("Transform data")
    print("---")
    file_transfo = open('transform_data.txt', 'a')
    file_transfo.write('#')
    file_transfo = open('transform_data.txt', 'r')
    print(lire_fichier(file_transfo))
    print("---")

    if (namefile := input("Enter new file name (or empty):")):
        print(f"Saving data to '{namefile}'")
        print(f"Data saved as file '{namefile}'")
        fichier_final = file_creator(f"{namefile}")
        for line in file_transfo:
    
    else:
        print("Not saving file")


if __name__ == "__main__":
    main()
