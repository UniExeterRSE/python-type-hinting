# Problem: You have a circular import issue.
# Solution: Import classes that are executed here.
import math
import typing

# Solution: Import classes used only for annotations when
# typing.TYPE_CHECKING is True (i.e. not at runtime).
if typing.TYPE_CHECKING:
    from b_classes import Showroom

if __name__ == "__main__":
    example_number = math.cos(1)
    showroom = Showroom()
