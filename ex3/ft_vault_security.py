FRAGMENTS = (
    "[FRAGMENT 001] Digital preservation protocols established 2087\n"
    "[FRAGMENT 002] Knowledge must survive the entropy wars\n"
    "[FRAGMENT 003] Every byte saved is a victory against oblivion\n"
)


def secure_archive(
    file_name: str,
    action: str = "read",
    content: str = ""
) -> tuple[bool, str]:
    try:
        if action == "read":
            with open(file_name, "r") as file:
                return (True, file.read())
        if action == "write":
            with open(file_name, "w") as file:
                file.write(content)
            return (True, "Content successfully written to file")
        return (False, f"Unknown action '{action}'")
    except (OSError, UnicodeDecodeError) as e:
        return (False, str(e))


def main() -> None:
    print("=== Cyber Archives Security ===")
    secure_archive("regular_fragment.txt", "write", FRAGMENTS)

    print("\nUsing 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))

    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd"))

    print("\nUsing 'secure_archive' to read from a regular file:")
    result = secure_archive("regular_fragment.txt")
    print(result)

    print("\nUsing 'secure_archive' to write previous content to a new file:")
    if result[0]:
        print(secure_archive("new_fragment.txt", "write", result[1]))
    else:
        print("Nothing to write: reading failed.")


if __name__ == "__main__":
    main()
