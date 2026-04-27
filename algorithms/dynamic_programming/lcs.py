def longest_common_subsequence_top_down(s1, s2, memo, index1=0, index2=0):
    if index1 == len(s1) or index2 == len(s2):
        return 0
    key = (index1, index2)
    if key not in memo:
        if s1[index1] == s2[index2]:
            memo[key] = 1 + longest_common_subsequence_top_down(s1, s2, memo, index1 + 1, index2 + 1)
        else:
            memo[key] = max(longest_common_subsequence_top_down(s1, s2, memo, index1 + 1, index2),
                            longest_common_subsequence_top_down(s1, s2, memo, index1, index2 + 1))
    return memo[key]

def longest_common_subsequence_bottom_up(s1, s2):
    memo_matrix = [[0 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                memo_matrix[i][j] = memo_matrix[i - 1][j - 1] + 1
            else:
                memo_matrix[i][j] = max(memo_matrix[i - 1][j], memo_matrix[i][j - 1])
    return memo_matrix[len(s1)][len(s2)]

