from dataclasses import dataclass


@dataclass()
class Product:
    id: int
    title: str
    category: str
