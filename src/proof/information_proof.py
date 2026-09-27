from src.core.difference_calculus import structural_difference


def information_preservation_score(a: str, b: str) -> float:
    """A simple evidence score: keep it deterministic and interpretable."""
    delta = structural_difference(a, b)
    if not delta:
        return 1.0
    base = len(a) + len(b)
    score = (base - len(delta)) / base if base else 1.0
    return max(0.0, min(1.0, score))
