def ft_plant_age():
    pt_age = int(input("Enter plant age in days: "))
    if pt_age > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
