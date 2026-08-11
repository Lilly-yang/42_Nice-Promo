import sys


def gen_inventory(argvs: list) -> dict:
    inventory: dict[str, int] = {}
    for av in argvs:
        inventory_get = [x.strip() for x in av.split(":")]
        if len(inventory_get) == 2:
            if inventory_get[0] in inventory:
                print(f"Redundant item '{inventory_get[0]}' - discarding")
            else:
                try:
                    inventory[inventory_get[0]] = int(inventory_get[1])
                except ValueError as e:
                    print(f"Quantity error for '{inventory_get[0]}': {e}")
        else:
            print(f"Error - invalid parameter '{av}'")
    return inventory


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")

    argc = len(sys.argv)
    if argc > 1:
        inventory = gen_inventory(sys.argv[1:])
        print(f"Got inventory: {inventory}")
        print(f"Item list: {[item for item in inventory]}")
        total_quantity = sum(inventory.values())
        print(f"Total quantity of the {len(inventory)} items: "
              f"{total_quantity}")

        for k in inventory.keys():
            most_abundant_quantity = inventory[k]
            least_abundant_quantity = inventory[k]
            break

        for k in inventory.keys():
            print(f"Item {k} represents "
                  f"{round(inventory[k] / total_quantity * 100, 1)}%")
            if inventory[k] > most_abundant_quantity:
                most_abundant_quantity = inventory[k]
            if inventory[k] < least_abundant_quantity:
                least_abundant_quantity = inventory[k]

        for k in inventory.keys():
            if inventory[k] == most_abundant_quantity:
                print(f"Item most abundant: {k} with quantity {inventory[k]}")
                break

        for k in inventory.keys():
            if inventory[k] == least_abundant_quantity:
                print(f"Item least abundant: {k} with quantity {inventory[k]}")
                break

        inventory.update({'magic_item': 1})
        print(f"Updated inventory: {inventory}")
