def ft_count_harvest_iterative() -> None:
    until_harvest: int = int(input("Days until harvest: "))
    for day in range(1, until_harvest + 1):
        print("Day", day)
    print("Harvest time!")
