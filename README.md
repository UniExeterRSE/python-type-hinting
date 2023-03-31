# Type hinting in Python

Simon Kirby, March 2023

## Introduction

This is a quick project to go along with a small type hinting presentation. Examples have been written from scratch.

## Set-up and tooling

- `Poetry` has been used for virtual environment and dependency management. Ensure `Poetry` has been installed locally, and then navigate to the project root. Once at the project root, open a terminal instance, and run `poetry install`. More concisely, to get up and running, install `Poetry` and follow the commands shown below:

```console
git clone https://github.com/UniExeterRSE/python-type-hinting
cd python-type-hinting
poetry install
```

- Type hinting for this project has been managed with the VSCode Python extensions `Pylance` and `Pyright`. These extensions have been listed in `extensions.json` file. These can be installed manually through the VSCode extensions tab/GUI.
- A `settings.json` VSCode file has been also been created, indicating the type hinting setting that can be altered. `"python.analysis.typeCheckingMode": "strict"` can be set to `off`, `basic` or `strict`.
- Other static type checkers exist. These have not been use here, but please explore them. An obvious choice is `mypy`.

## Additional materials

- The accompanying presentation can be found in `.pptx` and `.pdf` formats in the `presentations` folder.
- A great crib sheet containing information on the basic Python types can be found on the MyPy site [here](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html).
- Additional information on type hinting in NumPy can be found [here](https://numpy.org/devdocs/reference/typing.html). However, type hint support is not mature in NumPy, and discussions are ongoing (see [PEP 646](https://peps.python.org/pep-0646/)).
- Even so, a generic type `np.typing.NDArray` has been created which can be used by type checkers. An example is shown below:

```python
>>> import numpy as np
>>> import numpy.typing as npt

>>> print(npt.NDArray)
numpy.ndarray[typing.Any, numpy.dtype[+ScalarType]]

>>> print(npt.NDArray[np.float64])
numpy.ndarray[typing.Any, numpy.dtype[numpy.float64]]

>>> NDArrayInt = npt.NDArray[np.int_]
>>> a: NDArrayInt = np.arange(10)

>>> def func(a: npt.ArrayLike) -> npt.NDArray[Any]:
...     return np.array(a)
```

Note that `shape` and `dtype` support are in development, and liable to change.

- As well as the above, additional libraries have appeared to help the situation, such as [nptyping](https://github.com/ramonhagenaars/nptyping). This has not been tested, so your mileage may vary.
