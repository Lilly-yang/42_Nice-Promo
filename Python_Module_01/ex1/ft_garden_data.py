plant_1 = {"name": "Rose", "height": 25, "age": 30}
plant_2 = {"name": "Sunflower", "height": 80, "age": 45}
plant_3 = {"name": "Cactus", "height": 15, "age": 120}


class Plant:
    def __init__(self, plant_1: dict, plant_2: dict, plant_3: dict) -> None:
        self.rose = plant_1
        self.sunflower = plant_2
        self.cactus = plant_3

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


if __name__ == "__main__":
    plant = Plant(plant_1, plant_2, plant_3)
    print("=== Garden Plant Registry ===")
    plant.show("rose")
    plant.show("sunflower")
    plant.show("cactus")
