import sys
import typing


if __name__ == "__main__":
    argc = len(sys.argv)

    if argc == 1:
        print("Usage: ft_ancient_text.py <file>\n")
    else:
        print("=== Cyber Archives Recovery ===")
        file_name = sys.argv[1]
        print(f"Accessing file '{file_name}'")
        try:
            f: typing.IO[str] = open(file_name)
            print("---\n")
            print(f.read(), end="")
            print("---")
            f.close()
            print(f"File '{file_name}' closed.")
        except Exception as e:
            print(f"Error opening file '{file_name}': {e}\n")
