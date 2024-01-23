from dataclasses import dataclass
from cartItem import CartItem


@dataclass()
class Cart:
    id: int
    products: list[CartItem]
    userId: int
