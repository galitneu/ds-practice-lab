"""Select student code by default; reference mode is for explicit verification only."""
import importlib
import os

def exercise(number):
    package = "solutions" if os.getenv("USE_SOLUTIONS") == "1" else "src"
    return importlib.import_module(f"{package}.ex{int(number):02d}")
