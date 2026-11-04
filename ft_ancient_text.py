import sys
from typing import IO


def lire_fichier(file: IO[str]) -> str:
    return file.read()


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return
    content_file = sys.argv[1]
    print("=== Cyber Archives Recovery ===")
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


if __name__ == "__main__":
    main()
