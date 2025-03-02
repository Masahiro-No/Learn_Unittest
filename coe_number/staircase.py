def staircase(n, display):
    stair = []
    if 0 < n <= 30:
        for i in range(1, n + 1):
            stair.append(" " * (n - i) + display * i)
        return "\n".join(stair)
    return "Invalid input!"