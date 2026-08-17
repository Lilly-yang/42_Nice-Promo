from .light_spellbook import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed_ingredients = light_spell_allowed_ingredients()

    if ingredients in allowed_ingredients:
        if ingredients in ingredients.lower():
            return f"{ingredients} - VALID"

    return f"{ingredients} - INVALID"
