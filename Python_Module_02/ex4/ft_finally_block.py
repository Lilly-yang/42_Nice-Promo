class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    if plant_name[0].isupper():
        pass
    else:
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")


def test_watering_system(plants: list = []) -> None:
    print("Opening watering system")
    try:
        for plant_name in plants:
            try:
                water_plant(plant_name)
                print(f"Watering {plant_name}: [OK]")
            except PlantError as e:
                print(f"Caught PlantError: {e}")
                print(".. ending tests and returning to main")
                break
    finally:
        print("Closing watering system")


if __name__ == "__main__":
    print("--- Garden Watering System ===")

    print("\nTesting valid plants...")
    test_watering_system(['Tomato', 'Lettuce', 'Carros'])
    print("\nTesting invalid plants...")
    test_watering_system(['Tomato', 'lettuce', 'Carros'])

    print("\nCleanup always happens, even with errors!")
