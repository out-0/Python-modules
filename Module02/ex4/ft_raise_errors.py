def check_plant_health(plant_name: str,
                       water_level: int,
                       sunlight_hours: int
                       ) -> str:
    """Check and raise an ValueError in invalid args cases"""
    if plant_name is None or plant_name == "":
        raise ValueError("Plant name cannot be empty!")
    elif water_level < 1:
        raise ValueError(f"Water level {water_level} is too low (min 1)")
    elif water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)")
    elif sunlight_hours < 2:
        raise ValueError(f"Sunlight hours {sunlight_hours} is too low (min 2)")
    elif sunlight_hours > 12:
        raise ValueError(
                f"Sunlight hours {sunlight_hours} is "
                "too high (max 12)"
                )
    return f"Plant '{plant_name}' is healthy!"


def test_plant_checks():
    """Try several test cases and handle the error raised from the
    failed cases"""
    tests = [
            ("Testing good values...", "tomato", 5, 6),
            ("Testing empty plant name...", None, 3, 6),
            ("Testing bad water level...", "potato", 15, 4),
            ("Testing bad sunlight hours...", "carrots", 7, 0)
            ]
    for test, plant_name, water_level, sun_hours in tests:
        try:
            print(test)
            print(check_plant_health(plant_name, water_level, sun_hours))
        except ValueError as e:
            print(f"Error: {e}")
        print("")
    print("All error raising tests completed!")


print("=== Garden Plant Health Checker ===")
print("")
test_plant_checks()
