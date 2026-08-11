import sys

if __name__ == "__main__":
    print("=== Command Quest ===")

    file_path = __file__
    file_name = file_path.split("/")[-1]
    print(f"Program name: {file_name}")

    argc = len(sys.argv)
    if argc > 1:
        print(f"Arguments received: {argc - 1}")
        for i in range(1, argc):
            print(f"Argument {i}: {sys.argv[i]}")
    else:
        print("No arguments provided!")
    print(f"Total arguments: {argc}\n")
