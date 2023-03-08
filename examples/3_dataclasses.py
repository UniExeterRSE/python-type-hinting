from dataclasses import dataclass


# Dataclasses make use of type hints
@dataclass(frozen=True)
class InventoryItem:
    """Class for an inventory item in a showroom."""

    vehicle_type: str
    model: str
    unit_price: float
    stock: int = 0

    def total_model_cost(self) -> float:
        """Calculate total cost of model in stock."""

        return self.unit_price * self.stock


if __name__ == "__main__":
    inventory_item = InventoryItem("car", "land_rover", 1000, 2)
    print(inventory_item.total_model_cost())
