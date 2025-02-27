# Author: Jacqueline Garcia
# GitHub username: Jgarcia2
# Date: 02/26/2025
# Description: reverse list

def reverse_list(vals):
    """
    Reverses the order of elements in the given list in place.
    
    Parameters:
    vals (list): A list of elements.
    
    Returns:
    None
    """
    left, right = 0, len(vals) - 1
    while left < right:
        vals[left], vals[right] = vals[right], vals[left]
        left += 1
        right -= 1
