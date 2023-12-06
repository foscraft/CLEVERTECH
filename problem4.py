def max_robbery_amount(house_values, knapsack_capacity):
    num_houses = len(house_values)
    # Create a 2D table to store the maximum values
    dp = [[0] * (knapsack_capacity + 1) for _ in range(num_houses + 1)]
    # Build the table using dynamic programming
    for i in range(1, num_houses + 1):
        for w in range(1, knapsack_capacity + 1):
            # If the current house can fit in the knapsack
            if w >= i:
                # Choose the maximum between robbing the current house or skipping it
                dp[i][w] = max(dp[i - 1][w], dp[i - 2][w - i] + house_values[i - 1])
            else:
                # If the house cannot fit, choose the value without robbing the current house
                dp[i][w] = dp[i - 1][w]

    # The result is stored in the bottom-right cell of the table
    return dp[num_houses][knapsack_capacity]

# Example Usage:
house_values = [6, 7, 1, 30, 8, 2, 4]
knapsack_capacity = 5
result = max_robbery_amount(house_values, knapsack_capacity)
print(result)
