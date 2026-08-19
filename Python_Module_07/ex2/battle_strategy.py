import abc
from ex0 import Creature
from ex1 import HealCapability, TransformCapability
from typing import cast


class BattleStrategy(abc.ABC):
    @abc.abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass

    @abc.abstractmethod
    def act(self, creature: Creature) -> None:
        pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> None:
        print(f"{creature.attack()}")


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> None:
        if self.is_valid(creature):
            trans_creature = cast(TransformCapability, creature)
            print(f"{trans_creature.transform()}")
            print(f"{creature.attack()}")
            print(f"{trans_creature.revert()}")
        else:
            raise Exception(f"Invalid Creature '{type(creature).__name__}'"
                            " for this aggressive strategy")


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> None:
        if self.is_valid(creature):
            heal_creature = cast(HealCapability, creature)
            print(f"{creature.attack()}")
            print(f"{heal_creature.heal()}")
        else:
            raise Exception(f"Invalid Creature '{type(creature).__name__}' "
                            "for this defensive strategy")
