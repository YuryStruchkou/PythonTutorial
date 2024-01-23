from dataclasses import dataclass
from datetime import datetime


@dataclass()
class User:
    id: int
    first_name: str
    last_name: str
    birth_date: datetime
    height: int
    country: str
