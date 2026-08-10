class Plant:
    class PlantStatistics:
        def __init__(self) -> None:
            self.statistics: dict[str, dict[str, int]] = {}

        def creat_statistics(self, name: str) -> None:
            self.statistics[name] = {'grow': 0, 'age': 0, 'show': 0}

        # def show_statistics(self):
        #     print(f"")

    def __init__(self) -> None:
        self._plant_data: dict[str, dict[str, float | int | str | bool]] = {}
        self._plant_statistics = Plant.PlantStatistics()

    def creat_plant(
        self,
        name: str = '',
        height: float | int = 0.0,
        age: int = 0,
        growth: float = 0.1
    ) -> None:
        self._plant_data[name] = {'height': float(height),
                                  'age': age, 'growth': growth}
        self._plant_statistics.creat_statistics(name)
        # print("Plant created: ", end="")
        # self.show(name)

    def set_height(self, name: str, height: float | int) -> None:
        if height >= 0:
            try:
                self._plant_data[name]['height'] = float(height)
                print(f"Height updated: {height}cm")
            except KeyError:
                print("Plant dosen't exist.")
        else:
            print(f"{name}: Error, height can't be negative\n"
                  "Height update rejected")

    def set_age(self, name: str, age: int) -> None:
        if age >= 0:
            try:
                self._plant_data[name]['age'] = age
                print(f"Age updated: {age} days")
            except KeyError:
                print("Plant dosen't exist.")
        else:
            print(f"{name}: Error: age can't be negative\n"
                  "Age update rejected")

    @staticmethod
    def check_age(age: int) -> None:
        print(f"Is {age} days more than a year? -> ", end="")
        if age > 365:
            print("True")
        else:
            print("False")

    def get_height(self, name: str) -> float:
        height = self._plant_data[name]['height']
        if isinstance(height, (int, float)) and height >= 0:
            return float(height)
        print("height is invalid, reset to 0")
        self.set_height(name, 0)
        return 0.0

    def get_age(self, name: str) -> int:
        age = self._plant_data[name]['age']
        if isinstance(age, (int, float)) and age >= 0:
            return int(age)
        print("age is invalid, reset to 0")
        self.set_age(name, 0)
        return 0

    def show(self, name: str) -> None:
        h = self.get_height(name)
        a = self.get_age(name)
        print(f"{name}: "
              f"{round(h, 1)}cm, "
              f"{a} days old")
        self._plant_statistics.statistics[name]['show'] += 1

    def grow(self, name: str, grow_height: float = 0) -> None:
        height_value = self._plant_data[name]['height']
        growth_value = self._plant_data[name]['growth']

        if isinstance(height_value, (int, float)) and\
           isinstance(growth_value, (int, float)):
            if grow_height:
                self._plant_data[name]['height'] = \
                    float(height_value + grow_height)
            else:
                self._plant_data[name]['height'] = \
                    float(height_value + growth_value)
        else:
            self._plant_data[name]['height'] = 0.0
        # self.age(name)
        self._plant_statistics.statistics[name]['grow'] += 1

    def age(self, name: str, days: int = 1) -> None:
        age_value = self._plant_data[name]['age']
        if isinstance(age_value, (int, float)):
            self._plant_data[name]['age'] = int(age_value + days)
        else:
            self._plant_data[name]['age'] = 0
        self._plant_statistics.statistics[name]['age'] += 1

    # def show_growth(self, name: str, days: int) -> None:
    #     self.float_height()
    #     self.show(name)
    #     total_growth = 0.0
    #     for i in range(days):
    #         print(f"=== Day {i+1} ===")
    #         self.grow()
    #         if name == "rose":
    #             total_growth += self.rose_growth
    #         elif name == "sunflower":
    #             total_growth += self.sunflower_growth
    #         elif name == "cactus":
    #             total_growth += self.cactus_growth
    #         self.show(name)
    #     print(f"Growth this week: {total_growth}cm")

    # def float_height(self) -> None:
    #     for plt in [self.rose, self.sunflower, self.cactus]:
    #         plt['height'] = float(plt['height'])


class Flower(Plant):
    def __init__(self) -> None:
        super().__init__()

    def creat_plant(self, name: str = '', height: float | int = 0.0,
                    age: int = 0, growth: float = 0.1,
                    color: str = '') -> None:
        self._plant_data[name] = {'height': float(height), 'age': age,
                                  'growth': growth,
                                  'color': color, 'bloom': False}
        self._plant_statistics.creat_statistics(name)

    def bloom(self, name: str) -> None:
        self._plant_data[name]['bloom'] = True

    def show(self, name: str) -> None:
        super().show(name)
        print(f" Color: {self._plant_data[name]['color']}")
        if self._plant_data[name]['bloom']:
            print(f" {name} is blooming beautifully!")
        else:
            print(f" {name} has not bloomed yet")


