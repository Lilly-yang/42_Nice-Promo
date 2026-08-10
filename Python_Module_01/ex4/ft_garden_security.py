class Plant:
    def __init__(self) -> None:
        self._plant_data: dict[str, dict[str, float | int]] = {}

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
        if height >= 0:
            return height
        else:
            print("height is invalid, reset to 0")
            self.set_height(name, 0)
            return 0.0

    def get_age(self, name: str) -> int:
        age = self._plant_data[name]['age']
        if age >= 0:
            if isinstance(age, int):
                return age
            else:
                return int(age)
        else:
            print("age is invalid, reset to 0")
            self.set_age(name, 0)
            return 0

    def show(self, name: str) -> None:
        h = self.get_height(name)
        a = self.get_age(name)
        print(f"{name}: "
              f"{round(h, 1)}cm, "
              f"{a} days old")

    # def grow(self) -> None:
    #     self.rose['height'] += self.rose_growth
    #     self.sunflower['height'] += self.sunflower_growth
    #     self.cactus['height'] += self.cactus_growth
    #     self.age()

    # def age(self) -> None:
    #     for plt in [self.rose, self.sunflower, self.cactus]:
    #         plt['age'] += 1

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


if __name__ == "__main__":
    plant = Plant()
    print("=== Garden Security System ===")
    plant.creat_plant('Rose', 15, 10)
    print("")
    plant.set_height('Rose', 25)
    plant.set_age('Rose', 30)
    print("")
    plant.set_height('Rose', -25)
    plant.set_age('Rose', -30)
    print("")
    print("Current state: ", end="")
    plant.show('Rose')
