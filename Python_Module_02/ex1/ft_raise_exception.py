def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    if temp > 40:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
    elif temp < 0:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
    else:
        return temp


def test_temperature() -> None:
    for temp_test in ["25", "abc", "100", "-50"]:
        print(f"Input data is '{temp_test}'")
        try:
            temp = input_temperature(temp_test)
            print(f"Temperature is now {temp}°C\n")
        except ValueError as e:
            print(f"Caught input_temperature error: {e}\n")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    print("=== Garden Temperature Checker===\n")
    test_temperature()
