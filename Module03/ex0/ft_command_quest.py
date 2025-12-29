import sys

def test_command_quest() -> None:
    """"""
    print("=== Command Quest ===")

#test_command_quest()



print(sys.argv[1])

if sys.argv[0] == "cat":
    print("hello cat")
if sys.argv[0] == "dog":
    print("hello dog")
