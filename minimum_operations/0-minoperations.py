#!/usr/bin/python3
"""Minimum Operations module.

Provides a function that computes the fewest number of Copy All / Paste
operations needed to obtain exactly n 'H' characters in a file that
initially contains a single 'H'.
"""


def minOperations(n):
    """Return the fewest operations needed to get exactly n 'H' characters.

    The only allowed operations are 'Copy All' and 'Paste'. Building n
    characters requires one copy and (k - 1) pastes for every factor k of
    the multiplication chain, which costs k operations per factor. The
    minimum is therefore the sum of the prime factors of n.

    Args:
        n (int): the target number of 'H' characters.

    Returns:
        int: the minimum number of operations, or 0 if n is impossible to
        achieve (n is not an integer greater than 1).
    """
    if not isinstance(n, int) or n < 2:
        return 0

    operations = 0
    factor = 2
    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1
    return operations
