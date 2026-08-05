class Plant:
    def __init__(self) -> None:
        self.plant_data: dict[str, dict] = {}

    def creat_plant(
        self,
        name: str,
        height: float | int,
        age: int,
        growth: float = 0.1
    ) -> None:
        new_plant = {'height': float(height), "age": age, "growth": growth}
        self.plant_data[name] = new_plant

    def show(self, name: str) -> None:
        print(f"{name}: "
              f"{round(self.plant_data[name]['height'], 1)}cm, "
              f"{self.plant_data[name]['age']} days old")

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
    plant.creat_plant("Rose", 25, 30, 0.8)
    plant.creat_plant("Oak", 200, 365)
    plant.creat_plant("Cactus", 5, 90, 0.1)
    plant.creat_plant("Sunflower", 80, 45, 6)
    plant.creat_plant("Fern", 15, 120)
    print("=== Plant Factory Output ===")
    for k in plant.plant_data.keys():
        print("Created: ", end="")
        plant.show(k)
