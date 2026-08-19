from pydantic import BaseModel, Field, ValidationError
from datetime import datetime


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: str | None = Field(default=None, max_length=200)


def show_station(station: SpaceStation, show_time: bool = False) -> None:
    if station.station_id:
        print(f"ID: {station.station_id}")

    if station.name:
        print(f"Name: {station.name}")

    if station.crew_size:
        print(f"Crew: {station.crew_size} people")

    if station.power_level is not None:
        print(f"Power: {station.power_level}%")

    if station.oxygen_level is not None:
        print(f"Oxygen: {station.oxygen_level}%")

    if show_time:
        print(f"Last maintenance: {station.last_maintenance}")

    if station.is_operational:
        print("Status: Operational")
    else:
        print("Status: non-operational")

    if station.notes:
        print(f"{station.notes}")


if __name__ == "__main__":
    print("Space Station Data Validation\n"
          "========================================")

    # Create a valid space station
    international_space_station = SpaceStation(
        station_id="ISS001",
        name="International Space Station",
        crew_size=6,
        power_level=85.5,
        oxygen_level=92.3,
        last_maintenance=datetime.now(),
        is_operational=True)

    print("Valid station created:")

    # Displays the station information
    show_station(international_space_station)

    print("\n========================================")

    # create an invalid space station
    print("Expected validation error:")
    try:
        international_space_station = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=21,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime.now(),
            is_operational=True)
    except ValidationError as e:
        print(f"{e.errors()[0]['msg']}")

    # # test: pass a string timestamp to last_maintenance
    # international_space_station = SpaceStation(
    #     station_id="ISS001",
    #     name="International Space Station",
    #     crew_size=6,
    #     power_level=85.5,
    #     oxygen_level=92.3,
    #     last_maintenance="2026-08-20",
    #     is_operational=True)

    # show_station(international_space_station, True)
