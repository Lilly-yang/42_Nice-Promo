class Plant:
    def __init__(self) -> None:
        self._plant_data: dict[str, dict[str, float | int | str | bool]] = {}

    def creat_plant(
        self,
        name: str,
        height: float | int = 0.0,
        age: int = 0,
        growth: float = 0.1
    ) -> None:
        self._plant_data[name] = {'height': float(height),
                                  'age': age, 'growth': growth}
        print("Plant created: ", end="")
        self.show(name)

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

    def grow(self, name: str) -> None:
        height_value = self._plant_data[name]['height']
        growth_value = self._plant_data[name]['growth']
        if isinstance(height_value, (int, float)) and\
           isinstance(growth_value, (int, float)):
            self._plant_data[name]['height'] = \
                float(height_value + growth_value)
        else:
            self._plant_data[name]['height'] = 0.0
        self.age(name)

    def age(self, name: str) -> None:
        age_value = self._plant_data[name]['age']
        if isinstance(age_value, (int, float)):
            self._plant_data[name]['age'] = int(age_value + 1)
        else:
            self._plant_data[name]['age'] = 0

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
        self._plant_data: dict[str, dict[str, float | int | str | bool]] = {}

    def creat_plant(self, name: str, height: float | int = 0.0, age: int = 0,
                    growth: float = 0.1, color: str = '') -> None:
        self._plant_data[name] = {'height': float(height), 'age': age,
                                  'growth': growth,
                                  'color': color, 'bloom': False}

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

    def creat_plant(self, name: str, height: float | int = 0.0, age: int = 0,
                    growth: float = 0.1, trunk_diameter: float = 0.0) -> None:
        self._plant_data[name] = {'height': float(height), 'age': age,
                                  'growth': growth,
                                  'trunk_diameter': float(trunk_diameter)}

    def produce_shade(self, name: str) -> None:
        print(f"Tree {name} now produce a shade of "
              f"{self._plant_data[name]['height']}cm long "
              f"and {self._plant_data[name]['trunk_diameter']}cm wide.")

    def show(self, name: str) -> None:
        super().show(name)
        print(f" Trunk diameter: {self._plant_data[name]['trunk_diameter']}cm")


class Vegertable(Plant):
    def __init__(self) -> None:
        super().__init__()
        self._plant_data: dict[str, dict[str, float | int | str | bool]] = {}

    def creat_plant(self, name: str, height: float | int = 0.0, age: int = 0,
                    growth: float = 0.1, harvest_season: str = '',
                    nutri_value: int = 0) -> None:
        self._plant_data[name] = {'height': float(height), 'age': age,
                                  'growth': growth,
                                  'harvest_season': harvest_season,
                                  'nutritional_value': nutri_value}

    def grow(self, name: str) -> None:
        super().grow(name)
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


if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    print("=== Flower")
    flower = Flower()
    flower.creat_plant('Rose', 15, 10, color='red')
    flower.show('Rose')
    # asking the rose to bloom
    flower.bloom('Rose')
    flower.show('Rose')
    print("")

    print("=== Tree")
    tree = Tree()
    tree.creat_plant('Oak', 200, 365, trunk_diameter=5)
    tree.show('Oak')
    # asking the oak to produce shade
    tree.produce_shade('Oak')
    print("")

    print("=== Vegetable")
    vege = Vegertable()
    vege.creat_plant('Tomato', 5, 10, 2.1, 'April', 0)
    vege.show('Tomato')
    # make tomato grow and age for 20 days
    for i in range(20):
        vege.grow('Tomato')
    vege.show('Tomato')
