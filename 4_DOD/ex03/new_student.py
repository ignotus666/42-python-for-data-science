import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Creates and returns a random ID."""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """Represents a student with their data. Login and ID
    are not initialised. id calls generate_id for each student
    created so it's unique.
    """
    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(init=False, default_factory=generate_id)

    def __post_init__(self):
        """
        Takes care of creating a unique login from the name
        and surname.
        """
        try:
            assert len(self.name) > 0, "Must provide a name"
            assert len(self.surname) > 0, "Must provide a surname"

            self.login = self.name[0].upper() + self.surname.lower()

        except AssertionError as e:
            print("AssertionError:", e)
