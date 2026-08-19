from ex0 import FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import NormalStrategy, AggressiveStrategy, DefensiveStrategy


def battle(opponents: list) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved\n")

    for i, opp_1 in enumerate(opponents):
        factory_1 = opp_1[0]
        creature_1 = factory_1.create_base()
        strategy_1 = opp_1[1]

        for j in range(i+1, len(opponents)):
            opp_2 = opponents[j]
            factory_2 = opp_2[0]
            creature_2 = factory_2.create_base()
            strategy_2 = opp_2[1]

            print("\n* Battle *")
            print(f"{creature_1.describe()}")
            print(" vs.")
            print(f"{creature_2.describe()}")

            print(" now fight!")
            try:
                strategy_1.act(creature_1)
                strategy_2.act(creature_2)
            except Exception as e:
                print(f"Battle error, aborting tournament: {e}")
    print("")


if __name__ == "__main__":
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()
    healing_factory = HealingCreatureFactory()
    transform_factory = TransformCreatureFactory()

    # Create the three strategies
    normal = NormalStrategy()
    aggressive = AggressiveStrategy()
    defensive = DefensiveStrategy()

    print("Tournament 0 (basic)\n"
          " [ (Flameling+Normal), (Healing+Defensive) ]")
    opponents_list_0 = [(flame_factory, normal), (healing_factory, defensive)]
    battle(opponents_list_0)

    print("Tournament 1 (error)\n"
          " [ (Flameling+Aggressive), (Healing+Defensive) ]")
    opponents_list_1 = [(flame_factory, aggressive),
                        (healing_factory, defensive)]
    battle(opponents_list_1)

    print("Tournament 2 (multiple)\n"
          " [ (Aquabub+Normal), (Healing+Defensive), "
          "(Transform+Aggressive) ]")
    opponents_list_2 = [(aqua_factory, normal), (healing_factory, defensive),
                        (transform_factory, aggressive)]
    battle(opponents_list_2)
