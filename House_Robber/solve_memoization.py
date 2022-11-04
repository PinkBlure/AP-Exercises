#    t(n) = max (t(n-2) + v[n], t(n-1))
#    t(n) = 0		               : si n<0

def solve_memoization(items):
    mem = {}

    def t(n):
        key = n
        if key not in mem:
            if n < 0:
                r = 0
            else:
                r = max(t(n - 2) + items[n], t(n - 1))

            mem[key] = r
        return mem[key]

    return t(len(items) - 1)
    
