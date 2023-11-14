# __init__.py
print("Initializing source files...")

from .generators.complete import complete
from .generators.small_world import small_world

__all__ = ["complete", "small_world"]
