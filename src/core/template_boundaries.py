from dataclasses import dataclass, field


@dataclass
class BoundaryTemplate:
    north: int = 0
    south: int = 0
    east: int = 0
    west: int = 0
    padding_zeros: int = 0

    def as_dict(self):
        return {
            "north": self.north,
            "south": self.south,
            "east": self.east,
            "west": self.west,
            "padding_zeros": self.padding_zeros,
        }


def default_boundary_template() -> BoundaryTemplate:
    return BoundaryTemplate(
        north=1,
        south=1,
        east=1,
        west=1,
        padding_zeros=2,
    )
