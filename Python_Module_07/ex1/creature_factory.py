from ex0 import CreatureFactory, Creature  # noqa F401
from .creature import Shiftling, Sproutling, Bloomelle, Morphagon


class HealingCreatureFactory(CreatureFactory):
    """ create the base and evolved Creature for Sproutling and Bloomelle"""
    def create_base(self) -> Sproutling:
        return Sproutling()

    def create_evolved(self) -> Bloomelle:
        return Bloomelle()


class TransformCreatureFactory(CreatureFactory):
    """ create the base and evolved Creature for Shiftling and Morphagon"""
    def create_base(self) -> Shiftling:
        return Shiftling()

    def create_evolved(self) -> Morphagon:
        return Morphagon()
