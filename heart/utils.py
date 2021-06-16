from itertools import count, takewhile


def make_key_times(num_count):
    """
    return: list of key times points
    should append `1` because the svg keyTimes rule
        5 -> 0;0.2;0.4;0.6;0.8;1
    """
    s = list(takewhile(lambda n: n < 1, count(0, 1 / num_count)))
    if not round(s[-1], 2) == 1.0:
        s.append(1)
    return ";".join([str(round(i, 2)) for i in s])


def make_key_values(num_count, index):
    l = ["0"] * (num_count + 1)
    l[index] = "1"
    return ";".join(l)


def intersperse(lst, item):
    result = [item] * (len(lst) * 2 - 1)
    result[0::2] = lst
    return result
