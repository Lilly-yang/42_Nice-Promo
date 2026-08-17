def secure_archive(file_name: str, file_mode: str = 'r',
                   file_write: str = "") -> tuple:
    try:
        if file_mode == 'w':
            with open(file_name, file_mode) as file:
                file.write(file_write)
                return (True, 'Content successfully written to file')
        else:
            with open(file_name) as file:
                content = file.read()
                return (True, content)
    except Exception as e:
        return (False, f"{e}")


if __name__ == "__main__":
    print("=== Cyber Archives Security ===")

    print("\nUsing 'secure_archive' to read from a nonexistent file:")
    print(secure_archive('/not/existing/file'))

    print("\nUsing 'secure_archive' to read from a inaccessible file:")
    print(secure_archive('/etc/shadow'))

    print("\nUsing 'secure_archive' to read from a regular file:")
    print(secure_archive('ancient_fragment.txt'))

    print("\nUsing 'secure_archive' to write previous content to a new file:")
    print(secure_archive('new_fragment.txt', 'w', 'Hello 42!'))
