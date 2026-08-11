import math


def get_player_pos() -> tuple:
    while True:
        new_coords: tuple[float, ...] = ()
        coords_get = input("Enter new coordinates "
                           "as floats in format 'x,y,z': ")
        coords_get_split = [x.strip() for x in coords_get.split(",")]
        if len(coords_get_split) != 3:
            print("Invalid syntax")
        else:
            for coord in coords_get_split:
                try:
                    new_coords = new_coords + (float(coord),)
                except ValueError as e:
                    print(f"Error on parameter '{coord}': {e}")
                    break
            if len(new_coords) == 3:
                break
    return new_coords


def get_distance(coords_1: tuple, coords_2: tuple) -> float:
    return math.sqrt((coords_2[0] - coords_1[0]) ** 2
                     + (coords_2[1] - coords_1[1]) ** 2
                     + (coords_2[2] - coords_1[2]) ** 2)


if __name__ == "__main__":
    print("=== Game Coordinate System ===")

    print("\nGet a first set of coordinates")
    coords_1 = get_player_pos()
    print(f"Got a first tuple: {coords_1}")
    print(f"It includes: X={coords_1[0]}, Y={coords_1[1]}, Z={coords_1[2]}")
    print(f"Distance to center: {round(get_distance(coords_1, (0,0,0)), 4)}")

    print("\nGet a second set of coordinates")
    coords_2 = get_player_pos()
    print("Distance between the 2 sets of coordinates: "
          f"{round(get_distance(coords_1, coords_2), 4)}")
