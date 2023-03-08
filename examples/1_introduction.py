# Example of type annotations for simple variables/data structures

# We can annotate types outside function definitions
car_models: list[str] = ["bmw", "mercedes", "ferrari"]
car_counts: list[int] = [1, 2, 54]
inventory: dict[str, int] = dict(zip(car_models, car_counts))

inventory: dict[str, int] = {
    "citroen": 5,
    "audi": 5,
    "kia": 20,
}

average_car_prices: dict[str, float] = {
    "citroen": 2043.54,
    "audi": 5673.5,
    "kia": 3265.78,
}


# We can use type annotations for functions
def count_stock(inventory: dict[str, int]) -> int:
    """
    Function to count cars in inventory.

    Args:
        inventory: dictionary of inventory

    Returns:
        stock_count: the number of cars in inventory
    """

    stock_count = sum(inventory.values())

    return stock_count


def calculate_stock_value(inventory: dict[str, int], average_car_prices: dict[str, float]) -> float:
    """
    Calculate the (approximate) stock value of inventory with average prices. If no data is present
    for a model in stock, the average car price is used instead.

    Args:
        inventory: dictionary of inventory
        average_car_prices: dictionary containing average car prices in GBP

    Returns:
        stock_value: the approximate stock value in GBP
    """

    average_car_price = sum(average_car_prices.values()) / len(average_car_prices)

    total_stock_value = 0
    for model_name, stock_count in inventory.items():
        if model_name in average_car_prices:
            average_model_price = average_car_prices[model_name]
            total_stock_value += stock_count * average_model_price

        else:
            total_stock_value += stock_count * average_car_price

    return total_stock_value


def add_to_stock(inventory: dict[str, int], new_car_model: str):
    """
    Adds a new car to the inventory inplace.

    Args:
        inventory: dictionary of inventory
        new_car_model: the model of new car
    """

    if new_car_model in inventory:
        inventory[new_car_model] += 1

    else:
        inventory[new_car_model] = 1


def remove_from_stock(inventory: dict[str, int], car_model_to_remove: str):
    """
    Removes a car from the inventory.

    Args:
        inventory: dictionary of inventory
        car_model_to_remove: the model of car to remove
    """

    if car_model_to_remove not in inventory:
        raise ValueError(f"No cars of model {car_model_to_remove} in inventory.")

    current_stock = inventory[car_model_to_remove]

    if current_stock > 1:
        inventory[car_model_to_remove] -= 1

    else:
        del inventory[car_model_to_remove]
