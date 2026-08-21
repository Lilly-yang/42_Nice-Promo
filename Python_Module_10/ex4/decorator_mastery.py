from typing import Callable
from functools import wraps
import time


def fireball() -> str:
    return "Fireball cast!"


def spell_timer(func: Callable[..., str]) -> Callable:
    @wraps(func)
    def wrapper(*args: object, **kwargs: object) -> str:
        print(f"Casting {func.__name__}")

        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start

        print(f"Spell completed in {elapsed:.3f} seconds")

        return result

    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable[..., str]) -> Callable:
        @wraps(func)
        def wrapper(self: object, spell_name: str, power: int) -> str:
            if power < min_power:
                return "Insufficient power for this spell"

            return func(self, spell_name, power)

        return wrapper

    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable[..., str]) -> Callable:
        @wraps(func)
        def wrapper(*args: object, **kwargs: object) -> str:
            for i in range(max_attempts):
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception:
                    print("Spell failed, retrying... "
                          f"(attempt {i+1}/{max_attempts})")
                    pass
            return f"Spell casting failed after {max_attempts} attempts"

        return wrapper

    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and name.replace(" ", "").isalpha()

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":
    test_powers = [5, 23, 14, 5]
    spell_names = ['lightning', 'freeze', 'shield', 'blizzard']
    mage_names = ['Casey', 'Nova', 'Jordan', 'Storm', 'Ash', 'Kai']
    invalid_names = ['Jo', 'A', 'Alex123', 'Test@Name']

    print("Testing spell timer...")
    print(f"Result: {spell_timer(fireball)()}")

    print("\nTesting retrying spell...")
    attempts = 0

    @retry_spell(3)
    def test_spell() -> str:
        global attempts
        attempts += 1

        if attempts <= 3:
            raise ValueError("Spell failed")

        return "Waaaaaaagh spelled !"
    print(f"{test_spell()}")
    print(f"{test_spell()}")

    print("\nTesting MageGuild...")
    mage_guild = MageGuild()
    print(f"{mage_guild.validate_mage_name('Casey')}")
    print(f"{mage_guild.validate_mage_name('Jo')}")
    print(f"{mage_guild.cast_spell('Lightning', 15)}")
    print(f"{mage_guild.cast_spell('Jordan', 9)}")
