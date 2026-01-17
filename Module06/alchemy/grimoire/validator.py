
def validate_ingredients(ingredients: str) -> str:
    """Check the ingredients strings is valid.

    if all in the valid list = return valid
    else = return invalid
    """

    # Anything not in this list is invalid.
    valid_ingredients = ["fire", "water", "earth", "air"]

    ingredients_list = ingredients.split(' ')
    for word in ingredients_list:
        if word not in valid_ingredients:
            return f"{ingredients} - INVALID"

    # If all in the valid list.
    return f"{ingredients} - VALID"
