#!/usr/bin/python3
"""Change comes from within"""


def makeChange(coins, total):
    """Given a pile of coins of different values, determine the fewest
    number of coins needed to meet a given amount total.

    Arguments:
        coins {list} -- List of the values of the coins in your possession
        total {int} -- Total to reach

    Returns:
        [int] -- Fewest number of coins needed to meet total
        0 if total is 0 or less
        -1 if total cannot be met by any number of coins you have
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    num_coins = 0
    for coin in coins:
        if total <= 0:
            break
        num_coins += total // coin
        total = total % coin

    if total > 0:
        return -1
    return num_coins
