import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """
1.  Génère un identifiant aléatoire composé de 15 lettres minuscules.
    """
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass()
class Student:
    """
1.  Une classe représentant un étudiant.
    """

    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(default_factory=generate_id, init=False)

    def __post_init__(self):
        """
    1.  Initialise l'attribut login.
        """
        self.login = self.name[0].lower() + self.surname.lower()