class Tree(Plant):
    def __init__(self) -> None:
        super().__init__()

    def creat_plant(self, name: str = '', height: float | int = 0.0,
                    age: int = 0, growth: float = 0.1,
                    trunk_diameter: float = 0.0) -> None:
        self._plant_data[name] = {'height': float(height), 'age': age,
                                  'growth': growth,
                                  'trunk_diameter': float(trunk_diameter)}
        self._plant_statistics.creat_statistics(name)
        self._plant_statistics.statistics[name]['shade'] = 0

    def produce_shade(self, name: str) -> None:
        print(f"Tree {name} now produce a shade of "
              f"{self._plant_data[name]['height']}cm long "
              f"and {self._plant_data[name]['trunk_diameter']}cm wide.")
        self._plant_statistics.statistics[name]['shade'] += 1

    def show(self, name: str) -> None:
        super().show(name)
        print(f" Trunk diameter: {self._plant_data[name]['trunk_diameter']}cm")


class Vegertable(Plant):
    def __init__(self) -> None:
        super().__init__()

    def creat_plant(self, name: str = '', height: float | int = 0.0,
                    age: int = 0, growth: float = 0.1,
                    harvest_season: str = '', nutri_value: int = 0) -> None:
        self._plant_data[name] = {'height': float(height), 'age': age,
                                  'growth': growth,
                                  'harvest_season': harvest_season,
                                  'nutritional_value': nutri_value}
        self._plant_statistics.creat_statistics(name)

    def grow(self, name: str, grow_height: float = 0) -> None:
        super().grow(name, grow_height)
        nutritional_value = self._plant_data[name]['nutritional_value']
        if isinstance(nutritional_value, (int, float)):
            self._plant_data[name]['nutritional_value'] = nutritional_value + 1
        else:
            self._plant_data[name]['nutritional_value'] = 0

    def show(self, name: str) -> None:
        super().show(name)
        print(f" Harvest season: {self._plant_data[name]['harvest_season']}\n"
              f" Nutritional value: "
              f"{self._plant_data[name]['nutritional_value']}")


class Anonymous(Plant):
    def __int__(self) -> None:
        super().__init__()

    # def creat_plant(self, name = '', height = 0.0, age = 0, growth = 0.1):
    #     super().creat_plant(name, height, age, growth)
    #     # print(f"Unknown plant: {float(height)}cm, {age} days old")


class Seed(Flower):
    def __init__(self) -> None:
        super().__init__()

    def creat_plant(self, name: str = '', height: float | int = 0.0,
                    age: int = 0, growth: float = 0.1, color: str = '',
                    seed_gain: int = 0) -> None:
        self._plant_data[name] = {'height': float(height), 'age': age,
                                  'growth': growth, 'color': color,
                                  'bloom': False,
                                  'seed_gain': seed_gain, 'seed': 0}
        self._plant_statistics.creat_statistics(name)

    def bloom(self, name: str) -> None:
        super().bloom(name)
        seed_value = self._plant_data[name]['seed']
        seed_gain_value = self._plant_data[name]['seed_gain']

        if isinstance(seed_value, (int, float)) and\
           isinstance(seed_gain_value, (int, float)):
            self._plant_data[name]['seed'] = int(seed_value + seed_gain_value)

    def show(self, name: str) -> None:
        super().show(name)
        print(f" Seeds: {self._plant_data[name]['seed']}")


def show_statistics(plant_statistics: dict) -> None:
    print(f"Stats: {plant_statistics['grow']} grow, "
          f"{plant_statistics['age']} age, "
          f"{plant_statistics['show']} show")
    if 'shade' in plant_statistics:
        print(f" {plant_statistics['shade']} shade")


if __name__ == "__main__":
    print("=== Garden statistics ===")
    plant = Plant()

    print("=== Check year-old")
    plant.check_age(30)
    plant.check_age(400)
    print("")

    print("=== Flower")
    flower = Flower()
    flower.creat_plant('Rose', 15, 10, 8, 'red')
    # statistics for Rose
    flower.show('Rose')
    show_statistics(flower._plant_statistics.statistics['Rose'])
    # asking the rose to grow and bloom
    flower.grow('Rose')
    flower.bloom('Rose')
    flower.show('Rose')
    # statistics for Rose
    show_statistics(flower._plant_statistics.statistics['Rose'])
    print("")

    print("=== Tree")
    tree = Tree()
    tree.creat_plant('Oak', 200, 365, trunk_diameter=5)
    tree.show('Oak')
    # statistics for Oak
    show_statistics(tree._plant_statistics.statistics['Oak'])
    # asking the oak to produce shade
    tree.produce_shade('Oak')
    # statistics for Oak
    show_statistics(tree._plant_statistics.statistics['Oak'])
    print("")

    print("=== Seed")
    seed = Seed()
    seed.creat_plant('Sunflower', 80, 45, 1.5, 'yellow', 42)
    seed.show('Sunflower')
    # make sunflower grow, age and bloom
    seed.grow('Sunflower', 30)
    seed.age('Sunflower', 20)
    seed.bloom('Sunflower')
    seed.show('Sunflower')
    # statistics for Sunflower
    show_statistics(seed._plant_statistics.statistics['Sunflower'])
    print("")

    print("=== Anonymous")
    anonymous = Anonymous()
    anonymous.creat_plant('Unknown plant')
    anonymous.show('Unknown plant')
    # statistics for Unknown plant
    show_statistics(anonymous._plant_statistics.statistics['Unknown plant'])
