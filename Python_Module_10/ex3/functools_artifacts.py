from typing import Callable, Any
from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0

    if operation == 'add':
        return reduce(add, spells)
    elif operation == 'multiply':
        return reduce(mul, spells)
    elif operation == 'max':
        return reduce(max, spells)
    elif operation == 'min':
        return reduce(min, spells)
    else:
        raise ValueError("Unknown operation: {operation}")


def base_enchantment(power: int, element: str, target: str) -> str:
    return f"Power: {power}, Element: {element}, Target: {target}"


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    fire = partial(base_enchantment, 50, "fire")
    ice = partial(base_enchantment, 50, "ice")
    lightning = partial(base_enchantment, 50, "lightning")

    return {'fire': fire, 'ice': ice, 'lightning': lightning}


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if n <= 1:
        return n

    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def spell(value: Any) -> str:
        return "Unknown spell type"

    @spell.register
    def _(value: int) -> str:
        return f"Damage spell: {value} damage"

    @spell.register
    def _(value: str) -> str:
        return f"Enchantment: {value}"

    @spell.register
    def _(value: list) -> str:
        return f"Multi-cast: {len(value)} spells"

    return spell


if __name__ == "__main__":
    spell_powers = [12, 44, 17, 41, 26, 33]
    operations = ['add', 'multiply', 'max', 'min']
    fibonacci_tests = [20, 15, 14]

    print("\nTesting spell reducer...")
    print(f"Sum: {spell_reducer(spell_powers, 'add')}")
    print(f"Product: {spell_reducer(spell_powers, 'multiply')}")
    print(f"Max: {spell_reducer(spell_powers, 'max')}")

    print("\nTesting partial enchanter...")
    enchanter = partial_enchanter(base_enchantment)
    print(f"{enchanter['fire']('Dragon')}")
    print(f"{enchanter['ice']('Dragon')}")
    print(f"{enchanter['lightning']('Dragon')}")

    print("\nTesting memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")
    # print(f"{memoized_fibonacci.cache_info()}")

    print("\nTesting spell dispatcher...")
    spell = spell_dispatcher()
    print(f"{spell(42)}")
    print(f"{spell('fireball')}")
    print(f"{spell(['Fire', 'Ice', 'Heal'])}")
    print(f"{spell(3.14)}")
