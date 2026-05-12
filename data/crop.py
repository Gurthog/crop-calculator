import csv
from dataclasses import dataclass, fields

from .season import Season


@dataclass
class Crop:
    name: str
    seasons: list
    growth_time: int
    pierre_cost: int
    joja_cost: int
    sell_price: int

    @classmethod
    def from_csv(cls, filepath):
        """Return a list of Crops hydrated from a csv file"""
        # set None for nulls instead of attempting to type cast
        converters = {
            field.name: (lambda val, t=field.type: None if val == "" else t(val))
            for field in fields(cls)
        }
        crops = []
        with open(filepath) as f:
            reader = csv.DictReader(f)
            for row in reader:
                seasons = row["seasons"].upper().split("|")
                row["seasons"] = [Season[s] for s in seasons]
                typed_row = {k: converters[k](v) for k, v in row.items()}
                crops.append(Crop(**typed_row))
        return crops

