from typing import Callable, List, Any


def witness_check(fn: Callable[..., bool], *args, **kwargs) -> bool:
    try:
        return bool(fn(*args, **kwargs))
    except Exception:
        return False


def consensus(validators: List[Callable[..., bool]], *args, **kwargs) -> bool:
    if not validators:
        return False
    outcomes = [witness_check(v, *args, **kwargs) for v in validators]
    return all(outcomes) and len(outcomes) > 0
