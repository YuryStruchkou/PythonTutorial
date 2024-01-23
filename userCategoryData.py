from dataclasses import dataclass
from datetime import datetime


@dataclass()
class UserCategoryData:
    firstName: str
    lastName: str
    country: str
    birthDate: datetime
    height: int
    categories: list[str]
    categoriesTimes: int

    def __str__(self):
        return f"""
{self.firstName} {self.lastName} ({self.country}, born {self.birthDate}, height {self.height}): \
({self.categoriesTimes}, {self.categories})"""
