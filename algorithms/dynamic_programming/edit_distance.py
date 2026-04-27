# Time Complexity: O(n * m)
# Space Complexity:
# - Top-down: O(n * m)
# - Bottom-up: O(n * m)

def edit_distance_top_down(s1, s2, memo, index1=0, index2=0):
    if index1 == len(s1):
        return len(s2) - index2
    if index2 == len(s2):
        return len(s1) - index1
    if s1[index1] == s2[index2]: # this line is the key idea: the minimal number of operations is the one that maximizes the number of iterations in which s1[i1] == s2[i2]
        return edit_distance_top_down(s1, s2, memo, index1 + 1, index2 + 1)
    dict_key = (index1, index2)
    if dict_key not in memo:
        delete_op = 1 + edit_distance_top_down(s1, s2, memo, index1, index2 + 1)
        insert_op = 1 + edit_distance_top_down(s1, s2, memo, index1 + 1, index2)
        replace_op = 1 + edit_distance_top_down(s1, s2, memo, index1 + 1, index2 + 1)
        memo[dict_key] = min(delete_op, insert_op, replace_op)
    return memo[dict_key]

def edit_distance_bottom_up(s1, s2):
    n, m = len(s1), len(s2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = i # delete all characters from s1
    for j in range(m + 1):
        dp[0][j] = j # insert all characters into s1
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] # no operation
            else:
                delete_op = dp[i - 1][j]
                insert_op = dp[i][j - 1]
                replace_op = dp[i - 1][j - 1]
                dp[i][j] = 1 + min(delete_op, insert_op, replace_op)
    return dp[n][m]


