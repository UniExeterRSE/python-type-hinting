# Lets create a class for our showroom
class Showroom:
    """
    Class for our car inventory.
    """

    def __init__(self):
        """
        Constructor for Showroom class.

        Attributes:
            inventory: dictionary containing inventory
            total_stock_value: total stock value in GBP
            price_list: dictionary of currently advised model sale prices in GBP
            is_open: boolean flag indicating whether showroom is open, defaults to False
        """

        self.inventory: dict[str, float] = {}
        self.total_stock_value: float = 0
        self.price_list: dict[str, float] | None = None
        self.is_open: bool = False

    def bulk_add_inventory(self, car_models: list[str], model_counts: list[int]):
        """
        Bulk add multiple inventory items based on lists of car_models and model_counts.
        Note that car_models and model_counts must be the same length.

        Args:
            car_models: list of car models
            model_counts: list of model counts
        """

        if len(car_models) != len(model_counts):
            raise ValueError("car_models and model_counts must be the same length.")

        self.inventory = dict(zip(car_models, model_counts))
        print(self.inventory)

    def obtain_price_list(self, price_list: dict[str, float]):
        """
        Obtain price list from head office.

        Args:
            price_list: dictionary of prices by model in GBP
        """

        self.price_list = price_list

    def calculate_stock_value(self) -> float | None:
        """
        Calculate the stock value given the price list on file and return the value.

        Returns:
            total_stock_value: total value of stock given a price list
        """

        if self.price_list is None:
            raise ValueError("Price list must be obtained from head office before calculating stock value.")

        average_car_price = sum(self.price_list.values()) / len(self.price_list)

        total_stock_value = 0
        for model_name, stock_count in self.inventory.items():
            if model_name in self.price_list:
                average_model_price = self.price_list[model_name]
                total_stock_value += stock_count * average_model_price

            else:
                total_stock_value += stock_count * average_car_price

        self.total_stock_value = round(total_stock_value, 2)

        print(f"Total stock value: £{self.total_stock_value}")

        return self.total_stock_value


def open_showrooms(showroom_list: list[Showroom]):
    """
    Open a number of showrooms.

    Args:
        showroom_list: list of showrooms to open
    """

    for showroom in showroom_list:
        showroom.is_open = True

    print("All showrooms are now open!")


if __name__ == "__main__":
    # Create showroom
    showroom = Showroom()

    # Create inventory items and add to inventory
    car_models: list[str] = ["bmw", "mercedes", "ferrari"]
    car_counts: list[int] = [1, 2, 54]
    showroom.bulk_add_inventory(car_models, car_counts)

    # Obtain price list and calculate stock value
    total_stock_value = showroom.calculate_stock_value()
    price_list: dict[str, float] = {
        "citroen": 2043.54,
        "audi": 5673.5,
        "kia": 3265.78,
    }
    showroom.obtain_price_list(price_list)
    total_stock_value = showroom.calculate_stock_value()

    # Create a list of showrooms (1 for now) and open them
    showroom_list = [showroom]
    open_showrooms(showroom_list)
