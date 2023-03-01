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
        """

        self.inventory: dict[str, float] = {}
        self.total_stock_value: float = 0
        self.price_list: dict[str, float] | None = None

    def bulk_add_inventory(self, car_models: list[str], model_counts: list[int]):
        if len(car_models) != len(model_counts):
            raise ValueError("car_models and model_counts must be the same length.")

        self.inventory = dict(zip(car_models, model_counts))

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
            print("Price list must be obtained from head office before calculating stock value.")

        else:
            average_car_price = sum(self.price_list.values()) / len(self.price_list)

            total_stock_value = 0
            for model_name, stock_count in self.inventory.items():
                if model_name in self.price_list:
                    average_model_price = self.price_list[model_name]
                    total_stock_value += stock_count * average_model_price

                else:
                    total_stock_value += stock_count * average_car_price

            self.total_stock_value = total_stock_value

        return self.total_stock_value


if __name__ == "__main__":
    showroom = Showroom()
    print(showroom.inventory)

    car_models: list[str] = ["bmw", "mercedes", "ferrari"]
    car_counts: list[int] = [1, 2, 54]

    showroom.bulk_add_inventory(car_models, car_counts)

    print(showroom.inventory)

    total_stock_value = showroom.calculate_stock_value()

    price_list: dict[str, float] = {
        "citroen": 2043.54,
        "audi": 5673.5,
        "kia": 3265.78,
    }

    showroom.obtain_price_list(price_list)
    total_stock_value = showroom.calculate_stock_value()

    print(total_stock_value)
