def solve(p, q):
    mem = {}

    def getKey(p, q):
        return str(p) + "-" + str(q)

    def autoSum(p, q):
        value = 0

        for k in range(p, q):
            value += (t(p, k) + t(k + 1, q))

        return value

    def t(p, q):
        key = getKey(p, q)

        if key not in mem:
            if p == q:
                r = 1
            else:
                r = max(
                    t(p + 1, q),
                    autoSum(p, q)
                )
            mem[key] = r

        return mem[key]

    return t(p, q)
