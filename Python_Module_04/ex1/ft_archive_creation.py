import sys
import typing


def print_content(content: str) -> None:
    print("---\n")
    print(content, end="")
    print("---")


if __name__ == "__main__":
    argc = len(sys.argv)

    if argc == 1:
        print("Usage: ft_ancient_text.py <file>\n")
    else:
        print("=== Cyber Archives Recovery & Preservation ===")
        file_name = sys.argv[1]
        print(f"Accessing file '{file_name}'")
        try:
            f: typing.IO[str] = open(file_name)
            content = f.read()
            print_content(content)
            f.close()
            print(f"File '{file_name}' closed.\n")

            print("Transform data:")
            new_content = ""
            lines = content.splitlines()
            for line in lines:
                if line != "":
                    new_content += line + '#\n'
                else:
                    new_content += "\n"
            print_content(new_content)

            new_file_name = input("Enter new file name (or empty): ")
            if new_file_name != "":
                print(f"Saving data to '{new_file_name}'")
                new_f: typing.IO[str] = open(new_file_name, 'w')
                new_f.write(new_content)
                print(f"Data saved in file '{new_file_name}'.\n")
                new_f.close()
            else:
                print("Not saving data.")
        except Exception as e:
            print(f"Error opening file '{file_name}': {e}\n")
