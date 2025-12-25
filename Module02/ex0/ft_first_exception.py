def check_temperature(temp_str: str):
    """Check temperature value and handle invalud cases"""
    try:
        degrees = int(temp_str)
        if degrees < 0:
            print(f"Error: {degrees}°C is too cold for plants (min 0°C)")
        elif degrees > 40:
            print(f"Error: {degrees}°C is too hot for plants (max 40°C)")
        else:
            print(f"Temperature {degrees}°C is perfect for plants!")
            return degrees
    except ValueError:
        print(f"Error: {temp_str} is not a valid number")


def test_temperature_input() -> None:
    """Run some tests to check the temperature values"""
    values = ["25", "abc", "100", "-50"]
    for value in values:
        print(f"Testing temperature: {value}")
        check_temperature(value)
        print("")
    print("All tests completed - program didn't crash!")


test_temperature_input()
