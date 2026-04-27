# Time Complexity: O(n)
# Space Complexity: O(n)

def fib_top_down(n, memo):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n not in memo:
        memo[n] = fib_top_down(n-1, memo) + fib_top_down(n-2, memo)
    return memo[n]

def fib_bottom_up(n):
    if n <= 1:
        return n
    fib_list = [0] * (n + 1)
    fib_list[1] = 1
    for i in range(2, n + 1):
        fib_list[i] = fib_list[i-1] + fib_list[i-2]
    return fib_list[n]

