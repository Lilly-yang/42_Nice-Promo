import abc
from .creature import Flameling, Pyrodon, Aquabub, Torragon, Creature


class CreatureFactory(abc.ABC):
    @abc.abstractmethod
    def create_base(self) -> Creature:
        pass

    @abc.abstractmethod
    def create_evolved(self) -> Creature:
        pass


class FlameFactory(CreatureFactory):
    """ create the base and evolved Creature for Flameling and Pyrodon"""

    def create_base(self) -> Creature:
        return Flameling()

    def create_evolved(self) -> Creature:
        return Pyrodon()


class AquaFactory(CreatureFactory):
    """ create the base and evolved Creature for Aquabub and Torragon"""

    def create_base(self) -> Creature:
        return Aquabub()

    def create_evolved(self) -> Creature:
        return Torragon()
