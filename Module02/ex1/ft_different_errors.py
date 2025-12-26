def garden_operations(error_type: str) -> None:
    """Based on the specific input, calling the specific
    condition to result the intended exception"""
    if error_type == "value":
        int("abc")
    elif error_type == "zero":
        23 / 0
    elif error_type == "file":
        file_name = "notexists.txt"
        open(file_name, "r")
    elif error_type == "key":
        plants = {}
        plants["missing\\_plant"]


def test_error_types() -> None:
    """Calling the failing operations and caught the errors
    with printing whats happen, without crashing"""
    print("Testing ValueError...")
    try:
        garden_operations("value")
    except ValueError:
        print("Caught ValueError: invalid literal for int()")
    print("")
    print("Testing ZeroDivisionError...")
    try:
        garden_operations("zero")
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")
    print("")
    print("Testing FileNotFoundError...")
    try:
        garden_operations("file")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'")
    print("")
    print("Testing KeyError...")
    try:
        garden_operations("key")
    except KeyError:
        print("Caught KeyError: 'missing\\_plant'")
    print("")
    print("Testing multiple errors together...")
    try:
        garden_operations("value")
        garden_operations("zero")
        garden_operations("file")
    except (ValueError, ZeroDivisionError, FileNotFoundError):
        print("Caught an error, but program continues!")
    print("")
    print("All error types tested successfully!")


# Main
print("=== Garden Error Types Demo ===")
print("")
test_error_types()
