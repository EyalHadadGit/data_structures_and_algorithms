def longest_palindromic_subsequence_top_down(string, start_index, end_index, memo):
    if end_index == start_index:
        return 1
    if end_index < start_index:
        return 0
    key = (start_index, end_index)
    if key in memo:
        return memo[key]
    if string[start_index] == string[end_index]:
        memo[key] = 2 + longest_palindromic_subsequence_top_down(string, start_index + 1, end_index - 1, memo)
    else:
        memo[key] = max(
            longest_palindromic_subsequence_top_down(string, start_index + 1, end_index, memo),
            longest_palindromic_subsequence_top_down(string, start_index, end_index - 1, memo)
        )
    return memo[key]

def longest_palindromic_subsequence_bottom_up(string):
    n = len(string)
    rev = string[::-1]
    memo_matrix = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if string[i - 1] == rev[j - 1]:
                memo_matrix[i][j] = memo_matrix[i - 1][j - 1] + 1
            else:
                memo_matrix[i][j] = max(memo_matrix[i - 1][j], memo_matrix[i][j - 1])
    return memo_matrix[n][n]