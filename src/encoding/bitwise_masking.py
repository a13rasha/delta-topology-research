def directional_mask(direction: str) -> int:
    mapping = {
        "north": 0b0001,
        "south": 0b0010,
        "east": 0b0100,
        "west": 0b1000,
    }
    return mapping.get(direction.lower(), 0)


def apply_mask(value: int, direction: str) -> int:
    return value ^ directional_mask(direction)
