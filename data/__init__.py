from pathlib import Path

from .crop import Crop
from .season import Season


CROPS = Crop.from_csv(Path(__file__).parent / "crops.csv")

