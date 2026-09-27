from typing import List, Tuple


def encode_delta(delta: List[Tuple[int, str, str]]) -> str:
    """A very light, self-describing serialization inspired by compact binary-style record encoding."""
    encoded = []
    for idx, old, new in delta:
        encoded.append(f"{idx}:{old}->{new}")
    return "|".join(encoded)


def decode_delta(blob: str) -> List[Tuple[int, str, str]]:
    result = []
    for chunk in blob.split("|"):
        if not chunk:
            continue
        idx_part, rest = chunk.split(":", 1)
        old, new = rest.split("->", 1)
        result.append((int(idx_part), old, new))
    return result
