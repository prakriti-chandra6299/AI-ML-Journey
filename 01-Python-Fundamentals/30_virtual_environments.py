
"""
LESSON 30: VIRTUAL ENVIRONMENTS, PIP AND REQUIREMENTS

REVISION NOTES
--------------
1. Virtual Environment:
   An isolated Python environment for a project.

2. venv:
   Python's built-in module for creating virtual environments.

3. pip:
   Python package installer.

4. requirements.txt:
   Stores project dependencies and their versions.

5. Activation:
   Enables the virtual environment in the current terminal.

6. Deactivation:
   Returns the terminal to its previous Python environment.

7. Best Practice:
   Use python -m pip to install packages into the
   currently selected Python environment.
"""

import sys
import os
import importlib.util


# ==================================================
# 1. CHECK PYTHON VERSION
# ==================================================

print("PYTHON ENVIRONMENT INFORMATION")
print("-" * 35)

print("Python version:", sys.version)
print("Python executable:", sys.executable)


# ==================================================
# 2. CHECK WHETHER VIRTUAL ENVIRONMENT IS ACTIVE
# ==================================================

# sys.prefix and sys.base_prefix help identify
# whether Python is running inside a virtual environment.

if sys.prefix != sys.base_prefix:
    print("\nVirtual environment: ACTIVE")
else:
    print("\nVirtual environment: NOT ACTIVE")


# ==================================================
# 3. CHECK THE CURRENT WORKING DIRECTORY
# ==================================================

print("\nCurrent working directory:")
print(os.getcwd())


# ==================================================
# 4. CHECK WHETHER A PACKAGE IS AVAILABLE
# ==================================================

# find_spec() checks whether Python can locate a module.

packages = ["numpy", "pandas", "matplotlib"]

print("\nPackage availability:")

for package in packages:

    available = importlib.util.find_spec(package) is not None

    if available:
        print(package, "- Available")
    else:
        print(package, "- Not installed")


# ==================================================
# 5. USING BUILT-IN MODULES
# ==================================================

# Built-in modules do not need pip installation.

import math
import json

print("\nBuilt-in module examples:")

print("Square root of 25:", math.sqrt(25))

sample_data = {
    "subject": "Python",
    "level": "Beginner"
}

json_string = json.dumps(sample_data)

print("JSON data:", json_string)


# ==================================================
# 6. IMPORTANT TERMINAL COMMANDS
# ==================================================

"""
CREATE VIRTUAL ENVIRONMENT:
    python -m venv .venv

ACTIVATE IN WINDOWS POWERSHELL:
    .\\.venv\\Scripts\\Activate.ps1

CHECK PYTHON:
    python --version

CHECK PIP:
    python -m pip --version

LIST PACKAGES:
    python -m pip list

INSTALL PACKAGE:
    python -m pip install package_name

UNINSTALL PACKAGE:
    python -m pip uninstall package_name

GENERATE REQUIREMENTS:
    python -m pip freeze > requirements.txt

INSTALL REQUIREMENTS:
    python -m pip install -r requirements.txt

DEACTIVATE:
    deactivate
"""


# ==================================================
# 7. IMPORTANT CONCEPTS
# ==================================================

"""
GLOBAL PYTHON:
    The Python installation available outside a
    project-specific virtual environment.

VIRTUAL ENVIRONMENT:
    An isolated environment for a project.

PIP:
    Installs and manages external Python packages.

REQUIREMENTS.TXT:
    Records the dependencies needed by a project.

IMPORTANT:
    Never upload the .venv folder to GitHub.
    It can be recreated using Python and requirements.txt.
"""
