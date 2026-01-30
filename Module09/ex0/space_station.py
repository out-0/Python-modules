from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
from typing import Optional


class SpaceStation(BaseModel):
    """
    pydantic base stations model
    validate data and ensure correctness
    Validation constraints:
                ge == greater than or equal, le == less than or equal
    default_factory: each instance will call it to have its current time.

    Arguments:
        - station_id: represent the identifier of the station
        - name: station name
        - crew_size: crew size (people count)
        - power_level: power level (percent)
        - oxygen_level: oxygen level (percent)
        - last_maintenance: date of the last maintenance (default=current time)
        - is_operational: status of station (operational or not)
        - notes: Optional note for station (default=nothing)

    Return:
        return a Model of SpaceStation inform the station status.
    """

    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime = Field(default_factory=datetime.now)
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(default=None, max_length=200)


def main() -> None:
    """Main entry point"""

    # Create station instance
    alpha_station: SpaceStation = SpaceStation(
                                            station_id="ISS001",
                                            name="International Space Station",
                                            crew_size=6,
                                            power_level=85.5,
                                            oxygen_level=92.3,
                                            is_operational=True,
                                               )

    print("\n== Space Station Data Validation ==\n")

    print("Valid station created:")
    print(f"ID: {alpha_station.station_id}")
    print(f"Name: {alpha_station.name}")
    print(f"Crew: {alpha_station.crew_size} people")
    print(f"Power: {alpha_station.power_level}%")
    print(f"Oxygen: {alpha_station.oxygen_level}%")
    print(f"Status: {('Operational'
                      if alpha_station.is_operational
                      else 'non-operational')}")

    print('\n')
    print("Invalid station created:")
    # This will fail cause crew outbound the range
    try:
        delta_station: SpaceStation = SpaceStation(
                                                station_id="ABB002",
                                                name="Uneverse Space Station",
                                                crew_size=24,
                                                power_level=95.5,
                                                oxygen_level=92.3,
                                                is_operational=False
                                                )
        # This line just to silent flake for unused local variables
        del delta_station

    except ValidationError:
        print("Input should be less than or equal")


main()
