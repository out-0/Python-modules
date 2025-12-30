import sys
import math


def parsing_coordinate(args: str) -> None:
    """Parse the input string and convert to tuple and check for erros"""

    print(f'Parsing coordinates: "{args}"')
    # Split into list
    coordinate = args.split(',')
    position = ()
    try:
        for cor in coordinate:
            valid_coordinate = int(cor)
            position += (valid_coordinate,)
    except ValueError as e:
        print(f'Parsing invalid coordinates: "{args}"')
        print(f"Error parsing coordinates: {e}")
        print(f'Error details - Type: ValueError, Args: ("{e}",)')
        return

    x1, y1, z1 = (0, 0, 0)
    x2, y2, z2 = (position)
    distance = math.sqrt(
            (x2 - x1)**2 +
            (y2 - y1)**2 +
            (z2 - z1)**2
            )

    print(f"Parsed position: {position}")
    print(f"Distance between {0, 0, 0} and {position}: {distance:.2f}")


def test_coordinate_system() -> None:
    """Structure the Demo"""
    print("=== Game Coordinate System ===")
    print("")
    # Use __len__ method to avoid the builtin len
    # if no arguments provided create a position table
    if sys.argv.__len__() == 1:
        position = (10, 20, 5)
        # unpacking the tuple
        x1, y1, z1 = (0, 0, 0)
        x2, y2, z2 = (position)
        distance = math.sqrt(
                (x2 - x1)**2 +
                (y2 - y1)**2 +
                (z2 - z1)**2
                )
        print(f"Position created: {position}")
        print(
                f"Distance between ({x1}, {y1}, {z1}) and {position}: "
                f"{distance:.2f}"
                )
        print("")
        # Parse position of multi different inputs
        parsing_coordinate("3,4,0")
        print("")
        parsing_coordinate("abc,def,ghi")
        print("")

        # Demonstrate a tuple unpacking
        print("Unpacking demonstration:")
        position = (3, 4, 0)
        x, y, z = position
        print(f"Player at x={x}, y={y}, z={z}")
        print(f"Coordinates: X={x}, Y={y}, Z={z}")
    # Addisional, input from the commands line
    elif sys.argv.__len__() == 2:
        coordinate = sys.argv[1]
        coordinate.split(',')
        parsing_coordinate(coordinate)


# Run the demonstration
test_coordinate_system()
