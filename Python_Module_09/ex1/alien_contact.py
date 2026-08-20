from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime
from enum import Enum


class ContactType(Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime  # DateTime of contact
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: str | None = Field(default=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode='after')
    def validate_contact(self) -> "AlienContact":
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC' (Alien Contact)")
        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")
        if (
            self.contact_type == ContactType.TELEPATHIC
            and self.witness_count < 3
        ):
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses"
            )
        if self.signal_strength > 7.0 and self.message_received is None:
            raise ValueError(
                "Strong signals (> 7.0) should include received messages"
            )

        return self


def show_report(report: AlienContact,
                show_time: bool = False,
                show_verified: bool = False) -> None:
    if report.contact_id:
        print(f"ID: {report.contact_id}")

    if show_time:
        print(f"contact datetime: {report.timestamp}")

    print(f"Type: {report.contact_type}")

    if report.location:
        print(f"Location: {report.location}")

    if report.signal_strength is not None:
        print(f"Signal: {report.signal_strength}/10")

    if report.duration_minutes:
        print(f"Duration: {report.duration_minutes} minutes")

    if report.witness_count:
        print(f"Witnesses: {report.witness_count}")

    if report.message_received is not None:
        print(f"Message: '{report.message_received}'")

    if show_verified:
        print(f"Verified: {report.is_verified}")


if __name__ == "__main__":
    print("Alien Contact Log Validation\n"
          "======================================")

    # Create a valid alien contact report
    report = AlienContact(
        contact_id="AC_2024_001",
        timestamp=datetime.now(),
        contact_type="radio",
        location="Area 51, Nevada",
        signal_strength=8.5,
        duration_minutes=45,
        witness_count=5,
        message_received="Greetings from Zeta Reticuli")

    print("Valid contact report:")

    # Displays the report information
    show_report(report)

    print("\n========================================")

    # create an invalid alien contact report
    print("Expected validation error:")
    # # Contact ID not start with "AC"
    # try:
    #     report = AlienContact(
    #         contact_id="BC_2024_001",
    #         timestamp=datetime.now(),
    #         contact_type="radio",
    #         location="Area 51, Nevada",
    #         signal_strength=8.5,
    #         duration_minutes=45,
    #         witness_count=5,
    #         message_received="Greetings from Zeta Reticuli")
    #     # show_report(report)
    # except ValidationError as e:
    #     msg = e.errors()[0]['msg']
    #     msg = msg[len("Value error, "):]
    #     print(msg)

    # #  Physical contact reports is not verified
    # try:
    #     report = AlienContact(
    #         contact_id="AC_2024_001",
    #         timestamp=datetime.now(),
    #         contact_type="physical",
    #         location="Area 51, Nevada",
    #         signal_strength=8.5,
    #         duration_minutes=45,
    #         witness_count=5,
    #         message_received="Greetings from Zeta Reticuli")
    #     # show_report(report)
    # except ValidationError as e:
    #     msg = e.errors()[0]['msg']
    #     msg = msg[len("Value error, "):]
    #     print(msg)

    #  Telepathic contact have less than 3 witnesses
    try:
        report = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime.now(),
            contact_type="telepathic",
            location="Area 51, Nevada",
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=2,
            message_received="Greetings from Zeta Reticuli")
        # show_report(report)
    except ValidationError as e:
        msg = e.errors()[0]['msg']
        msg = msg[len("Value error, "):]
        print(msg)

    # #  Strong signals (> 7.0) not include received messages
    # try:
    #     report = AlienContact(
    #         contact_id="AC_2024_001",
    #         timestamp=datetime.now(),
    #         contact_type="radio",
    #         location="Area 51, Nevada",
    #         signal_strength=8.5,
    #         duration_minutes=45,
    #         witness_count=5)
    #     # show_report(report)
    # except ValidationError as e:
    #     msg = e.errors()[0]['msg']
    #     msg = msg[len("Value error, "):]
    #     print(msg)
