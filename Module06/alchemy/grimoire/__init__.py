from .spellbook import record_spell
from .validator import validate_ingredients

# To silent the unused (flake8)
record_spell("Anything", "AnotherAnything")
validate_ingredients("Anything")
