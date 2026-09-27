from typing import List, Tuple


def structural_difference(a: str, b: str) -> List[Tuple[int, str, str]]:
    """Return index-wise differences between two strings."""
    max_len = max(len(a), len(b))
    result: List[Tuple[int, str, str]] = []
    for i in range(max_len):
        left = a[i] if i < len(a) else "∅"
        right = b[i] if i < len(b) else "∅"
        if left != right:
            result.append((i, left, right))
    return result


def delta_signature(a: str, b: str) -> str:
    """Create a compact symbolic signature for a transformation."""
    diffs = structural_difference(a, b)
    return "|".join(f"{idx}:{old}->{new}" for idx, old, new in diffs)


def example_666666_to_936693() -> List[Tuple[int, str, str]]:
    """A concrete non-standard example from the research narrative."""
    return structural_difference("666666", "936693")
