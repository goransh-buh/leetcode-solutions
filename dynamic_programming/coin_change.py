"""
Coin Change

Given coin denominations and an amount, find the minimum number of
coins needed to make that amount.

Approach: Bottom-up dynamic programming.
Time: O(amount * len(coins)), Space: O(amount)
"""

from typing import List


def coin_change(coins: List[int], amount: int) -> int:
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float("inf") else -1


if __name__ == "__main__":
    assert coin_change([1, 2, 5], 11) == 3
    assert coin_change([2], 3) == -1
    print("All tests passed.")
