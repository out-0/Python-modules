from enum import Enum
from pydantic import BaseModel, Field, ValidationError, model_validator
from pydantic_core import ErrorDetails, PydanticCustomError
from datetime import datetime
from typing import List, Self


class Rank(Enum):
    """Constant Ranks for a space crew"""

    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    """
    Crew model represent Individual crew member
    for space mission
    • member_id: String, 3-10 characters
    • name: String, 2-50 characters
    • rank: Rank enum
    • age: Integer, 18-80 years
    • specialization: String, 3-30 characters
    • years_experience: Integer, 0-50 years
    • is_active: Boolean, defaults to True
    """

    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    """
    Module for Mission with crew
    list and these fields:

    • mission_id: String, 5-15 characters
    • mission_name: String, 3-100 characters
    • destination: String, 3-50 characters
    • launch_date: DateTime
    • duration_days: Integer, 1-3650 days (max 10 years)
    • crew: List of CrewMember, 1-12 members
    • mission_status: String, defaults to "planned"
    • budget_millions: Float, 1.0-10000.0 million dollars
    """

    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime = Field(default_factory=datetime.now)
    duration_days: int = Field(ge=1, le=3650)
    crew: List[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def mission_validator(self) -> Self:
        """Validator for some rules for members according to mission"""

        # Check correct mission id
        if not self.mission_id.startswith("M"):
            raise PydanticCustomError(
                "CustomValueError", 'Mission ID must start with "M"'
            )
        # Check crew must have a Commander or Captain
        found: bool = False
        for member in self.crew:
            if member.rank == Rank.COMMANDER or member.rank == Rank.CAPTAIN:
                found = True
        if not found:
            # Using PydanticCustomError which more easier to access the message
            # of the error later.
            raise PydanticCustomError(
                "CustomValueError",
                "Mission Must have at least one Commander or Captain",
            )

        # Check long missions rules
        if self.duration_days > 365:
            # Extract the experienced member count
            experienced_count: int = len(
                [member for member in self.crew if member.years_experience > 5]
            )
            if experienced_count < len(self.crew) / 2:
                raise PydanticCustomError(
                    "CustomValueError",
                    ("Long missions (> 365 days) "
                     "need 50% experienced crew (5+ years)"),
                )

        # Validate that all crew members is active
        not_active: int = len(
            [member for member in self.crew if not member.is_active])
        if not_active > 0:
            raise PydanticCustomError(
                "CustomValueError", "All crew members must be active"
            )

        return self


def main() -> None:
    """Main demonstration"""

    print("\n==Space Mission Crew Validation==\n")

    print("Valid mission created:")

    # Create 3 members.

    sarah_connor: CrewMember = CrewMember(
        member_id="M001_M",
        name="Sarah Connor",
        rank=Rank.COMMANDER,
        age=55,
        specialization="Mission Command",
        years_experience=30,
    )

    john_smith: CrewMember = CrewMember(
        member_id="J002_M",
        name="John Smith",
        rank=Rank.LIEUTENANT,
        age=40,
        specialization="Navigation",
        years_experience=12,
    )

    alice_johnson: CrewMember = CrewMember(
        member_id="A003_M",
        name="Alice Johnson",
        rank=Rank.OFFICER,
        age=31,
        specialization="Engineering",
        years_experience=8,
    )

    # Create mars mission.

    mars_colony: SpaceMission = SpaceMission(
        mission_name="Mars Colony Establishment",
        mission_id="M2024_MARS",
        destination="Mars",
        duration_days=900,
        budget_millions=2500.0,
        crew=[sarah_connor, john_smith, alice_johnson],
    )

    print(f"Mission: {mars_colony.mission_name}")

    print(f"ID: {mars_colony.mission_id}")

    print(f"Destination: {mars_colony.destination}")

    print(f"Duration: {mars_colony.duration_days} days")

    print(f"Budget: ${mars_colony.budget_millions}M")

    print(f"Crew size: {len(mars_colony.crew)}")

    print("Crew members:")

    for member in mars_colony.crew:
        print(
            f"- {member.name} ({member.rank.value}) - {member.specialization}")

    print("\n")

    print("Expected validation error:")

    # Create invalid mission (no members)

    # Create an random member just to pass first field validation
    baba_yaga: CrewMember = CrewMember(
        member_id="X000_Z",
        name="Baba Yaga",
        rank=Rank.OFFICER,
        age=26,
        specialization="Communication",
        years_experience=5,
    )

    try:
        meta_exp: SpaceMission = SpaceMission(
            mission_name="Meta Exploration",
            mission_id="M2027_JAN",
            destination="Meta",
            duration_days=999,
            budget_millions=5500.0,
            crew=[baba_yaga],
        )
        del meta_exp

    except ValidationError as e:
        # Extract the list of errors from ValidationError object
        # since the ValidationError create list of errors happen
        # inside ModelValidator
        list_of_errors: List[ErrorDetails] = e.errors()
        # Extract specify first erros
        raised_error: ErrorDetails = list_of_errors[0]
        # Print the required msg since we use PydanticCustomError
        # so accessing msg is clearly than standard error
        print(raised_error["msg"])


main()
