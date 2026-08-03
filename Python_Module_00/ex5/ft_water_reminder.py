def ft_water_reminder():
    d_since_last_w = int(input("Days since last watering: "))
    if d_since_last_w > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
