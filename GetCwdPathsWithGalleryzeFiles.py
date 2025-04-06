import os
from pathlib import Path

root = Path(os.getcwd())
print(list(root.rglob("*.galleryze")))