from src.core.difference_calculus import structural_difference


def test_666666_to_936693():
    delta = structural_difference("666666", "936693")
    print("delta:", delta)
    print("length:", len(delta))
    return delta


if __name__ == "__main__":
    test_666666_to_936693()
