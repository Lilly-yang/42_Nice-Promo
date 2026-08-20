from typing import Callable


def spell(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target}"


def heal(target: str, power: int) -> str:
    return f"Heals {target}"


def get_power(target: str, power: int) -> str:
    return str(power)


def spell_validation(target: str, power: int) -> bool:
    if power > 10:
        return True
    else:
        return False


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combiened(*args):
        return (spell1(*args), spell2(*args))

    return combiened


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(target, power):
        return base_spell(target, power * multiplier)

    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def casted(*args):
        if condition(*args):
            return spell(*args)
        else:
            return "Spell fizzled"

    return casted


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequenced(*args):
        return list(map(lambda speel: speel(*args), spells))

    return sequenced


if __name__ == "__main__":
    test_values = [20, 13, 6]
    test_targets = ['Dragon', 'Goblin', 'Wizard', 'Knight']

    print("\nTesting spell combiner..")
    combiner = spell_combiner(fireball, heal)
    result = combiner('Dragon', 20)
    print(f"Combined spell result: {', '.join(result)}")

    print("\nTesting power amplifier...")
    amplifier = power_amplifier(get_power, 3)
    print(f"Original: {get_power('Goblin', 13)}, "
          f"Amplified: {amplifier('Goblin', 13)}")

    # print("\nTesting conditional caster")
    # cater = conditional_caster(spell_validation, spell)
    # print(f"test when condition is true: {cater('Wizard', 11)}")
    # print(f"test when condition is false: {cater('Knight', 6)}")

    # print("\nTesting spell sequence")
    # sequence = spell_sequence([spell, fireball, heal])
    # result = sequence('Dragon', 20)
    # print(f"{' -> '.join(result)}")
