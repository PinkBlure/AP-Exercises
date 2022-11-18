from collections import namedtuple

Item = namedtuple("Item", ['index', 'value', 'weight'])


def solve_memoization(items, capacity):
    mem = {}

    def getKey(n, w):
        return str(n) + "-" + str(w)

    def t(n, w):
        key = getKey(n, w)

        if key not in mem:
            if n < 0 or w == 0:
                r = 0
            elif items[n].weight > w:
                r = t(n - 1, w)
            else:
                r = max(
                    t(n - 1, w),
                    t(n - 1, w - items[n].weight) + items[n].value
                )

            mem[key] = r
        return mem[key]

    return t(len(items) - 1, capacity)
