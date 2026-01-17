def record_spell(spell_name: str, ingredients: str) -> str:
    """Check the ingredients if valid then record the spell,
    Use the validate ingredients functions to check.
    """
    try:
        # Use late(lazy) import to import in the function call.
        from .validator import validate_ingredients
    except Exception:
        return "Error Detected: Lazy importing failed"

    validation_result: str = validate_ingredients(ingredients)

    if validation_result == ingredients + " - VALID":
        return f"Spell recorded: {spell_name} ({validation_result})"

    elif validation_result == ingredients + " - INVALID":
        return f"Spell rejected: {spell_name} ({validation_result})"

    # Just to silent the prototype.
    return ""
