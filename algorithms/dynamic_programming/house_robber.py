# Time Complexity: O(n)

# Space Complexity:
# - Top-down: O(n)
# - Bottom-up: O(n)

def house_robber_top_down(houses, current_index, temp_dict): # top-down
    if current_index >= len(houses):
        return 0
    else:
        if current_index not in temp_dict:
            steal_house = houses[current_index] + house_robber_top_down(houses, current_index + 2, temp_dict)
            skip_house = house_robber_top_down(houses, current_index + 1, temp_dict)
            temp_dict[current_index] = max(steal_house, skip_house)
        return temp_dict[current_index]

def house_robber_bottom_up(houses): # bottom-up
    temp_arr_f = [0] * (len(houses) + 2)
    for i in range(len(houses) - 1, -1, -1):
        temp_arr_f[i] = max(houses[i] + temp_arr_f[i + 2], temp_arr_f[i + 1])
    return temp_arr_f[0]


