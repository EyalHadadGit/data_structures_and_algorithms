def zeroOneKnapsack_top_down(weights, profits, capacity, memo, current_index=0):
    if current_index == len(weights):
        return 0
    key = (current_index, capacity)
    if key not in memo:
        dont_choose = zeroOneKnapsack_top_down(weights, profits, capacity, memo, current_index + 1)
        choose = 0
        if weights[current_index] <= capacity:
            choose = profits[current_index] + zeroOneKnapsack_top_down(weights, profits, capacity - weights[current_index], memo, current_index + 1)
        memo[key] = max(choose, dont_choose)
    return memo[key]

def zeroOneKnapsack_bottom_up(weights, profits, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)] # dp table: (n+1) x (capacity+1)
    for i in range(1, n + 1):
        for c in range(capacity + 1):
            dp[i][c] = dp[i - 1][c] # don't take item i-1
            if weights[i - 1] <= c: # take item i-1 (if possible)
                dp[i][c] = max(dp[i][c], profits[i - 1] + dp[i - 1][c - weights[i - 1]])
    return dp[n][capacity]

