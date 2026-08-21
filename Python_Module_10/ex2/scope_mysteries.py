from typing import Callable


def mage_counter() -> Callable:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> Callable:
    total_power = initial_power

    def accumulator(power: int) -> int:
        nonlocal total_power
        total_power += power
        return total_power

    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable:
    enchantment = enchantment_type

    def factory(name: str) -> str:
        return enchantment + " " + name

    return factory


def memory_vault() -> dict[str, Callable]:
    memory: dict[str, int] = {}

    def store(key: str, value: int) -> None:
        memory[key] = value

    def recall(key: str) -> str | int:
        return memory.get(key, "Memory not found")

    return {'store': store, 'recall': recall}


if __name__ == "__main__":
    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")

    print("\nTesting spell accumulator...")
    base = 100
    s_accumulator = spell_accumulator(base)
    add_1 = 20
    add_2 = 30
    print(f"Base {base}, add {add_1}: {s_accumulator(add_1)}")
    print(f"Base {base}, add {add_2}: {s_accumulator(add_2)}")

    print("\nTesting enchantment factory...")
    flaming_enchantment = enchantment_factory("Flaming")
    frozen_enchantment = enchantment_factory("Frozen")
    print(f"{flaming_enchantment('Sword')}")
    print(f"{frozen_enchantment('Shield')}")

    print("\nTesting memory vault...")
    m_vault = memory_vault()
    key = 'secret'
    value = 42
    print(f"Store '{key}' = {value}")
    m_vault['store'](key, value)
    print(f"Recall '{key}': {m_vault['recall'](key)}")
    unknow_key = 'unknown'
    print(f"Recall '{unknow_key}': {m_vault['recall'](unknow_key)}")
