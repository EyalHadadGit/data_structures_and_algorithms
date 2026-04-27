import numpy as np

def egg_drop_bottom_up(n_floors, n_eggs):
    if n_floors == 0:
        return 0
    if n_eggs == 0:
        return np.inf
    matrix = [[0] * (n_floors + 1) for _ in range(n_eggs + 1)]
    # each element in the matrix represents the worst result of the best strategy (the optimal worst-case scenario for that number of eggs and floors)
    # ignore the first row & first columns
    for i in range(n_floors + 1):
        matrix[1][i] = i # with one egg, the result is always N for N floors
    for i in range(1, n_eggs + 1): # with one floor, it's always one shot (for any n_eggs >= 1)
        matrix[i][1] = 1
    for j in range(2, n_eggs + 1):
        for i in range(2, n_floors + 1):
            # now you have i floors and j eggs. where should you throw the first egg?
            # you go floor by floor. in each floor, you want to know what is the worst-case scenario -
            # meaning, for each floor, you throw the egg, which either breaks or not, which gives you two options for additional throws. You take the maximum of those.
            # after checking all the options, you insert to cell (j, i) the minimal of all the numbers you computed.
            minimal_throws = i # 1 egg, i floors (starting from the maximal throws, obviously)
            for k in range(1, i + 1):
                broken_egg = matrix[j-1][k-1] + 1 # if the egg's broken, you are left with j-1 eggs and k-1 floors to examine; +1 for the broken egg
                not_broken_egg = matrix[j][i-k] + 1 # if it's unbroken, then you still have j eggs, and only have to examine floors from k+1 to i (i-k floors)
                minimal_throws = min(minimal_throws, max(broken_egg, not_broken_egg))
            matrix[j][i] = minimal_throws
    return matrix[-1][-1]

