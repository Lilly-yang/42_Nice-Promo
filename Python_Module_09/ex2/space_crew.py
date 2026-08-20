from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime
from enum import Enum


class Rank(Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def valide_mission(self) -> "SpaceMission":
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID not start with 'M'")

        crew_valide = 0
        for member in self.crew:
            if member.rank == Rank.COMMANDER or member.rank == Rank.CAPTAIN:
                crew_valide = 1
                break
        if not crew_valide:
            raise ValueError(
                "Mission must have at least one Commander or Captain"
                )

        if self.duration_days > 365:
            experienced_crews = 0
            for member in self.crew:
                if member.years_experience >= 5:
                    experienced_crews += 1
            if experienced_crews / len(self.crew) < 0.5:
                raise ValueError(
                    "Long missions (> 365 days) with less than 50% "
                    "experienced crew (5+ years)"
                )

        for member in self.crew:
            if not member.is_active:
                raise ValueError("crew member not active")

        return self


def show_mission(mission: SpaceMission, show_time: bool = False) -> None:
    if mission.mission_name:
        print(f"Mission: {mission.mission_name}")

    if mission.mission_id:
        print(f"ID: {mission.mission_id}")

    if mission.destination:
        print(f"Destination: {mission.destination} people")

    if show_time:
        print(f"Launch date: {mission.launch_date}")

    if mission.duration_days:
        print(f"Durations: {mission.duration_days} days")

    if mission.budget_millions:
        print(f"Budget: ${mission.budget_millions}M")

    crew_size = len(mission.crew)
    if crew_size:
        print(f"Crew size: {crew_size}")
        show_crew(mission.crew)


def show_crew(crew: list) -> None:
    print("Crew members:")
    for member in crew:
        print(f"- {member.name} ({member.rank}) - {member.specialization}")


if __name__ == "__main__":
    print("Space Mission Crew Validation\n"
          "========================================")

    # Create a valid space mission
    sarah = CrewMember(
        member_id="CM0",
        name="Sarah Connor",
        rank="commander",
        age=30,
        specialization="Mission Command",
        years_experience=8,
    )

    john = CrewMember(
        member_id="CM1",
        name="John Smith",
        rank="lieutenant",
        age=27,
        specialization="Navigation",
        years_experience=5,
    )

    alice = CrewMember(
        member_id="CM2",
        name="Alice Johnson",
        rank="officer",
        age=25,
        specialization="Engineering",
        years_experience=3,
    )

    mission = SpaceMission(
        mission_name="Mars Colony Establishment",
        mission_id="M2024_MARS",
        destination="Mars",
        launch_date=datetime.now(),
        duration_days=900,
        crew=[sarah, john, alice],
        budget_millions=2500.0,
    )

    print("Valid mission created:")

    # Displays the mission information
    show_mission(mission)

    print("\n========================================")

    # create an invalid space mission
    print("Expected validation error:")

    # Mission lack Commander or Captain
    try:
        mission = SpaceMission(
            mission_name="Mars Colony Establishment",
            mission_id="M2024_MARS",
            destination="Mars",
            launch_date=datetime.now(),
            duration_days=900,
            crew=[john, alice],
            budget_millions=2500.0,
        )
    except ValidationError as e:
        msg = e.errors()[0]['msg']
        msg = msg[len("Value error, "):]
        print(msg)

    # # invalide CrewMemer within SpaceMission
    # try:
    #     mission = SpaceMission(
    #         mission_name="Mars Colony Establishment",
    #         mission_id="M2024_MARS",
    #         destination="Mars",
    #         launch_date=datetime.now(),
    #         duration_days=900,
    #         crew=[sarah, john, alice,
    #               CrewMember(
    #                 member_id="CM3",
    #                 name="bob Y.",
    #                 rank="cadet",
    #                 age=17,
    #                 specialization="Nothing Specialized",
    #                 years_experience=0,)],
    #         budget_millions=2500.0,
    #     )
    # except ValidationError as e:
    #     msg = print(f"{e.errors()[0]['msg']}")
