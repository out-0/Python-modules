from enum import Enum
from pydantic import BaseModel, Field, model_validator, ValidationError
from datetime import datetime
from typing import Optional


class ContactType(Enum):
    """
    Constants for contact types

    The contact usually use one of those types to communicate
        - radio
        - visual
        - physical
        - telepathic
    """

    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    """
    Model for contacting aliens with informal info:

    - contact_id: String, 5-15 characters
    - timestamp: DateTime of contact
    - location: String, 3-100 characters
    - contact_type: ContactType enum
    - signal_strength: Float, 0.0-10.0 scale
    - duration_minutes: Integer, 1-1440 (max 24 hours)
    - witness_count: Integer, 1-100 people
    - message_received: Optional string, max 500 characters
    - is_verified: Boolean, defaults to False
    """

    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime = Field(default_factory=datetime.now)
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode="after")
    def contact_validation(self):
        """
        Model validator to validate some rules after
        the class created, and before the instance initialized

        'Decorator job is to wrap that custom validator
        based on its mode, since our case our case we
        use 'after' so the method will apply a classmethod
        and get registered with (PydanticDescriptorProxy)
        to be called just before the model instantiated,
        by that that object instance is already have the
        attributes which will be used by the validator
        and after checking it return the object self
        again so the instantiating complete correctly.'

        arguments:
            - its take the self which already have the attributes

        return:
            - return the object self after validation to continue
              initialization and assigning it.

        """

        if not self.contact_id.startswith("AC"):
            # The validator itself will catch that ValueError
            # and wrap it into ValidationError which u can caught
            # in your main or something when creating model instance.
            raise ValueError("Contact ID must start with 'AC'")

        if self.contact_type.value == ContactType.PHYSICAL.value and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")

        if self.contact_type.value == ContactType.TELEPATHIC.value and self.witness_count < 3:
            raise ValueError("Telepathic contact requires at least 3 witnesses")

        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError("Strong signals (> 7.0) should include received messages")

        return self


def main() -> None:
    """Entry point for demonstration"""

    print("\n==Alien Contact Log Validation==\n")

    print("Valid contact report:")
    zeta_report: AlienContact = AlienContact(
        contact_id="AC_2024_001",
        contact_type=ContactType.RADIO,
        location="Area 51, Nevada",
        signal_strength=8.5,
        duration_minutes=45,
        witness_count=5,
        message_received=("Greetings from Zeta Reticuli"),
    )

    print(f"ID: {zeta_report.contact_id}")
    print(f"Type: {zeta_report.contact_type.value}")
    print(f"Location: {zeta_report.location}")
    print(f"Signal: {zeta_report.signal_strength}/10")
    print(f"Duration: {zeta_report.duration_minutes} minutes")
    print(f"Witnesses: {zeta_report.witness_count}")
    print(f"Message: '{zeta_report.message_received}'")

    print("\n")
    print("Expected validation error:")

    try:
        nega_report: AlienContact = AlienContact(
            contact_id="AC_2024_001",
            contact_type=ContactType.TELEPATHIC,
            location="Area 54, Nevada",
            signal_strength=5.5,
            duration_minutes=35,
            witness_count=2,
            message_received=("Greetings from Negggalzo Man"),
        )
    except ValidationError as e:
        # The error caught is an collection (list) of errors
        # that returned as a list of informed errors by errors method
        # in the ValidationError(ValueError) inside pydantic_core waited by rust
        # so we should extract the first error in the list of ErrorDetails objects
        # and since the validation will stop when first error raised so thicnically
        # the list will containe one object, and access the msg attribute in the
        # desired ErrorDetails which first one to extract the desired error msg.
        
        # Usually we wont access to that message like that but to match the demo
        # output we going through it.
        all_errors = e.errors()
        first_error = all_errors[0]
        message_expected = first_error['msg']
        # Remove the additional inform string (Value error, )
        print(message_expected.replace("Value error, ", ""))


main()
