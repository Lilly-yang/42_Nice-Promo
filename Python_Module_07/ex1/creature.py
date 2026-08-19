from ex0 import Creature
from .capability import HealCapability, TransformCapability


class Sproutling(Creature, HealCapability):
    def describe(self) -> str:
        return "Sproutling is a Grass type Creature"

    def attack(self) -> str:
        return "Sproutling uses Vine Whip!"

    def heal(self) -> str:
        return "Sproutling heals it for a small amount"


class Bloomelle(Creature, HealCapability):
    def describe(self) -> str:
        return "Bloomelle is a Grass/Fairy type Creature"

    def attack(self) -> str:
        return "Bloomelle uses Petal Dance!"

    def heal(self) -> str:
        return "Bloomelle heals it and others for a large amount"


class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__()
        self.transformed = False

    def describe(self) -> str:
        return "Shiftling is a Normal type Creature"

    def attack(self) -> str:
        if self.transformed:
            return "Shiftling performs a boosted strike!"
        else:
            return "Shiftling attacks normally."

    def transform(self) -> str:
        self.transformed = True
        return "Shiftling shifts into a sharper form!"

    def revert(self) -> str:
        return "Shiftling returns to normal."


class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__()
        self.transformed = False

    def describe(self) -> str:
        return "Morphagon is a Normal/Dragon type Creature"

    def attack(self) -> str:
        if self.transformed:
            return "Morphagon unleashes a devastating morph strike!"
        else:
            return "Morphagon attacks normally."

    def transform(self) -> str:
        self.transformed = True
        return "Morphagon morphs into a dragonic battle form!"

    def revert(self) -> str:
        return "Morphagon stabilizes its form."
