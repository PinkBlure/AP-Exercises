def order_crossover(parent1, parent2, lower_bound, upper_bound):
    child1 = []

    for i in range(0, len(parent1)):
        if lower_bound <= i < upper_bound:
            child1.append(parent1[i])
        else:
            child1.append(0)

    aux = upper_bound
    while 0 in child1:
        if child1[aux] == 0:
            if parent2[aux] not in child1:
                child1[aux] = parent2[aux]
            else:
                ind = aux
                while parent2[ind] in child1:
                    ind = (ind + 1) % len(child1)
                child1[aux] = parent2[ind]

        aux = (aux + 1) % len(child1)

    return child1
