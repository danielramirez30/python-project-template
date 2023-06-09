# Python Project Template

## Install dependencies

Install `pipenv` to manage dependencies

> pip install --user pipenv

If you get a warning like

```
WARNING: The scripts pipenv and pipenv-resolver are installed in '/home/${REPLACE_UBUNTU_USERNAME_HERE}/.local/bin' which is not on PATH.
Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
```

Modify `PATH` system variable to use `pipenv`

> nano ~/.zshrc

Add the next line at the end of the file

> export PATH="$PATH:/home/${REPLACE_UBUNTU_USERNAME_HERE}/.local/bin"

Create `.env` file with environment variable (to create virtual environment inside the project folder)

> PIPENV_VENV_IN_PROJECT=1

Finally, install dependencies using pipenv

> pipenv install --dev

## Select virtual environment in VS Code

1. Open Command Prompt: Ctrl + Shift + P

2. Write `Python: Select Interpreter`

3. Select your virtual environment

> Should be something like `./.venv/bin/python`

## Test project with pytest

> pytest

Install pre-commit hooks in your repository to use `pytest`

> pre-commit install

Install commit linter hook to follow conventional commits guide [like here](https://www.conventionalcommits.org/en/v1.0.0/)

> commit-linter install

## Pylint

1. Open Command Prompt: Ctrl + Shift + P

2. Write `Python: Select Linter`

3. Select `pylint`

## Working with pipenv

-   To activate this project's virtual environment, run pipenv shell.
-   Alternatively, run a command inside the virtual environment with pipenv run.

## Template setup

1. Set `GH_TOKEN` secret using a personal access token to use semantic release
2. Set `PYPI_TOKEN` secret using an auth token from PyPI to upload your project
