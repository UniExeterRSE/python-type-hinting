from dataclasses import dataclass
from typing import TypedDict


# TypedDicts declares a dictionary type that expects all of its instances to have a
# certain set of keys. Each key is associated with a value of a consistent type.
# We can use these for type hints, especially when returning more complex data structures.
class EngineAttributes(TypedDict):
    engine_type: str
    engine_size: str
    cylinders: float
    turbo: bool
    engine_location: str


@dataclass
class Car:
    """Class for a particular car item in inventory."""

    model: str
    year: int
    trim_package: str
    mass: float
    engine_type: str
    engine_size: str
    engine_location: str
    cylinders: int
    turbo: bool
    unit_price: float
    colour: str
    wheels: int
    seats: int

    def get_engine_attributes(self) -> EngineAttributes:
        """Return a dictionary of engine attributes."""

        return {
            "engine_type": self.engine_type,
            "engine_size": self.engine_size,
            "cylinders": self.cylinders,
            "turbo": self.turbo,
            "engine_location": self.engine_location,
        }


if __name__ == "__main__":
    car_data = {
        "model": "audi",
        "year": 2023,
        "trim_package": "RS",
        "mass": 1100.1,
        "engine_type": "Petrol",
        "engine_size": "3L",
        "engine_location": "Rear",
        "cylinders": 8,
        "turbo": True,
        "unit_price": 40003,
        "colour": "black",
        "wheels": 4,
        "seats": 4,
    }

    data_values = list(car_data.values())

    car = Car(*data_values)
    car.get_engine_attributes()
