import abc


class Creature(abc.ABC):
    @abc.abstractmethod
    def attack(self) -> str:
        pass

    @abc.abstractmethod
    def describe(self) -> str:
        pass


class Flameling(Creature):
    def attack(self) -> str:
        return "Flameling uses Ember!"

    def describe(self) -> str:
        return "Flameling is a Fire type Creature"


class Pyrodon(Creature):
    def attack(self) -> str:
        return "Pyrodon uses Flamethrower!"

    def describe(self) -> str:
        return "Pyrodon is a Fire/Flying type Creature"


class Aquabub(Creature):
    def attack(self) -> str:
        return "Aquabub uses Water Gun!"

    def describe(self) -> str:
        return "Aquabub is a Water type Creature"


class Torragon(Creature):
    def attack(self) -> str:
        return "Torragon uses Hydro Pump!"

    def describe(self) -> str:
        return "Torragon is a Water type Creature"
