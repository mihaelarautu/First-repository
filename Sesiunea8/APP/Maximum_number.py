def get_max(a, b, c):
    if a > b > c:
        return a
    if a < b > c:
        return b
    else:
        return c