def divide(a : int, b: int) -> int:
    i = 0
    for e in range(a, 0, -b): i += 1
    return i