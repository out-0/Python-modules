import sys


def test_command_quest() -> None:
    """Parse the command line arguments and print them in formated output"""

    print("=== Command Quest ===")
    if len(sys.argv) == 1:
        print("No arguments provided!")
        print(f"Program name: {sys.argv[0]}")
        print(f"Total arguments: {len(sys.argv)}")
        print("")
    else:
        print(f"Program name: {sys.argv[0]}")
        argv_count = len(sys.argv)
        print(f"Arguments received: {argv_count - 1}")
        i = 1
        while i < argv_count:
            print(f"Argument {i}: {sys.argv[i]}")
            i += 1
        print(f"Total arguments: {i}")
        print("")


test_command_quest()
