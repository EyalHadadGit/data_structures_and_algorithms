
def min_cost_to_cell_top_down(matrix_f, row=0, col=0):
    if row >= len(matrix_f) or col >= len(matrix_f[0]):
        return float('inf')

    if row == len(matrix_f) - 1 and col == len(matrix_f[0]) - 1:
        return matrix_f[row][col]

    return matrix_f[row][col] + min(
        min_cost_to_cell_top_down(matrix_f, row, col + 1),
        min_cost_to_cell_top_down(matrix_f, row + 1, col)
    )

def min_cost_to_cell_bottom_up(matrix_f):
    for col in range(1, len(matrix_f[0])):
        matrix_f[0][col] = matrix_f[0][col - 1] + matrix_f[0][col]
    for row in range(1, len(matrix_f)):
        matrix_f[row][0] = matrix_f[row - 1][0] + matrix_f[row][0]
    for row in range(1, len(matrix_f)):
        for col in range(1, len(matrix_f[0])):
            min_route = min(matrix_f[row - 1][col], matrix_f[row][col - 1])
            matrix_f[row][col] = min_route + matrix_f[row][col]
    return matrix_f[-1][-1]


