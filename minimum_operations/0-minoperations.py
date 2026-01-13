#!/usr/bin/python3
"""
Module for calculating minimum operations needed to reach n H characters
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to result in exactly
    n H characters in the file.
    
    Args:
        n: Target number of H characters
        
    Returns:
        Integer representing minimum number of operations, or 0 if impossible
    """
    if n <= 1:
        return 0
    
    operations = 0
    divisor = 2
    
    # Find all prime factors and sum them
    while n > 1:
        # While n is divisible by current divisor
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1
    
    return operations
