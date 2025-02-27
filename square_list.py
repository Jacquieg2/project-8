# Author: Jacqueline Garcia
# GitHub username: Jgarcia2
# Date: 02/26/2025
# Description: Square list.

def square_list(nums):
    """
    Takes a list of numbers and replaces each value with its square.
    Mutates the original list.
    
    Parameters:
    nums (list): A list of numbers.
    
    Returns:
    None
    """
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2
