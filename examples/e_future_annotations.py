# from __future__ import annotations


# We need to uncomment from __future__ import annotations at the top of
# the file for this to evaluate without raising a NameError.
class A:
    def f(self) -> A:
        return self
