from ex0 import FlameFactory, AquaFactory, CreatureFactory


def test_factory(factory: CreatureFactory) -> None:
    print("Testing factory")
    creature_base = factory.create_base()
    print(f"{creature_base.describe()}")
    print(f"{creature_base.attack()}")
    creature_evolved = factory.create_evolved()
    print(f"{creature_evolved.describe()}")
    print(f"{creature_evolved.attack()}")
    print("")


def test_battle(factory_1: CreatureFactory,
                factory_2: CreatureFactory) -> None:
    print("Testing battle")

    creature_1 = factory_1.create_base()
    print(f"{creature_1.describe()}")
    print(" vs.")
    creature_2 = factory_2.create_base()
    print(f"{creature_2.describe()}")

    print(' fight!')

    print(f"{creature_1.attack()}")
    print(f"{creature_2.attack()}")


if __name__ == "__main__":
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()

    test_factory(flame_factory)
    test_factory(aqua_factory)
    test_battle(flame_factory, aqua_factory)
