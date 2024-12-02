def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.
    
    Parameters:
    coins (list): List of coin denominations.
    total (int): Target amount to achieve.
    
    Returns:
    int: Fewest number of coins needed to meet the total or -1 if it can't be met.
    """
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1