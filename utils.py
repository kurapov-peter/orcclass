
def normalize_rounding(n):
    if round(0.5) != 1 and n % 1 == .5 and not int(n) % 2:
        return int((round(n) + (abs(n) / n) * 1))
    else:
        return int(round(n))


def get_coordinate_for_int(n, size):
    result = []
    while n:
        n, r = divmod(n, 3)
        result.append(r)
    leading_zeroes = [0] * (size - len(result))
    return leading_zeroes + list(reversed(result))


def get_int_for_coordinates(coords):
    out = 0
    prod = 1
    for bit in reversed(coords):
        out += bit * prod
        prod *= 3
    return out


def get_euclid_distance(vector1, vector2):
    assert len(vector1) == len(vector2)
    dist = 0
    for i in range(len(vector1)):
        dist += abs(vector1[i] - vector2[i])
    return dist