# PYTHON PROJECT TEMPLATE

A template for python projects with virtual environment.

## HOW TO USE

### OPEN THE PYTHON INTERPRETER

The python interpreter to use for the scripts is `./venv/Scripts/python.exe`, as per usual in a python virtual environment.

Inside, libraries can be installed by activating the virtual environment from terminal, and then installing them via pip. These wil be saved in the file `requirements.txt`, via the script `requirements_tools.py`, as explained in the _REQUIREMENTS_ section.

### REQUIREMENTS

#### INSTALL REQUIREMENTS

To install requirements from `requirements.txt`, run

`python requirements_tools.py install [project_dir]`

from any python interpreter.

`[project_dir]` is defaulted to the project directory name.

#### SAVE REQUIREMENTS

To save requirements to `requirements.txt`, run

`python requirements_tools.py save [project_dir]`

from any python interpreter.

`[project_dir]` is defaulted to the project directory name.

