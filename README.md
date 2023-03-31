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
