plant_1 = {"name": "Rose", "height": 25, "age": 30}
plant_2 = {"name": "Sunflower", "height": 80, "age": 45}
plant_3 = {"name": "Cactus", "height": 15, "age": 120}


class Plant:
    def __init__(self, plant_1: dict, plant_2: dict, plant_3: dict) -> None:
        self.rose = plant_1
        self.sunflower = plant_2
        self.cactus = plant_3
        self.rose_growth = 0.8
        self.sunflower_growth = 6
        self.cactus_growth = 0.1

    def show(self, name: str) -> None:
        if name == "rose":
            plt = self.rose
        elif name == "sunflower":
            plt = self.sunflower
        elif name == "cactus":
            plt = self.cactus
        print(f"{plt['name']}: "
              f"{round(plt['height'], 1)}cm, "
              f"{plt['age']} days old")

    def grow(self) -> None:
        self.rose['height'] += self.rose_growth
        self.sunflower['height'] += self.sunflower_growth
        self.cactus['height'] += self.cactus_growth
        self.age()

    def age(self) -> None:
        for plt in [self.rose, self.sunflower, self.cactus]:
            plt['age'] += 1

    def show_growth(self, name: str, days: int) -> None:
        self.float_height()
        self.show(name)
        total_growth = 0.0
        for i in range(days):
            print(f"=== Day {i+1} ===")
            self.grow()
            if name == "rose":
                total_growth += self.rose_growth
            elif name == "sunflower":
                total_growth += self.sunflower_growth
            elif name == "cactus":
                total_growth += self.cactus_growth
            self.show(name)
        print(f"Growth this week: {total_growth}cm")

    def float_height(self) -> None:
        for plt in [self.rose, self.sunflower, self.cactus]:
            plt['height'] = float(plt['height'])


if __name__ == "__main__":
    plant = Plant(plant_1, plant_2, plant_3)
    print("=== Garden Plant Growth ===")
    plant.show_growth("rose", 7)
