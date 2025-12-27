def water_plants(plant_list: list) -> None:
    """Water a list of plants,
    if an value is not valid, raise an error"""
    try:
        print("Opening watering system")
        for plant in plant_list:
            print("Watering " + plant)
    except Exception:
        print("Error: Cannot water None - invalid plant!")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    """Test the watering system wiht two palnts list,
    one with good values and one with bad value and handle
    the raised error with cleaning up at the end for all cases"""

    print("Testing normal watering...")
    good_list = ["tomato", "lettuce", "carrots"]
    water_plants(good_list)
    print("Watering completed successfully!")
    print("")
    print("Testing with error...")
    bad_list = ["tomato", None, "carrots"]
    water_plants(bad_list)
    print("")
    print("Cleanup always happens, even with errors!")


# Structure the output
print("=== Garden Watering System ===")
print("")
test_watering_system()
