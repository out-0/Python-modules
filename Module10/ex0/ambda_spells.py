def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    """
    Sort magical artifacts in descending order
    based on their power value

    Arguments:
        - artifacts = list of dictionaries

    Return:
        - New list sorted in descending order

    """
    if not artifacts:
        print("ERROR: NO ARTIFACTS PROVIDED 🧿")
        return []

    return sorted(artifacts,
                  key=lambda element: element["power"],
                  reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    """Filter mages by power

    Arguments:
        - Mages = list of mages with power info

    Return:
        - Filtered list of mages which have power
          grater than or equal min_power

    """
    # Check invalid data
    if not mages:
        print("ERROR: NO MAGES PROVIDED 🧙🧙‍♀️🧙‍♂️")
        return []

    # For each element in the iterator list, apply the lambda
    # function, and just keep the elements pass the condition
    # with true
    filtered: filter = filter(
            lambda element: element["power"] >= min_power, mages)

    # Convert the filter object to a list
    return list(filtered)


def spell_transformer(spells: list[str]) -> list[str]:
    """Transform spell names:
    add "* " prefix and " *" suffix

    • Arguments:
        - list of spell names (strings)
    • Return:
        - A list of transformed spell names
    """
    if not spells:
        print("ERROR: NO SPELL PROVIDED 🪄 ")
        return []

    return list(map(lambda element: "* " + element + " *", spells))


def mage_stats(mages: list[dict]) -> dict:
    """
    Calculate statistics of mages:
        - Most powerful
        - Least powerful
        - Average power of mages

    Arguments:
        list or mages dictionaries.
    Return:
        Dictionary contain -max power -min power -avg power

    """

    if not mages:
        print("ERROR: NO MAGES PROVIDED 🧙🧙‍♀️🧙‍♂️")
        return {}
    # Extract statistics
    most_powerful: dict = max(mages, key=lambda element: element["power"])
    least_powerful: dict = min(mages, key=lambda element: element["power"])
    sum_of_powers: float = sum(mage["power"] for mage in mages)
    # Round the average to 2 decimal(2.546 -> 2.55 | 2.434 -> 2.43)
    average: float = round(sum_of_powers / len(mages), 2)

    return {
        "max_power": most_powerful["power"],
        "min_power": least_powerful["power"],
        "avg_power": average,
    }


def main() -> None:
    """starting point for demonstration"""

    # List the artifacts
    artifacts = [
        {"name": "Storm Crown", "power": 106, "type": "focus"},
        {"name": "Wind Cloak", "power": 95, "type": "relic"},
        {"name": "Water Chalice", "power": 61, "type": "weapon"},
        {"name": "Ice Wand", "power": 66, "type": "armor"},
    ]

    print("\nTesting artifact sorter...\n")
    # Sort the artifacts based on their power.
    sorted_artifacts: list[dict] = artifact_sorter(artifacts)
    for art in sorted_artifacts:
        print(f"- {art['name']} ({art['power']} power) type: {art['type']}")

    # List of mages
    mages = [
        {"name": "Phoenix", "power": 69, "element": "earth"},
        {"name": "Ember", "power": 59, "element": "fire"},
        {"name": "Phoenix", "power": 58, "element": "shadow"},
        {"name": "Alex", "power": 97, "element": "water"},
        {"name": "Morgan", "power": 87, "element": "ice"},
    ]

    print("\nTesting power filter...\n")
    # Filter the powerful mages with power >= 80
    sorted_mages: list[dict] = power_filter(mages, 80)
    for mage in sorted_mages:
        print(
            f"- mage: {mage['name']}, "
            f"with power {mage['power']} "
            f"specialized in {mage['element']}"
        )

    print("\nTesting spell transformer...\n")
    # Modified the spells name
    spells = ["flash", "freeze", "fireball", "tsunami"]
    for spell in spell_transformer(spells):
        print(spell)

    print("\nTesting power filter...\n")
    mages_statistic: dict = mage_stats(mages)
    print(f"Most power: {mages_statistic['max_power']}")
    print(f"Least power: {mages_statistic['min_power']}")
    print(f"average power: {mages_statistic['avg_power']}")


if __name__ == "__main__":
    main()
