def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    return temp


def test_temperature() -> None:
    for temp_test in ["25", "abc"]:
        print(f"Input data is '{temp_test}'")
        try:
            temp = input_temperature(temp_test)
            print(f"Temperature is now {temp}°C\n")
        except ValueError as e:
            print(f"Caught input_temperature error: {e}\n")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    print("=== Garden Temperature ===\n")
    test_temperature()
