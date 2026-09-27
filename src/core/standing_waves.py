from typing import List, Tuple


def standing_wave_positions(deltas: List[Tuple[int, str, str]]) -> List[int]:
    """Very small prototype for recurring positions."""
    positions = [idx for idx, _, _ in deltas]
    uniq = []
    seen = set()
    for pos in positions:
        if pos not in seen:
            uniq.append(pos)
            seen.add(pos)
    return uniq


def standing_wave_summary(deltas: List[Tuple[int, str, str]]) -> dict:
    positions = standing_wave_positions(deltas)
    return {
        "unique_positions": positions,
        "count": len(positions),
    }
