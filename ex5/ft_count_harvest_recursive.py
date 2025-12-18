def ft_count_harvest_recursive() -> None:
    until_harvest: int = int(input("Days until harvest: "))

    def recursive_function(days) -> None:
        if days == until_harvest + 1:
            return
        print(f'Day {days}')
        recursive_function(days + 1)

    recursive_function(1)
    print("Harvest time!")
