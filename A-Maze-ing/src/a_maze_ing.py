# from ..mazegen import MazeGenerator


def validate_config(key, value):
    if key in ["WIDTH", "HEIGHT", "SEED"]:
        return int(value)

    if key in ["ENTRY", "EXIT"]:
        return parse_coordinates(value)

    if key == "PERFECT":
        return value == "True"


def read_config(filename: str) -> dict[str, str]:
    config = {}

    with open(filename) as file:
        for line in file:
            line = line.strip()

            if not line or line.startswith("#"):
                continue

            key, value = line.split("=", 1)
            config[key] = validate_config(key, value)

    return config


def parse_coordinates(value: str) -> tuple[int, int]:
    x, y = value.split(",")
    return int(x), int(y)


if __name__ == "__main__":
    config = read_config("config.txt")

    # generator = MazeGenerator()
    # generator.generate()
    # maze = generator.get_maze()
    # solution = generator.get_solution()
