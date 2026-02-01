def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    """
    Sort magical artifacts in descending order
    based on their power value

    Arguments:
        - artifacts = list of dictionaries

    Return:
        - New list sorted in descending order

    """

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
    return list(map(lambda element: "* " + element + " *", spells))


def mage_stats(mages: list[dict]) -> dict:
    """"""
    tst = max(mages, key=lambda element: element['power'])
    
    return {'fuck': tst}


lst = [{"name": "fuck", "power": 34}, {"name": "you", "power": 2}]
spells = ["fuck", "you", "fireball"]


print(spell_transformer(spells))

obj = map(lambda x: x + "fuck", ["hello", "world"])

t = mage_stats(lst)

