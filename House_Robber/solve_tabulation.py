#    t(n) = max (t(n-2) + v[n], t(n-1))
#    t(n) = 0		               : si n<0

def solve_tabulation(items):
    table = [items[0], max(items[0], items[1])]

    def fill_table():
        for i in range(2, len(items)):
            table.append(max(table[i-2] + items[i], table[i-1]))
        return

    fill_table()

    return table[-1]
