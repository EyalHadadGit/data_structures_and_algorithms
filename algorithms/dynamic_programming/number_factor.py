# Time Complexity: O(n)
# Space Complexity: O(n)

## TASK:
def number_factor_top_down(num, memo):
    if num in (0, 1, 2) : return 1
    if num == 3: return 2
    if num not in memo:
        memo[num] = number_factor_top_down(num - 4, memo) + number_factor_top_down(num - 3, memo) + number_factor_top_down(num - 1, memo)
    return memo[num]

def number_factor_bottom_up(num):
    if num in (0, 1, 2) : return 1
    if num == 3: return 2
    num_factor_list = [0] * (num + 1)
    num_factor_list[0], num_factor_list[1], num_factor_list[2] = 1, 1, 1
    num_factor_list[3] = 2
    for i in range(4, num + 1):
        num_factor_list[i] = num_factor_list[i-1] + num_factor_list[i-3] + num_factor_list[i-4]
    return num_factor_list[num]

